# Mobbin MCP reference

Documentation checked on 2026-09-27. Live tool schemas take precedence over these examples. The REST API's schema is not automatically the MCP schema.

## Setup

The [official MCP](https://docs.mobbin.com/mcp/introduction) uses Streamable HTTP and browser-based OAuth. See [supported clients](https://docs.mobbin.com/mcp/clients/overview); the skill installer does not connect or authenticate MCP.

For [Codex CLI](https://docs.mobbin.com/mcp/clients/codex-cli):

```sh
codex mcp add mobbin --url https://api.mobbin.com/mcp
codex mcp login mobbin
```

For Codex App, follow the [app setup guide](https://docs.mobbin.com/mcp/clients/codex-app). Reuse an existing connection. Do not read stored OAuth tokens or write credentials into files. Account authorization is completed by the user.

## Capability check

Before first use, inspect the available schema for `search_screens`, `search_flows`, and `search_sections`. Confirm required arguments, supported platforms, mode enum, query length, result bounds, and any pagination fields. Use only the capabilities actually present. Older connections may expose fewer tools.

- Select the requested OS if supported. If Android is unavailable, state that limitation and use supported mobile references only when they help; label their actual platform. Never present iOS references as Android evidence.
- For mobile plus web comparison, keep results labeled by platform. A missing web-section tool can sometimes be covered by a supported web screen search, with that limitation stated.
- Use `image_format: "webp"`, exclusion IDs, or a page/cursor only if that specific tool accepts them. Follow returned pagination and do not guess a cursor.
- A supplied Mobbin link is the user's intended reference. Open it using a supported tool/browser if possible. Search is not an exact-link resolver; label substitutes and ask for the missing screen only when fidelity depends on it.

## Search cost and recovery

Mobbin [documents](https://docs.mobbin.com/ai-credits) `search_screens` modes `standard` and `deep`, with standard screen/flow/section search using no AI credits and successful deep searches using credits. Check current policy and the connected schema before making cost claims. Do not hard-code allowances, reset dates, beta terms, or balances.

Prefer standard search for clear screen types. Use deep search when nuanced visual intent remains unresolved, within the user's budget. An explicit no-credit constraint excludes deep search. Reuse prior useful results; repeated successful deep searches can consume credits again.

- Authentication/access failure: report it and point to official connection/account settings. Repeating the search cannot fix missing authorization.
- Invalid argument: reread the schema and correct the request; do not cycle guessed parameter names.
- Rate limit: honor `Retry-After`; without it, use bounded exponential backoff. Allow at most two retries per failed call and report continued failure. Do not wait beyond the task's time budget.
- Empty results: simplify the query, then broaden one dimension. Do not invent evidence.
- Credit limit: use available standard searches when sufficient and explain the deep-search limitation. Never promise an account reset date or purchase credits.
- Expired image: use the source link or a supported fresh search and verify identity. [Current documentation](https://docs.mobbin.com/mcp/features) describes temporary image URLs; record Mobbin source links and observations instead of treating media URLs as permanent IDs.

## Compact research record

For multi-step work, keep one note in the project's existing research location, or `work/mobbin-research.md` if none exists:

```text
Question and acceptance criterion:
Implementation stack / target OS:
Query / tool / mode / source platform:
App / returned source URL or ID:
Observed / inferred / proposed:
Decision / unresolved gap / next check:
```

Do not create a large reference archive for a one-screen question. Include only task-relevant notes, no tokens, personal account information, or proprietary screenshots in public evaluation artifacts.
