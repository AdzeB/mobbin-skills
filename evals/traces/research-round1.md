# Mobbin usage forward test

Evidence status: **simulated**. I read only `skills/mobbin-usage/SKILL.md` and its linked `references/mcp.md`. No Mobbin requests, browser requests, external writes, credential access, or app changes occurred. Requests below are the exact canonical tool name and JSON arguments I would send under each supplied schema. No invented results are included.

## A. Compare budgeting onboarding, research only

Decision: compare when onboarding reaches a useful budgeting screen and whether optional setup can be deferred. No target OS was specified; use iOS as the reference platform, without inferring the app's implementation stack.

First simulated request:

```json
{"tool":"search_flows","arguments":{"query":"budgeting app onboarding from welcome through profile setup to the first budget or home screen","platform":"ios","limit":3}}
```

After the supplied synthetic result, record:

- App: Budget A.
- Returned source: `https://example.invalid/flow-a`.
- Tool metadata: `screenCount: 9`; preview indices 1, 5, and 9; captions welcome, profile, and home.
- Observed images: none. These are metadata and captions, not verified visible screen content.
- Unknown: six omitted positions, every screen's visual content, optionality, interactions, actual start/end completeness, and onboarding duration.

Next simulated request:

```json
{"tool":"search_flows","arguments":{"query":"budgeting app onboarding that lets users defer optional profile questions and reach their first useful budget screen","platform":"ios","limit":3}}
```

Then await its results. Deduplicate by returned URL; do not assume a second app was found. Do not invent a supported image-fetch or link-opening tool. If the only evidence remains incomplete metadata, close with that limitation instead of claiming a completed visual comparison.

Concise user response at the supplied evidence boundary:

> I’m using iOS references. [Budget A](https://example.invalid/flow-a) has nine indexed screens, but only three preview positions and captions were returned, with no images. That does not establish its full onboarding journey. I’m checking another flow before comparing when users reach a useful budgeting screen; any recommendation to defer optional setup remains a proposal.

Actions: maintain one compact research note; seek one additional relevant app; inspect images if actually returned; produce only evidence-backed comparisons and explicit gaps; make no app changes.

## B. Android checkout references

The supplied platform enum excludes Android. Supported iOS references can help compare checkout information hierarchy, but cannot establish Android conventions or behavior.

Next simulated request:

```json
{"tool":"search_screens","arguments":{"query":"checkout review showing order summary, delivery details, total fees, payment method, and place order button","platform":"ios","mode":"standard","limit":8}}
```

Concise user response before results:

> This Mobbin connection has no Android search. I’m looking at iOS checkout screens for cross-platform inspiration and will label them accordingly. Android navigation, controls, and interaction behavior still need separate verification.

Actions: inspect returned screens; retain exact source URLs; compare only visible hierarchy and states; distinguish proposed Android adaptations from observed iOS evidence. Do not pass `platform: "android"` or claim Android examples were found.

## C. Website pricing section

Next simulated request:

```json
{"tool":"search_sections","arguments":{"query":"pricing section with clear plan comparison, monthly and yearly billing switch, and a primary plan selection action","limit":3}}
```

Concise user response before results:

> I’ll look for pricing sections that make plan differences and the next action easy to understand, then share the strongest linked examples.

Actions: inspect the returned sections and choose a useful example based on visible content. Do not add `platform`, `mode`, `image_format`, or an exclusion field; this schema does not accept them. Do not infer that the user's product needs annual billing merely because it appears in the search.

## D. Subtle hierarchy, no AI credits

Next simulated requests: **none**. The two prior standard searches produced unrelated screens; there is no useful returned evidence to cite. Deep search is excluded by the explicit budget constraint. Stopping here is a conservative research-budget choice, not a claim that two total searches necessarily equal two refinements.

Concise user response:

> The two standard searches did not find a useful reference. I won’t use deep search under your no-credit constraint. My proposal is to separate primary and secondary content with spacing and modest type-weight changes, while keeping secondary text readable; that is design advice, not an observed Mobbin example.

Actions: state that the requested reference remains unfound; offer the proposal as provisional; use existing useful user references if supplied; perform no deep request and make no claim about current account balances or a verified credit policy.

## E. Improve an existing settings screen, disconnected

Next simulated tool requests: **none available**. No connected tools or usable source-file path were supplied. The screenshot is inaccessible. I will not manufacture an MCP tool, infer the framework, or claim to have edited or visually checked the app.

Concise user response:

> Mobbin is not connected; [setup instructions](https://docs.mobbin.com/mcp/clients/codex-app) are available. The source snippet does expose one issue: Save is disabled without explaining why. Show the actual blocking reason beside it and associate that text with the control. Share the screen and the code that decides when Save is disabled so I can complete and verify the improvement.

Concrete implementation contract from the available evidence:

- User job: understand whether settings can be saved and what must change before saving.
- Primary action: preserve Save and its existing eligibility rule.
- Disabled state: show a concise explanation derived from that rule. Do not assume the reason is a missing field, unchanged data, or a pending request.
- Recovery: update or remove the explanation when the eligibility condition changes.
- Accessibility: connect the explanation to Save using the existing framework's native semantics; do not presume HTML or invent a platform-specific API.
- Check once source/runtime access exists: reproduce each actual disabled reason, confirm its matching explanation, fix the condition, verify Save enables and the explanation updates, then exercise the normal save path.

Actions: prepare the above change from the snippet; once source access exists, inspect the eligibility predicate and all callers before changing it; reuse the app's current text and control primitives. A live Mobbin connection is not required for this code correction. In this controlled case, missing executable source/runtime is the implementation blocker, and missing screenshot is the visual verification blocker.

## F. Show an exact Mobbin screen with search only

Next simulated requests: **none**. `search_screens` is not an exact-link resolver. Searching for the supplied URL would not establish that a returned screen is the requested one.

Concise user response:

> This connection only supports search, so I can’t retrieve that exact screen. You can open the [supplied Mobbin link](https://mobbin.com/screens/example-reference), or attach its screenshot here so I can display the intended reference.

Actions: retain the supplied URL as a user reference, not as inspected evidence. Do not invent a screen ID, get-by-ID request, fetched image, or approximate substitute. Request the screenshot because exact fidelity is essential to this request.

## Concrete problems encountered

1. **Missing images have no explicit branch.** Case A reaches “look at the returned images,” but none exist. The broader evidence rules prevent fabrication, yet an explicit metadata-only outcome would make execution more deterministic. I retained captions as metadata and left visual comparison unresolved.
2. **Search/refinement counting is ambiguous.** In D, two prior searches could mean an initial query plus one refinement, while the skill says two unproductive refinements. I stopped because another request lacked a concrete new dimension and deep search was disallowed. A hard two-search limit was not inferred.
3. **Disconnected implementation has two distinct blockers.** E can still yield a useful contract from the snippet, but cannot yield an actual verified patch without the relevant file, eligibility predicate, and execution surface. The instruction to continue independent implementation is sound; the scenario does not contain enough source to claim implementation complete. The actual disabled reason must not be invented.
4. **No exact-link retrieval is available in F.** The reference document handles this directly. No workaround search was issued, and the missing screenshot was requested because exactness was the task.

All submitted request objects fit the supplied schemas. Research-only scope was retained in A; unsupported Android was not sent in B; optional parameters were not invented in C; deep search was not used in D; disconnected evidence was not presented as Mobbin findings in E; no substitute was represented as an exact match in F.
