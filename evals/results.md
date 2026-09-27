# Evaluation results

Date: 2026-09-27. Package version: 1.0.0.

## Actual execution

- Both skills passed the skill-creator frontmatter/naming validator.
- Relative documentation links, Codex UI metadata, and MCP configuration JSON were checked.
- Skills CLI **1.7.0** discovered both skills from the local source.
- Three fresh-project installation cases passed: app-design alone, usage alone, and both together. Every installed skill file matched the source bytes, including references and the MIT license. Installed Codex copies were regular files, and project lockfiles contained exactly the selected skills.
- The same three installation cases passed again after the research improvements. The final [local machine-readable result](install-local.json) records SHA-256 values. Full CLI transcripts remain in the executing checkout's ignored `work/install-check-*/` directories; rerun `python3 scripts/check-install.py` to produce a fresh artifact.
- Invalid installer source input was rejected before invoking the CLI.

GitHub delivery also passed all three fresh-project cases against public source `AdzeB/mobbin-skills` at commit `92d9b89`, including exact installed bytes and GitHub lockfile provenance. See the [remote machine-readable result](install-github.json). Public visibility was also confirmed with an unauthenticated GitHub API request. Reproduce with `python3 scripts/check-install.py AdzeB/mobbin-skills`.

## Usage iterations

Two independent evaluators executed 16 controlled decision scenarios across an initial pass and a targeted second pass. They received skill files and synthetic task/tool fixtures, without the expected outcomes. These are agent decision traces, not live product or MCP E2E results.

| Pass | Scope | Outcome |
| --- | --- | --- |
| [Research round 1](traces/research-round1.md) | Six cases: incomplete flows, Android fallback, section schema, no-credit searches, missing MCP, exact-link requests | Requests respected the supplied schemas and scope; exposed implicit handling of missing images and ambiguous refinement counting |
| [Platform routing](traces/platform-routing.md) | Six cases: Expo with maintained native code, bare RN, SwiftUI, Compose, payment history, repeated keyboard fix | Preserved the selected stack and existing architecture; retained receipts and pending-state reconciliation; disclosed missing runtime evidence |
| [Research round 2](traces/research-round2.md) | Four cases: metadata-only responses, exhausted refinements, injected instructions, reused references | Explicitly withheld visual claims without images, stopped unproductive searching, ignored source instructions, and continued a focused runtime fix without researching again |

Changes made from observed friction:

1. Added an explicit metadata-only branch when images cannot be viewed.
2. Clarified that the research bound is an initial search plus at most two unproductive refinements, with each call requiring an unanswered question or useful query change.
3. Kept schema discovery, source-platform labels, independent installation, stack preservation, and bounded runtime improvement as central requirements.

The checks found no remaining demonstrated decision failure in these traces. They do not establish a numeric improvement in agent performance or guarantee the same behavior on every model/project.

## Not verified

- Authenticated live Mobbin calls: no connected Mobbin tools were available in the authoring session. Official documentation was checked, but actual tool argument schemas, account permissions, returned images, and rate/credit behavior require a connected client.
- Actual mobile implementations, simulator/emulator flows, accessibility checks, and release-device performance. This task produced skills rather than a target app; platform exercises were simulations.
- Search-directory indexing or install popularity. A public GitHub install does not require a separate npm package, and successful installation does not prove listing/indexing elsewhere.

The next useful usage pass is a real connected Mobbin research task and one existing native or Expo app change, using the scenarios and evidence contract in this repository. Do not convert the simulations above into claims of live runtime validation.
