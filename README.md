# Mobbin skills

Agent skills for researching real product interfaces with Mobbin MCP and building the result in **SwiftUI, Jetpack Compose, bare React Native, or Expo**.

An independent community project by [AdzeB](https://github.com/AdzeB). Not an official Mobbin product. Adapted from the MIT-licensed [Appllama skills](https://github.com/Appllama/appllama-skills), with attribution preserved.

## Install

From your project directory:

```sh
npx skills add AdzeB/mobbin-skills
```

Preview the available skills or install both for Codex without prompts:

```sh
npx skills add AdzeB/mobbin-skills --list
npx skills add AdzeB/mobbin-skills --skill mobbin-usage mobbin-app-design --agent codex --copy -y
```

Add `--global` for a personal installation. For team use, install in the project and commit the generated skill files and lockfile. `--copy` creates portable copies. Use `--skill mobbin-usage` or `--skill mobbin-app-design` to install either skill independently. The [Skills CLI](https://github.com/vercel-labs/skills) supports other agents through `--agent` or the interactive installer.

| Skill | Use it for |
| --- | --- |
| [mobbin-usage](skills/mobbin-usage/SKILL.md) | Search screens, flows, and web sections; inspect evidence; produce design decisions or continue into an authorized build |
| [mobbin-app-design](skills/mobbin-app-design/SKILL.md) | Implement mobile UI in the existing native/React Native/Expo stack, then exercise and improve the actual flow |

The research skill can study web interfaces. The app-design skill targets mobile implementation. Both work independently, and the design skill can use supplied references without MCP access.

## Connect Mobbin MCP

Installing skills does **not** configure or authenticate Mobbin. Use the [official setup guide](https://docs.mobbin.com/mcp/clients/overview) for your agent. Mobbin access depends on your account's plan.

For [Codex CLI](https://docs.mobbin.com/mcp/clients/codex-cli):

```sh
codex mcp add mobbin --url https://api.mobbin.com/mcp
codex mcp login mobbin
```

For the desktop app, use [Mobbin's Codex App instructions](https://docs.mobbin.com/mcp/clients/codex-app). Complete OAuth in the browser. [mcp.json](mcp.json) is a configuration example for clients using `mcpServers`, not an automatic installer; do not overwrite an existing client configuration.

The skills discover live tool schemas before use. They prefer standard search and reserve deep search for unresolved questions, following [Mobbin's current credit policy](https://docs.mobbin.com/ai-credits). They do not assume that Android references, pagination, or a particular optional parameter exist on every connection.

## Try it

> Use mobbin-usage to compare onboarding flows for a budgeting app. Cite the screens you inspect and keep this research only.

> Use mobbin-usage and mobbin-app-design to improve our Expo checkout. Keep our existing theme and navigation. Verify pending, failure, retry, and success.

> Use mobbin-app-design to polish this SwiftUI settings flow. Keep it native Swift and verify Dynamic Type, keyboard behavior, and back navigation.

> Use mobbin-app-design for our Android Compose onboarding. Adapt Mobbin references to Android conventions and verify system back and state restoration.

> Improve this bare React Native screen using Mobbin references. Keep React Navigation and our current dependencies. Repeat the runtime checks until the reported issues are resolved.

## What changed from the original

- Mobbin's actual screen/flow/section search model replaces Appllama tools and assumptions.
- Explicit native iOS, native Android, bare React Native, and Expo paths replace the Expo-first baseline.
- Focused research and evidence reuse replace fixed screen quotas and whole-catalog walks.
- Source links, partial-flow caveats, and observed/inferred/proposed distinctions keep claims traceable.
- Acceptance checks and a defect-driven loop replace an untestable promise of perfection.
- Existing architecture, brand choices, and native code are preserved; dependencies and optimizations need a concrete reason.

## Improve and verify

The skills include a research/refine and implement/verify loop. To improve the skills themselves, reproduce a failure with a prompt in [evals/scenarios.md](evals/scenarios.md), change the smallest relevant instruction, and rerun that scenario plus adjacent cases. Publish only sanitized notes, never Mobbin images or private project/account data. Routine skill use does not silently modify the package or schedule background work.

Run the real installer E2E with Node/npm and Python 3:

```sh
python3 scripts/check-install.py
# After publishing, also test GitHub delivery:
python3 scripts/check-install.py AdzeB/mobbin-skills
```

The check retains CLI transcripts and JSON results under `work/`. It verifies independent and paired installation, file integrity, bundled references/licenses, and the remote lockfile source. It does not authenticate Mobbin or prove mobile runtime behavior. See [evaluation results](evals/results.md) for what was actually verified.

## License and attribution

[MIT](LICENSE). Original copyright retained; see [ATTRIBUTION.md](ATTRIBUTION.md) for the source revision and changes. Mobbin and Appllama names and marks belong to their respective owners. This repository's license covers the skill materials, not third-party screens, images, logos, or product designs.
