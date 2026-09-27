#!/usr/bin/env python3
"""Exercise the real Skills CLI in empty projects; retain logs and byte checks."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def main():
    if len(sys.argv) > 2:
        raise SystemExit("Usage: check-install.py [local-directory|owner/repo]")
    root = Path(__file__).resolve().parents[1]
    source = sys.argv[1] if len(sys.argv) > 1 else str(root)
    if Path(source).is_dir():
        source = str(Path(source).resolve())
    elif not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", source):
        raise SystemExit("Source must be an existing directory or GitHub owner/repo")
    work = root / "work"
    work.mkdir(exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix="install-check-", dir=work))
    report = {"source": source, "cli": "skills@1.7.0", "status": "failed", "cases": []}
    cli = ["npx", "--yes", report["cli"]]
    env = dict(os.environ, DISABLE_TELEMETRY="1", NO_COLOR="1")

    def command(args, cwd, log):
        with log.open("w") as output:
            result = subprocess.run(
                cli + args, cwd=cwd, env=env, stdout=output,
                stderr=subprocess.STDOUT, text=True, timeout=180,
            )
        if result.returncode:
            raise RuntimeError(f"Skills CLI failed ({result.returncode}); see {log}")
        return log.read_text()

    try:
        names = sorted(p.name for p in (root / "skills").iterdir() if p.is_dir())
        assert names == ["mobbin-app-design", "mobbin-usage"], names
        listing = command(["add", source, "--list"], run, run / "discovery.log")
        assert all(name in listing for name in names), "Discovery missed a skill"
        for selected in [[name] for name in names] + [names]:
            label = "paired" if len(selected) > 1 else selected[0]
            project = run / label
            project.mkdir()
            command(
                ["add", source, "--skill", *selected, "--agent", "codex", "--copy", "-y"],
                project, run / f"{label}.log",
            )
            installed = project / ".agents" / "skills"
            assert sorted(p.name for p in installed.iterdir()) == selected, label
            lock = json.loads((project / "skills-lock.json").read_text())["skills"]
            assert sorted(lock) == selected, "Unexpected lockfile skills"
            hashes = {}
            for name in selected:
                original = root / "skills" / name
                target = installed / name
                assert not target.is_symlink(), "Expected portable copies"
                expected = {p.relative_to(original) for p in original.rglob("*") if p.is_file()}
                actual = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
                assert actual == expected, f"Incomplete or extra files in {name}"
                assert Path("LICENSE") in actual, f"Missing license in {name}"
                for relative in sorted(expected):
                    data = (target / relative).read_bytes()
                    assert not (target / relative).is_symlink(), relative
                    assert data == (original / relative).read_bytes(), f"Stale/changed {name}/{relative}"
                    hashes[f"{name}/{relative}"] = hashlib.sha256(data).hexdigest()
                if not Path(source).exists():
                    assert lock[name]["sourceType"] == "github", lock[name]
                    assert lock[name]["source"].lower() == source.lower(), lock[name]
            command(["list", "--agent", "codex", "--json"], project, run / f"{label}-list.json")
            report["cases"].append({"name": label, "status": "passed", "sha256": hashes})
        report["status"] = "passed"
    except Exception as error:
        report["error"] = str(error)
        raise
    finally:
        artifact = run / "result.json"
        artifact.write_text(json.dumps(report, indent=2) + "\n")
        print(f"{report['status']}: {artifact}", flush=True)


if __name__ == "__main__":
    main()
