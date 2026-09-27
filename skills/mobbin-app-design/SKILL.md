---
name: mobbin-app-design
description: Build or refine mobile screens and flows using Mobbin references and native platform conventions. Use for SwiftUI, Jetpack Compose, bare React Native, or Expo UI implementation, navigation, accessibility, visual polish, and device verification.
license: MIT
metadata:
  author: AdzeB
  version: 1.0.0
---

# Mobbin app design

Deliver a usable screen or flow in the user's actual stack, with observable checks. Keep the product's identity, adopt useful reference patterns, and verify the result in the target runtime.

## Resolve the implementation path

Inspect project instructions, manifests, native project files, dependency versions, navigation, shared components, and theme tokens before editing. Expo projects can have `ios/` and `android/` directories; directories alone do not identify the workflow.

| Existing project or explicit request | Path |
| --- | --- |
| Expo dependencies/configuration | [Expo and React Native](references/expo-react-native.md), retaining its current native-project workflow |
| Bare React Native / React Native CLI | [Expo and React Native](references/expo-react-native.md), retaining the existing navigator and build tools |
| SwiftUI or UIKit Xcode app | [Native platforms](references/native.md), iOS section |
| Jetpack Compose or Android Views Gradle app | [Native platforms](references/native.md), Android section |

"Native feel" is a quality goal, not permission to change frameworks. For a new project, honor the requested stack. If the choice is unresolved and consequential, ask native or Expo while progressing the screen contract/research. Do not introduce Expo into a native app or replace React Navigation with Expo Router as a design fix.

## Establish a screen contract

Read the relevant flow end to end, including callers and state ownership. Identify the user's job, primary action, layout hierarchy, applicable states, navigation entry/exit, and expected back/cancel/retry behavior. For existing UI, capture the current screen and interaction before editing when runtime access exists.

Use provided references first. If Mobbin is connected, research the unanswered design decisions with `mobbin-usage` when installed. Otherwise discover Mobbin's actual search tools, use a small relevant sample, and cite returned links. Neither skill requires the other. If live research is unavailable, use supplied evidence or the existing design system and disclose the limitation.

Separate the source platform from the implementation OS. A screenshot can inform hierarchy, not prove gesture behavior or conversion. Annotate uncertain transitions as proposed. Keep this contract short enough to verify against the running app.

## Build with the platform

- Reuse existing controls, navigation, themes, and state patterns before adding dependencies. Use system controls or established wrappers where they fit; custom design is valid when the product requires it.
- Keep semantic color roles, readable hierarchy, consistent spacing/radii, and coherent iconography. Preserve intentional brand decisions rather than imposing a universal accent, font, or material rule.
- Support the app's themes and text scaling, safe areas/window insets, keyboard avoidance, long labels, and compact layouts. Add accessible labels, roles, states, focus order, and non-color feedback. Use platform target sizes, at least 44pt on iOS and 48dp on Android unless a larger project standard applies.
- Use persistent field labels, appropriate keyboard/autofill behavior, and errors with a recovery action. Do not change form control strategy or validation timing without a demonstrated need.
- Retain server/client/local state ownership. Preserve drafts on recoverable failure. Guard competing submissions; a pending payment or booking is not success. Optimistic updates are appropriate only when their consequences can be safely reversed.
- Use existing assets and platform icons. Generate new imagery only when the screen needs it, using a consistent art direction and authorized tools. Treat reference art as inspiration, not a distributable product asset.

## Navigation and recovery

Describe whether each destination is a peer tab, pushed detail, self-contained modal, or short sheet. Use the chosen platform's navigation model and preserve the user's place.

- Back changes location, not completed business events. After sign-in, onboarding, or payment, prevent stale forms from repeating work through state guards and appropriate stack updates. Receipts/history may remain reachable; do not erase unrelated history or ban all back navigation after success.
- A feature-scoped sign-in or purchase returns to that feature when complete. Cold start and deep links resolve session/loading state before showing a destination.
- Allow cancel/back where valid. Protect unsaved work using the existing navigation guard. If a request cannot be cancelled, explain its pending state and support reconciliation instead of trapping the user indefinitely.
- Test dismissal, interactive back cancellation, Android back, keyboard-visible back, and restored state where relevant. Native routes and application state need to agree after interruption.

## Motion and performance

Keep platform transitions unless the task calls for custom motion. Custom gestures should track the finger, preserve velocity when supported, and recover from interruption. Respect reduced motion and avoid delaying input for animation.

For performance work, measure the reported interaction first, change the identified bottleneck, then compare the same build type/device/data/workload. Use platform profiling tools. Screen recordings can reveal visual defects but do not establish frame timing. Do not force a new list, state, animation, or caching library without evidence it is needed.

## Verify and improve

Use [the runtime loop](references/verification.md). Exercise the requested flow in the actual app, fix the highest-impact defect, and repeat the affected checks. Keep improving within scope while evidence reveals actionable defects; do not keep redesigning a passing flow for taste alone.

Completion means the agreed screen/flow works and relevant verification passes. Report the files changed, checks actually run, evidence paths, and any unverified platform/state. If runtime access is missing, complete feasible implementation and provide a repeatable verification path, while stating runtime verification is blocked. Never replace that limitation with a claim that a build or static review proved the UX.
