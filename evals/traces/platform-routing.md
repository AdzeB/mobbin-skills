# Independent forward test: mobile platform and runtime decisions

Date: 2026-09-27

This is a controlled implementation simulation. No apps, builds, simulators, payments, Mobbin queries, or external actions were run. The only generated artifact is this report. Commands below are proposed first actions, not execution evidence. Source filenames not present in the supplied fixture are illustrative roles to resolve with `rg`, not claims about a real repository.

## Inputs read

- `outputs/mobbin-skills/skills/mobbin-app-design/SKILL.md`
- Its references: `expo-react-native.md`, `native.md`, and `verification.md`
- `skill-creator/SKILL.md`, especially Independent Forward-Testing

No eval definitions, assertions, previous test results, or other agents' conclusions were read. The locally installed non-system `skill-creator` was initially read because two skills have the same name. It did not contain Independent Forward-Testing, so the system skill was then read and used for this task's evaluation method. No skill was edited.

## A. Expo checkout with a hand-edited Swift payment module

**User request:** “Polish checkout and keep its native feel.”

**Raw fixture:** `package.json` contains `expo: ~55.0.0`, `expo-router: ~7.0.0`, `react-native: 0.83.0`, and `acme-payments: 1.0.0`. There is an `ios/` project with hand-edited Swift payment integration. Expo Go is available. A custom development build is not available. No script names, checkout source paths, payment-provider capabilities, or simulator inventory were supplied.

**Implementing-agent response and decision trace:**

I will retain Expo, React Native, Expo Router, the existing theme, and the maintained iOS project. “Native feel” sets the quality bar for the checkout; it does not select SwiftUI or authorize regenerating native projects. I will first find the checkout route, its layout owner, the payment state hook/service, shared inputs/buttons, and the Swift integration's JavaScript entry point.

My first commands would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'package.json' -g '*lock*' -g 'app.config.*' -g 'app.json' -g '*.xcodeproj/project.pbxproj' -g '*.xcworkspace/contents.xcworkspacedata'
cat package.json
rg -n 'acme-payments|checkout|payment|KeyboardAvoidingView|useSafeAreaInsets' app src ios
git diff -- ios
```

The last search will use only directories that actually exist. I will inspect committed native configuration as well as the diff: hand-maintained code can already be committed. I will inspect the lockfile and native dependency setup rather than infer complete compatibility from the version strings alone. Before using new Expo Router APIs, I would consult the official docs matching the installed version.

I would edit the existing checkout route and its existing style/component files, plus the shared payment boundary only if the UI defect originates there. I would preserve the Swift payment module. The initial screen contract would specify total and fees, persistent field labels, one primary payment action, keyboard-visible CTA behavior, pending/failed/success feedback, and valid return paths.

Expo Go is useful only for parts of this checkout that can load and execute without unsupported native modules. An eagerly imported `acme-payments` module could prevent even the screen from loading there. I would not replace it with a fake adapter and call the payment flow verified. I would use an existing local native build script, or inspect the actual Xcode workspace/scheme and build that maintained project, if the local native toolchain and test device are available. I would not run `expo prebuild --clean`, overwrite `ios/`, or trigger a paid cloud build.

**Completion evidence I would provide:** exact changed files, before/after checkout screenshots on the supported target, a focused synthetic-payment scenario through pending/error/success, keyboard and back behavior, duplicate-submit prevention, and the build/device details. If only Expo Go can run, I would label its evidence as the supported UI subset. Full payment/native verification remains blocked until a compatible local development build and sandbox provider path are available. No performance claim would follow from Expo Go footage.

**Problem exposed by this fixture:** an available Expo Go runtime does not establish that this particular checkout can run. The skill provides a clear limitation and a non-destructive native build path; missing build configuration and provider test support remain genuine unknowns.

## B. Bare React Native account screen

**User request:** “Improve our React Native account screen.”

**Raw fixture:** React Native 0.82, `@react-navigation/native` 7, no Expo dependency, and checked-in `android/` and `ios/`. Navigator implementation, package manager, native run scripts, and test runner are not provided.

**Implementing-agent response and decision trace:**

I will keep the bare React Native project and its React Navigation integration. I will trace the account screen from the current navigator, reuse the app's account rows, form controls, safe-area handling, and theme tokens, and change only what the screen contract requires. I will not add Expo Router, Expo modules, or a new list library merely to polish a settings list.

My first commands would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'package.json' -g '*lock*' -g 'Podfile' -g 'build.gradle*' -g '*Account*' -g '*Navigation*' -g '*Theme*'
cat package.json
rg -n 'Account|create.*Navigator|NavigationContainer|SafeArea|Keyboard' src
```

I would then read the actual account screen and every relevant caller, including any account-edit, logout, or delete-account action. The chosen files would be the discovered account screen, a reused account-row component only if shared behavior needs correction, and existing styles/tokens. Platform-specific files would be added only for a concrete iOS/Android behavior difference.

I would use the repository's existing package-manager commands to build and launch each supported OS. `@react-navigation/native` alone does not identify whether the project uses native stack, JS stack, tabs, or another navigator, so I would not select navigation methods before inspecting its actual navigator packages and route configuration.

**Completion evidence I would provide:** account screenshots in the app's supported themes, small-screen/large-text coverage, accessible row labels and focus order, actual account entry/back behavior, and editing/error recovery if editing is changed. I would retain one existing E2E scenario or provide exact manual steps if no runner exists. An iOS-only run would be reported as iOS-only, even though React Native code is shared.

**Problem exposed by this fixture:** the installed navigation core package does not determine the navigator implementation. The skill's instruction to inspect and preserve the actual navigator prevents an unsupported assumption, but exact edits and run commands still need repository discovery.

## C. SwiftUI onboarding on iOS 17

**User request:** “Build native iOS onboarding with our current design system.”

**Raw fixture:** an existing SwiftUI Xcode app, minimum iOS 17, an existing design system, and no Node manifest. No workspace/scheme names, onboarding routes, persistence owner, or test target names are given.

**Implementing-agent response and decision trace:**

I will implement this in SwiftUI inside the existing Xcode app. I will read its app entry point, navigation/session state, theme definitions, reusable controls, and any existing first-run storage. I will not create a Node project or introduce Expo. I will stay within APIs supported by iOS 17 or explicitly use the project's established availability pattern.

My first commands would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g '*.swift' -g 'project.pbxproj' -g 'Package.swift' -g '*.xcscheme' -g 'contents.xcworkspacedata'
rg -n 'WindowGroup|NavigationStack|onboarding|AppStorage|Theme|DesignSystem' --glob '*.swift'
```

After resolving the actual workspace or project, I would inspect its schemes using `xcodebuild -list -workspace <actual-workspace>` or `xcodebuild -list -project <actual-project>`. Those are alternatives; I would use the one this repository already uses.

The chosen files would be a small onboarding view or the existing onboarding view, the existing app/session navigation owner for the entry and completion transition, and the current state store if an onboarding-complete field is required. I would reuse existing tokens and button/input components rather than create a parallel theme. The flow contract would cover first launch, progress, back/skip if permitted by product behavior, completion persistence, returning users, and feature-scoped return destinations if applicable.

I would add a focused scenario to an existing XCUITest target before implementing behavior if such a target exists. Without one, I would preserve exact manual steps instead of adding a testing framework solely for this change. A SwiftUI preview would help iterate on layout but would not be completion evidence for lifecycle or navigation.

**Completion evidence I would provide:** the exact Xcode scheme, build destination, minimum-OS check, and simulator/device screenshots for the steps; a recording or XCUITest result for entry, back, completion, relaunch, and returning-user behavior; Dynamic Type, VoiceOver, keyboard where inputs exist, and reduced-motion checks. Build or preview success alone would leave onboarding runtime behavior unverified.

**Problem exposed by this fixture:** no Node manifest is expected here and is not a blocker. Exact Xcode commands depend on actual project metadata, and onboarding persistence must be integrated with the existing app state rather than invented in a disconnected preview.

## D. Native Android checkout with iOS-only Mobbin references

**User request:** “Improve native Android checkout.”

**Raw fixture:** Kotlin, Jetpack Compose, a Gradle app, and only iOS Mobbin references. The reference screenshots do not supply verified Android interaction behavior. Actual Mobbin URLs, Gradle variant, navigation dependencies, and current source filenames are not included.

**Implementing-agent response and decision trace:**

I will use the iOS references to inform content order and visual hierarchy, while implementing the checkout with the app's Compose theme, Material components where appropriate, existing state holder, and Android navigation. I will not copy iOS back gestures, SF Symbols, or an iOS sheet presentation as if they were Android requirements.

My first commands would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'settings.gradle*' -g 'build.gradle*' -g 'libs.versions.toml' -g '*.kt'
rg -n 'Checkout|NavHost|composable\(|WindowInsets|imePadding|MaterialTheme|SavedStateHandle' --glob '*.kt'
./gradlew tasks --all
```

I would read the provided reference notes/screenshots and retain their actual returned links in the design notes; I would not invent a URL from an app name. If an unanswered Android design decision genuinely needs research, I would discover available Mobbin tools and search for the Android counterpart. The absence of Android Mobbin screens does not block work supported by the existing product and native conventions.

The chosen files would be the current checkout composable and its existing state holder, plus the actual navigation graph only if the flow requires a navigation fix. I would check existing edge-to-edge and IME handling before adding padding to avoid counting an inset twice. Pending, error, and success would stay distinct. For state affected by backgrounding or recreation, I would inspect the real persistence/reconciliation path rather than assume that having a ViewModel solves process death.

After identifying the actual module and variant, I would use its Gradle build and connected-test tasks. I would not assume `:app:connectedDebugAndroidTest` exists merely because this is an Android project.

**Completion evidence I would provide:** Android screenshots and flow recordings, the exact variant/device/API level, keyboard-visible checkout, large fonts, TalkBack, system back and predictive back where supported, and pending-payment restoration. Notes would identify which choices came from iOS visual references and which were Android adaptations or proposed transitions. A screenshot would not be cited as proof of gesture behavior or conversion improvement.

**Problem exposed by this fixture:** reference platform and implementation platform differ. The skill gives a clear mapping boundary, so this does not force either a platform switch or speculative Android gesture claims.

## E. Payment success navigation with receipts and interruptions

**User request:** “Fix the payment success navigation but let users go back to receipts.”

**Raw fixture:** receipt history, a payment form, a pending asynchronous charge, and users who sometimes background the app. There is no running simulator/emulator or test runner. No framework, route structure, transaction API, cancellation capability, or persistence mechanism is specified.

**Implementing-agent response and decision trace:**

I will first identify the actual framework and follow the payment flow from receipt history through the form, request initiation, status resolution, completion route, and app restoration. With the supplied fixture, selecting Expo Router, React Navigation, SwiftUI, or Compose would be guesswork. I can define the business and navigation checks now while resolving the exact stack from source.

My first commands would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'package.json' -g 'project.pbxproj' -g 'build.gradle*' -g '*.swift' -g '*.kt' -g '*.tsx' -g '*.ts'
rg -n -i 'receipt|payment|charge|pending|transaction|appstate|scenephase|onresume|savedstate' --glob '*.{ts,tsx,swift,kt}'
```

Before changing code, I would write the failure scenarios as a small manual verification record: response remains pending; double tap; timeout with unknown server outcome; background/resume during pending; successful server completion while backgrounded; failure and retry; back from success to receipts; revisiting or restoring the old form; keyboard-visible back; and process recreation when supported by the target flow.

The chosen files would be the existing shared payment state/service, its existing lifecycle/persistence boundary, and the relevant navigation owner. The form would change only if its submission affordance is missing the shared state guard. I would inspect all callers before editing the shared payment function.

The intended stack would retain receipt history and unrelated destinations. Once the server confirms success, the completed payment form must no longer submit the same operation. The success/receipt detail can remain a pushed destination with Back returning to history, or the completed form can be replaced/dismissed using the existing stack's suitable operation. I would choose that operation from the actual stack shape, rather than issuing a universal `replace` or resetting all history.

Pending is not success. Back may return to receipts while the request continues, with a visible pending item or the app's established pending status, if that is how the existing product can expose it. Back does not imply cancellation. On resume or restoration, I would reconcile the durable transaction/request identifier against the authoritative status path. A timeout or unknown outcome must not silently enable a second charge. If that status lookup or identity is absent, I would call out the concrete missing contract and avoid presenting navigation changes as a complete recovery fix.

**Completion evidence I would provide:** actual files changed, source-level verification that can be performed, and one repeatable manual scenario covering the listed states. Once source inspection supplies them, the record would include the real application ID, exact build/launch commands, synthetic account/payment setup, entry route, expected screen and transaction state at each step, and capture paths under the existing evidence folder or `work/ui-verification/`. The current fixture lacks the identifiers and commands, so I would not fabricate them here.

No runtime pass is possible under the fixture as supplied. I would complete feasible source implementation and explicitly report that simulator/emulator execution, interrupted-payment reconciliation, and post-success back behavior remain unrun. A compile pass, if a build tool is available, would be described only as a compile pass. If the server contract is also missing, that is a separate behavior blocker requiring resolution before the full recovery flow can be called complete.

**Problem exposed by this fixture:** this is the strongest incomplete-evidence case. The skill supports continuing source work without pretending the UX passed. The raw fixture also omits the stack and transaction contract, so exact navigation APIs and a complete runnable verification script cannot honestly be selected until repository inspection.

## F. “Keep looping” with one keyboard defect

**User request:** “Keep looping on design improvements.”

**Raw fixture:** one current defect where the keyboard overlaps the relevant screen content/control; yesterday's linked design-reference notes; all other implementation criteria pass. Current component filenames, target OS, and runtime inventory are unspecified.

**Implementing-agent response and decision trace:**

I will resolve the keyboard overlap, then rerun the affected checks and stop once the agreed criteria pass without an actionable in-scope defect. I will read yesterday's notes first. Their age alone is not a reason to repeat Mobbin research or replace a design that is already meeting its contract.

My first commands/actions would be:

```sh
git status --short
rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g '*design*' -g '*reference*' -g 'package.json' -g 'project.pbxproj' -g 'build.gradle*'
rg -n 'KeyboardAvoidingView|keyboardVerticalOffset|useSafeAreaInsets|imePadding|WindowInsets|ignoresSafeArea|keyboardLayoutGuide' --glob '*.{ts,tsx,swift,kt}'
```

I would open the relevant notes and current screen code, resolve the actual target platform, and capture the keyboard-visible defect from the real entry point if a runtime is available. The acceptance criterion would be concrete: the focused field and primary action remain reachable when the keyboard is open, content scrolls or reflows as intended, and dismissal restores the normal layout without extra bottom spacing. I would include the app's supported compact viewport and large text setting where they affect this layout.

I would edit the existing screen's keyboard/inset owner, reusing its current mechanism. For example, I would remove duplicate keyboard/safe-area offsets if inspection establishes that as the cause; I would not introduce a new keyboard package without finding a gap in the current one. The actual fix is conditional on measured overlap and source ownership, not a preselected wrapper.

I would then capture the same entry, focus, keyboard, scroll-to-action, and dismissal sequence after the change, inspect the images, and repeat only affected checks. If another in-scope defect appears, I would fix it and verify again. After two passes without improvement, I would change the diagnostic, such as inspecting the parent container's insets and keyboard behavior, or report the specific unavailable runtime/state instead of repeating ineffective edits.

**Completion evidence I would provide:** baseline revision/device/build and exact reproduction steps; before/after captures with the keyboard open and dismissed; assertions or manual expected/actual results for reachability and restored spacing; and remaining unverified targets. If the defect is fixed and the other criteria still pass, I would finish. I would not schedule an automation, claim continuous background work, or keep restyling the screen solely because the wording says “keep looping.”

**Problem exposed by this fixture:** the instruction is open-ended, but the skill gives an evidence-based stopping condition and a non-progress limit. The fixture does not establish runtime availability; if unavailable, the loop stops at the concrete verification blocker after feasible source work, not at an invented visual pass.

## Observed limitations of this forward test

These are implementing-agent decision outputs, not end-to-end execution results. All six cases yielded a feasible next step without changing frameworks or manufacturing runtime evidence. The skill supplied enough routing and recovery guidance to make the choices above. The simulation cannot establish whether a model executing a real repository would discover the correct state owner, choose the correct version-specific API, or capture valid runtime evidence.

The concrete unknowns remain project source paths, installed scripts and versions, native toolchain/device access, and payment sandbox/status contracts. Those are inputs to discover in a real run. The report deliberately does not replace them with fictional successful commands or a numeric pass score.
