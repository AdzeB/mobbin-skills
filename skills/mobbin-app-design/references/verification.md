# Runtime improvement loop

Agree on observable acceptance before editing. Verify the screen or journey the user will actually use, with synthetic or authorized data and the existing test tooling.

1. **Baseline:** record the app revision, build type, target OS/device, entry route, data/setup, and defect. Capture the current screen or flow if possible.
2. **Implement:** make a focused change against the screen contract. Keep business behavior and unrelated navigation intact.
3. **Exercise:** run the affected journey from its real entry point; observe the result rather than relying on successful compilation.
4. **Inspect:** open the relevant screenshots. For changed motion, inspect a full-speed recording and slow/review the questionable segment. Treat measured frame timing as separate evidence.
5. **Fix:** address the most consequential remaining defect and repeat affected checks, including nearby behavior that could regress.

## Choose checks by the change

| Surface | Useful runtime checks |
| --- | --- |
| Layout | Supported themes, small viewport, large text, long content, safe areas/insets |
| Inputs | Labels/autofill, focus sequence, keyboard coverage, validation, preserved values after failure |
| Submission | Pending, failed, retry, success, rapid double tap, interruption and reconciliation |
| Navigation | Entry/deep link, back/cancel, sheet dismissal, keyboard-visible back, post-completion history |
| Data | Relevant loading, empty, error, stale/offline, and success states |
| Accessibility | VoiceOver/TalkBack labels, states and focus; target sizes; contrast; reduced motion |
| Performance | Same release/profileable build and workload before/after, measured with native tools |

Test each affected target platform. Add tablet/landscape only if supported or changed. A single-platform pass must not be reported as cross-platform verification. Do not execute real payments, destructive actions, or external messages as test fixtures.

## Leave repeatable evidence

Prefer the project's existing E2E runner. Keep one focused scenario with assertions and screenshots that would fail if the reported defect returned. If no runner is available, provide exact manual steps with expected results, application identifiers, build/launch commands, and capture locations; label them unrun when appropriate.

Save evidence in the project's established location, otherwise `work/ui-verification/`. A compact record can be:

```text
Revision / platform / device / build:
Setup / command / scenario:
Expected / actual:
Screenshot or recording paths:
Measurement method and before/after, if applicable:
Remaining unverified states:
```

Stop when the agreed checks pass and no actionable in-scope defect remains. After two passes without progress, change the diagnostic or state the concrete blocker. Missing simulators, accounts, fixtures, or native dependencies are limitations to report, not reasons to invent a pass. Continue independent source work that can still be completed.
