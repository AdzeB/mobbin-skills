# Native implementation

Match the existing framework and minimum OS versions. Read only the relevant platform section; a native app does not require an npm project.

## iOS: SwiftUI or UIKit

- In SwiftUI, use existing view/state patterns, semantic colors, system text styles, and platform controls. In UIKit, keep existing controllers/coordinators and Auto Layout. Do not rewrite one framework into the other for visual polish.
- Use the app's navigation model. [NavigationStack](https://developer.apple.com/documentation/swiftui/navigationstack) can represent a SwiftUI hierarchy; UIKit apps may use navigation/tab controllers. Match sheet or full-screen presentation to the task and preserve cancellation.
- Respect safe areas, Dynamic Type, VoiceOver focus and labels, keyboard avoidance, and reduced motion. System symbols and custom brand assets should have consistent weight and meaning.
- On completion, update domain state and appropriate navigation state together. Preserve return destinations for feature-scoped authentication and purchases; keep receipts reachable without permitting resubmission.
- Build with the repository's Xcode scheme/destination. Prefer existing XCUITest coverage for the changed flow. A SwiftUI preview does not verify real keyboard, navigation, or lifecycle behavior.
- Capture simulator screenshots and recordings of relevant interactions. Use Instruments on an appropriate build/device for performance claims; simulator video does not measure production frame pacing.

## Android: Jetpack Compose or Views

- In Compose, reuse the app's theme, state holders, and Material components where appropriate. In a Views app, preserve its established layouts/fragments instead of starting a Compose migration.
- Use existing [navigation](https://developer.android.com/develop/ui/compose/navigation) and saved-state conventions. Model back-stack changes explicitly, retain return destinations, and verify system/predictive back where supported.
- Respect edge-to-edge/window insets, IME insets, font scaling, TalkBack semantics, and accessibility focus. Android interaction/layout conventions take precedence over the surface appearance of an iOS reference.
- Keep pending/error/success distinct through backgrounding and recreation. Verify the relevant restored-state behavior rather than assuming a ViewModel covers process death.
- Build with the project's Gradle wrapper and variant. Use existing Compose UI tests or UI Automator/Espresso flows as applicable; capture emulator screenshots/recordings for inspection.
- Use Android Studio profiling, system traces, or an existing Macrobenchmark for performance work. Measure the same scenario before and after rather than infer responsiveness from code.

## Platform mapping

| Product intent | iOS direction | Android direction |
| --- | --- | --- |
| Top-level destinations | Existing tab structure | Existing navigation bar/rail |
| Drill into an item | Navigation hierarchy | Navigation destination/back stack |
| Short contextual task | Sheet/menu suited to content | Bottom sheet/menu/dialog suited to content |
| Date/time selection | System picker style suited to task | Platform/Material picker suited to task |
| Irreversible action feedback | Visible pending and outcome states | Visible pending and outcome states |

These are starting points, not a demand to restyle a product. Check current [Apple HIG](https://developer.apple.com/design/human-interface-guidelines) and [Android accessibility](https://developer.android.com/develop/ui/compose/accessibility) when an unfamiliar platform behavior matters.
