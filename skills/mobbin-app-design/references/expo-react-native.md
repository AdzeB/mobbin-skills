# Expo and bare React Native

Use the project's installed versions and scripts. Consult matching official documentation before choosing APIs; the examples below identify responsibilities, not mandatory dependencies.

## Expo

- Confirm Expo SDK, router/navigation package, app configuration, and whether native projects are generated or maintained manually. Preserve existing edits and the package manager/lockfile.
- Expo Go can verify supported JavaScript/UI behavior. Use an existing development build when custom native modules, native configuration, or unavailable Expo Go capabilities matter. [Development builds](https://docs.expo.dev/develop/development-builds/introduction/) have a different capability set from Expo Go.
- Start with the existing development command. Use `npx expo install` for a required compatible Expo package, not arbitrary latest versions. Do not add packages simply because a reference uses a similar control.
- Do not run destructive prebuild regeneration over hand-maintained native projects. Native configuration changes may require rebuilding the development client. Do not trigger a paid cloud build or release beyond the user's authorization.
- With [Expo Router](https://docs.expo.dev/router/introduction/), keep route groups/layout ownership and the existing stack semantics. Choose push, dismiss, replace, or guards based on the required history. Check APIs against the installed version; a replace is not a universal stack reset.

## Bare React Native

- Keep the repository's native projects, navigator, build scripts, and platform integration. No Expo migration is necessary for Mobbin research or native-quality UI.
- Use installed native wrappers first and confirm support on every target OS. If new native code is required, account for iOS/Android integration and rebuild requirements.
- Use `Platform` or platform-specific files when behavior differs. Expo-only environment variables or modules are not portable React Native assumptions.

## Shared implementation details

- Use the established safe-area, keyboard, sheet, form, data, and theme solutions. Check bottom CTAs with keyboard visible; avoid counting insets twice.
- Use supported native controls and accessible wrappers. Avoid applying iOS-only presentation, shadows, or icons to Android without a deliberate platform mapping.
- Virtualize long lists with the existing list component and stable keys. A small settings list does not automatically need FlashList. Profile before replacing a working list implementation.
- Keep form state correctness: controlled inputs are valid. Replacing them with refs requires evidence and must preserve validation, reset, hydration, and accessibility behavior.
- Reuse the app's animation system. If using Reanimated, consult the installed version for worklet/shared-value APIs and threading; do not paste version-specific snippets unverified.
- Treat simulator/emulator functional checks separately from release-build performance measurements. Expo Go performance is not a release-device benchmark.

Use the project's existing E2E runner, such as Maestro or Detox, when available. Preserve a repeatable interaction script and screenshots of the changed states. See [React Native testing](https://reactnative.dev/docs/testing-overview) and [React Navigation](https://reactnavigation.org/docs/getting-started) for the installed stack.
