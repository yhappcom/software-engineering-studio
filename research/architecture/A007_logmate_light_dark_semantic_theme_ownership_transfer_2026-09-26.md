# A007 — LogMate Light/Dark Semantic Theme Ownership Transfer

Status: **PROJECT-SPECIFIC ARCHITECTURE TRANSFER / PRE-IMPLEMENTATION CONTRACT — RUNTIME VALIDATION OPEN**  
Date: 2026-09-26  
Lead: Architecture

## Purpose

Define the engineering boundary for LogMate Light/Dark theming before product code is changed.

This note does **not** choose final color values. Design Studio owns reusable color/visual semantics; LogMate product sources own implementation truth. Architecture owns the question of where theme decisions live, how consumers depend on them, how provider-owned presentation is isolated, and how the refactor is validated without conflating structural change with visual redesign.

## Evidence identity

### Engineering Studio
- repository: `yhappcom/software-engineering-studio`
- inspected main head before this note: `6cc97641c504f47f7003bcf89126be9e95de5f5b`
- evidence date: 2026-09-26

### LogMate product
- repository: `yhappcom/logmate`
- inspected branch: `main`
- exact inspected head: `88d71141963240b559785e5cd49c87afd9a4fb1e`
- declared app version: `1.0.0+1`
- evidence date: 2026-09-26
- production identity: **UNKNOWN**; `main` is not assumed production

Relevant product files inspected:
- `lib/theme/logmate_theme.dart`
- `lib/screens/welcome_screen.dart`
- `lib/auth/logmate_native_auth_buttons.dart`
- `lib/auth/logmate_auth_buttons_web.dart`
- `docs/specs/welcome-mobile-light-visual-spec.md`
- `docs/evidence/welcome-mobile-light-implementation-2026-09-24.md`
- `pubspec.yaml`

### Design Studio
- repository: `yhappcom/design-studio`
- inspected main head: `6b2b13011eb7fc6d6f8c8a797aedc20b99f7302f`
- evidence date: 2026-09-26

Relevant evidence:
- `research/color/C017-controlled-semantic-palette-derivation-token-contract.md`
- `research/color/C020-multisurface-semantic-token-system.md`
- `research/color/C021-concrete-semantic-pair-matrix.md`
- `research/color/C074-logmate-auth-state-render-transfer.md`
- `research/color/C103-logmate-brand-salience-semantic-state-contradiction-audit.md`
- `research/color/C104-logmate-integration-principle-inputs.md`
- `case-studies/logmate/DESIGN_SYNTHESIS_GATE_20260919.md`

## Current product observation

At the inspected LogMate ref, theme ownership is split.

### Global theme owns only part of the decision

`lib/theme/logmate_theme.dart` currently declares:
- brand;
- light surface / on-surface;
- dark surface / on-surface;

and then uses `ColorScheme.fromSeed(...)` for the broader Material color scheme.

This means some product color behavior is produced indirectly by Material seed derivation while other product roles are specified manually elsewhere.

### Welcome owns its own appearance branch

`welcome_screen.dart` independently selects:
- `Colors.white` vs `Colors.black` for the Welcome surface;
- explicit Light/Dark wordmark colors;
- explicit Light/Dark subtitle colors.

The screen therefore knows concrete theme values and theme-mode branching that could otherwise be owned by a theme boundary.

### Auth components own additional appearance rules

`logmate_native_auth_buttons.dart` independently owns:
- Light/Dark resting border values;
- Light/Dark focused border values;
- inherited foreground behavior for the Apple symbol;
- a LogMate-owned Email mark whose painter hard-codes `#20201E`.

The hard-coded Email mark is not theme-aware, which directly explains why it can disappear against the current black Dark surface.

The PWA Google control is provider-rendered through the Google web renderer and is therefore a separate external presentation boundary rather than an ordinary LogMate-owned color consumer.

## Problem classification

This is not merely a one-screen color defect.

The current structure duplicates or disperses knowledge of the same volatile decision:

> how a semantic visual role resolves under Light vs Dark appearance.

A001 treats duplicated knowledge of a changeable decision as a change-propagation risk when multiple consumers must understand the representation. A002 similarly requires an authority for semantic state/policy and distinguishes authoritative ownership from projections/adapters.

The relevant risk is not "many files changed." A005 natural LogMate evolution evidence already rejects that shortcut. The risk is **independently editable semantic ownership**: Theme, Welcome and Auth can disagree about what `surface`, `primary text`, `secondary text`, `boundary`, `focus` or `owned icon` mean in Dark mode.

## Design Studio input

Design Studio provides a stronger semantic contract than the current product implementation.

C017 states:
- primitive values may change;
- semantic names should be the stable implementation interface;
- Light and Dark preserve role identity rather than numeric identity;
- components should consume semantic tokens rather than palette-step names.

C020 defines the graph:

`meaning → semantic role → interaction state → theme mode → output/gamut mapping → surface instance`

and explicitly states that Light and Dark are separately authored mappings from the same semantic roles, not RGB inversions.

C103/C104 further constrain LogMate:
- brand/accent is not semantic authority;
- focus, selection, warning/error/recovery and success must remain distinct roles;
- restrained visual character must not reduce functional state salience;
- Light/Night consistency is relational, not literal;
- environmental/night claims require real environmental evidence.

Engineering therefore has enough design input to define the ownership boundary, but **not** enough authority to select final production color values.

## Architecture alternatives

### Alternative A — keep screen-local Light/Dark branches

Example structure:

`Welcome → if dark use X`  
`Auth → if dark use Y`  
`Home → if dark use Z`

**Rejected as the default architecture.**

Reason:
- each screen/component learns theme representation;
- one visual-role change propagates through multiple consumers;
- partial migration can leave semantically equivalent roles inconsistent;
- testing must rediscover the same rule in multiple places.

Local exceptions remain valid only when the role itself is genuinely surface-specific.

### Alternative B — use Material `ColorScheme` alone as the complete product contract

**Insufficient by itself.**

Material roles are useful for framework integration, but LogMate has product semantics that do not map cleanly to a single generic field:
- identity/wordmark prominence;
- operational secondary text;
- provider-adjacent shell roles;
- selected/current/focus distinctions;
- known failure vs ambiguous outcome;
- offline/stale/conflict;
- future data-visualization namespaces.

Forcing unrelated meanings into one Material field would replace duplicated hex values with semantic collisions.

### Alternative C — shared semantic core plus screen-scoped appearance profiles/adapters

**Recommended architecture, refined by owner direction on 2026-09-26.**

Model:

`screen-by-screen Light/Dark design → repeated semantic roles promoted to shared core → screen profile/role aliases → component/surface consumer`

This deliberately separates **design/review granularity** from **implementation ownership**.

- The owner reviews and approves each screen's Light/Dark pair independently.
- A screen may retain a scoped role when its hierarchy is genuinely surface-specific.
- A role is promoted into the shared semantic core only when repeated evidence shows the same meaning should behave consistently across screens.
- Material `ColorScheme` remains an adapter/projection for Material-owned controls, not a competing semantic authority.
- Provider-owned controls/assets remain an external adapter boundary.

This avoids both extremes:
1. one global palette that forces every screen into the same visual hierarchy;
2. unrelated per-screen hard-coded colors that duplicate semantic meaning without a shared owner.

## Recommended ownership contract

### 1. Semantic roles are the product-facing interface

Consumers should request meanings such as:
- surface base / raised / sunken;
- text primary / secondary / disabled;
- boundary default / strong;
- action primary;
- focus indicator;
- selection indicator;
- success / warning / critical / unknown / offline / conflict;
- LogMate-owned icon primary / secondary where justified.

Consumers should not normally request:
- `darkWhite`;
- `lightGray700`;
- `welcomeDarkText`;
- arbitrary palette-step names.

### 2. Light and Dark are separate mappings of the same roles

The semantic role set remains stable while concrete values may differ by appearance.

Dark is therefore not implemented as:
- RGB inversion;
- opacity applied to Light values;
- a global black background plus near-white foreground;
- per-screen conditional literals.

### 3. Shared semantic core with screen-scoped ownership

The final Flutter mechanism may be a strongly typed Theme extension or equivalent theme-owned object. The mechanism is secondary to the contract.

The architecture has two levels of ownership:

1. **shared semantic core** — meanings that have proven cross-screen invariance, such as ordinary primary/secondary text, focus, error, selection or shared surfaces where the same semantics truly apply;
2. **screen/component-scoped roles** — meanings whose visual hierarchy is intentionally local to a surface, such as Welcome identity prominence or dense-ledger comparison hierarchy.

A screen is allowed to own a scoped role. It is **not** allowed to own an arbitrary Light/Dark literal for a meaning that already has a shared semantic owner.

Promotion rule:

`screen-specific role → repeated same meaning across screens → promote to shared semantic core`

Do not add extra palette/alias layers unless they hide a real independently changing decision. A001's counterexample remains controlling: abstraction must earn its carrying cost.

A private primitive palette may exist as implementation support, but primitive names are not the component API.

### 4. Component aliases require a real semantic reason

A component-specific alias is justified when:
- it is reused;
- it owns a stable component meaning not represented by a generic semantic role;
- it may evolve independently without changing the role beneath it.

A page name alone is not sufficient reason.

Prefer:
- `auth.shell.border` if Auth genuinely has a reusable shell contract;

over:
- `welcomeDarkBorder`.

### 5. Material theme is an adapter

Material widgets may continue to consume `ThemeData.colorScheme`, but those values should be intentionally mapped from the same LogMate semantic system where product semantics overlap.

Avoid two authorities:
- LogMate semantic token says one thing;
- `ColorScheme.fromSeed` independently derives another;
- components then receive conflicting hierarchy.

Seed generation may remain only where its output is explicitly accepted as implementation detail and cannot redefine product semantic roles.

## Provider boundary

Systems S007 remains controlling for provider-owned presentation.

### LogMate-owned presentation
Safe candidates for semantic-theme ownership include:
- Email icon;
- LogMate-owned labels;
- shared shell background/border where provider rules permit;
- focus geometry/color owned by LogMate;
- surrounding layout.

### Provider/platform-owned presentation
Do not treat the following as ordinary recolorable product tokens without provider/platform authority:
- Google provider-rendered web control/artwork;
- provider-owned Google artwork;
- Apple provider/system presentation where external rules govern it.

Current LogMate product evidence records a deliberate shared Flutter peer shell and platform Apple symbol, while provider-brand review remains OPEN. Therefore this architecture note does **not** authorize arbitrary Apple recoloring.

The provider adapter must expose enough surrounding integration for visual coherence without making LogMate theme values the authority over provider-owned artwork.

## Refactoring boundary

A005 requires observer-scoped behavior preservation. Therefore architecture migration and visual retuning should be separated.

### Phase 0 — inventory
Before implementation:
- inventory direct color literals, `Colors.*`, brightness branches and seed-derived dependencies in relevant LogMate UI;
- classify each use as semantic product role, decorative implementation detail, provider-owned presentation or intentionally local exception;
- do not mechanically replace every literal with a token.

This exhaustive inventory has **not** been completed in this study.

### Phase 1 — introduce semantic ownership without intentional visual change

Create the semantic theme boundary and map the **current accepted Light/Dark values** into it.

Goal:
- ownership changes;
- visible behavior should remain stable for the observer set.

This is the cleanest point to test whether the refactor itself caused regressions.

### Phase 2 — migrate Welcome/Auth as the first transfer surface

Move LogMate-owned Welcome/Auth decisions to semantic ownership:
- surface;
- wordmark/secondary identity roles if retained as distinct semantics;
- button label/boundary/focus roles;
- Email icon.

Keep provider-controlled presentation isolated.

Existing Mobile Light evidence becomes a regression baseline. Add Dark evidence before visually retuning it.

### Phase 3 — apply Design Studio Dark corrections deliberately

Only after structural migration passes:
- change the Dark role values according to the Design Studio review;
- update Dark visual expectations as an explicit product/design change;
- preserve Light unless Design Studio/product intentionally changes it.

This separates:
1. architecture/refactor defect,
from
2. intentional visual change.

### Phase 4 — migrate remaining surfaces incrementally

Move Home, onboarding/auth forms, Add Flight, Activity, View Logbook/import/configuration surfaces as their semantic roles are audited.

Do not create one huge token-replacement diff unless the inventory proves that risk is lower than staged migration.

## Screen-by-screen design and approval contract

Owner direction on 2026-09-26 establishes the preferred UI workflow:

`screen Light → screen Dark → render/review → approve → next screen`

The shared semantic system is therefore **not** a prerequisite that must be visually finalized for the whole application before individual screens can be designed.

For each screen:
- author and review Light/Dark as a pair;
- preserve the screen's own information hierarchy;
- classify each visual role as shared, screen-scoped, provider-owned or state-specific;
- promote only repeated semantics into the shared core;
- keep screen-specific optical roles local when global promotion would make unrelated screens move together.

This is especially relevant because LogMate currently has a bounded set of primary product screens. The lower screen count makes direct screen-by-screen optical review practical and reduces the need for premature global abstraction.

The implementation still avoids raw screen-local Light/Dark literals where a semantic role can own the decision.

## User-adjustable Dark text luminance

### Owner direction

Prepare a fine-grained user control for **Dark-mode text brightness/luminance** after onboarding.

Scope:
- **excluded:** signed-out Welcome and Initial Logbook Onboarding;
- **eligible:** post-onboarding application surfaces, including Settings and ordinary operational screens;
- the control has no effect in Light mode;
- Welcome and onboarding always use their approved fixed Standard appearance, even if a saved user preference exists.

The setting should be exposed from the existing Settings surface under an Appearance section when implementation begins.

### Interaction model

Preferred control:
- continuous slider rather than only three presets;
- internal normalized value may be represented as `0...1` or `0...100`;
- UI does not need to expose a numeric percentage unless later usability evidence supports it;
- provide an explicit reset-to-Standard action.

The slider does **not** control device display brightness. It controls LogMate-authored Dark-theme text luminance within a bounded authored range.

### Semantic application

Do not apply one scalar directly to every foreground RGB value.

The adjustment function should resolve per semantic role, for example:

`user intensity → role-specific bounded luminance mapping → text.primary / text.secondary / text.tertiary / owned-icon roles`

Each role may have:
- its own minimum;
- Standard/default value;
- maximum;
- response curve/sensitivity.

This preserves hierarchy while allowing fine adjustment.

### Roles excluded from generic text-luminance scaling

Do not automatically scale:
- error / critical / warning / success state colors;
- focus indicator;
- selection/current-context state;
- disabled semantics where contrast/state distinction would be corrupted;
- provider-owned Apple/Google artwork or provider-rendered controls;
- any role whose independent semantic contrast contract would be broken.

A screen-scoped identity role such as a wordmark may react partially, fully or not at all, but that behavior must be explicitly authored rather than inherited accidentally.

### Safety clamp

The user control must be bounded by the authored role contract.

At both slider extremes:
- required text remains legible;
- primary/secondary/tertiary ordering remains intact;
- operational values are not demoted below their labels when the screen contract requires the opposite;
- state colors remain independently recognizable;
- non-color state cues remain intact.

The slider therefore adjusts **within** the approved Dark system; it does not let the user redesign the palette.

### Persistence and scope

Engineering recommendation:
- store this as a **device-local appearance preference**, not canonical logbook/account data;
- preserve the value across restarts;
- retain it while Light mode is active but do not apply it until Dark mode becomes active;
- do not sync it across devices by default, because perceived luminance needs can differ materially by phone/tablet/display/environment.

This persistence decision must be canonicalized in the LogMate product repository before implementation. It is not a data-ledger or flight-record preference.

### Runtime update

When the slider moves:
- eligible currently visible surfaces should update without app restart;
- Theme resolution should recompute semantic text roles from Standard Dark + user luminance preference;
- screens must not manually read the raw slider value and calculate their own colors;
- Welcome/onboarding must bypass this user layer and resolve fixed Standard mappings.

### Validation matrix

At minimum validate:
- Standard Dark;
- lower supported bound;
- upper supported bound;
- one or more intermediate values;
- Settings live update;
- navigation between eligible screens retains the same preference;
- app restart retains the preference;
- system Light → Dark transition applies the saved preference;
- Dark → Light ignores it without deleting it;
- sign-out / Welcome ignores it;
- Initial Onboarding ignores it;
- 200% text and constrained-height layouts remain unaffected geometrically;
- semantic focus/error/selection states do not drift with the text slider.

Physical-device and low-light evaluation remain necessary before any cockpit/night-readability claim.

## Validation contract

### Claim A — refactor preserves accepted Light behavior
- **SPEC/PROPERTY:** current LogMate Light visual/product contract.
- **TARGET:** exact post-refactor LogMate ref.
- **ORACLE:** existing Light Flutter goldens + behavioral tests + targeted owner review where optical judgment is required.
- **FAILURE MODEL:** semantic-theme migration changes surface/text/boundary/focus appearance or action behavior unintentionally.

### Claim B — Dark roles resolve through one authority
- **SPEC/PROPERTY:** semantic role → theme-mode mapping contract.
- **ORACLE:** component/theme tests that resolve representative roles in Light and Dark plus rendered Dark fixtures.
- **FAILURE MODEL:** screen-local literal/branch bypasses the authoritative mapping or semantically equivalent components resolve incompatible values.

### Claim C — functional states remain distinct
Test at least:
- ordinary;
- focus;
- disabled;
- pending;
- error/known failure where applicable;
- ambiguous/unknown where applicable.

Color must not be the sole oracle for semantic state.

### Claim D — provider constraints survive migration
- Google/Apple provider-owned rendering/assets are not distorted/recolored outside approved constraints;
- Email remains visually coherent while staying LogMate-owned;
- provider action mapping and Auth semantics remain unchanged.

### Target/runtime evidence

Host Flutter goldens are bounded evidence only. Preserve target identity for:
- Android;
- iOS/iPadOS;
- PWA/browser engine where applicable;
- 200% text / constrained geometry;
- forced-colors/high-contrast where supported;
- physical-device/night/glare only when those claims are actually made.

## Regression/golden policy

Do not overwrite existing Light goldens merely because theme architecture changes.

For the structural migration:
- existing Light baseline should remain unchanged unless an intentional Light design decision is recorded;
- establish Dark goldens/fixtures for the current appearance before intentional Dark retuning where practical;
- intentional Dark design changes require explicit expected-output revision, not blind golden regeneration.

A green golden test proves only agreement with its stored oracle. Q001 remains controlling: the stored image must itself be traceable to the accepted product/design expectation.

## Rollback/recovery

This change has no persisted user-data migration by itself.

Rollback boundary:
- preserve a clean commit before semantic-theme migration;
- keep structural migration and intentional Dark visual retuning in separate commits/PR stages where practical;
- if runtime/render regression appears, revert the structural or visual stage independently.

No backup/schema/data rollback contract is required for this theming refactor unless implementation unexpectedly changes persisted preferences or settings.

## RELATED DOMAIN CHECK

### Foundations
F001 confirms target/runtime identity matters. Host/Chrome/Safari evidence does not silently transfer to native/mobile/product execution.

### Architecture
- A001: hide volatile theme representation behind one semantic owner; avoid abstraction without real change-pressure benefit.
- A002: distinguish semantic authority from projections/adapters.
- A003: semantic role names become a contract and should evolve compatibly.
- A005: preserve observer-visible behavior during structural refactoring; coordinated spec/test/implementation edits are not themselves harmful coupling.
- A006: keep product decision state separate from implementation/evidence state.

### Mobile
M001/M006 confirm Flutter/platform/browser normalization does not erase target-specific rendering evidence. Exact product native/PWA transfer remains required.

### Data
Not materially involved. No persisted schema or user-data migration is implied by this architecture change.

### Quality
Q001 requires explicit claims and valid oracles. Existing Light goldens are useful only within their known specification/evidence boundary. Dark fixtures and provider-state tests need independent acceptance rules rather than "test is green."

### Systems
S007 provider presentation authority is a hard boundary. Auth UI refactoring must not redefine provider identity/session semantics or provider-owned branding constraints.

### Design Studio
Design Studio owns semantic Color hierarchy and final appearance values. C017/C020/C103/C104 directly support role-based Light/Dark mapping and reject literal cross-theme reuse. Engineering owns the executable ownership boundary and validation.

### Web Manager
Not materially decision-changing for the theme ownership boundary. PWA browser/forced-color integration remains a later runtime transfer concern.

### Marketing Manager
Not materially relevant.

### Product
Current LogMate implementation at `88d7114...` demonstrates dispersed theme ownership and the concrete Email Dark-mark failure mechanism. No product files were changed in this study.

## HANDOFFS

### Design Studio
Engineering accepts the semantic-role model and separate Light/Dark mappings. Design Studio should return:
- final product semantic role inventory needed for the first migration;
- approved Light mapping if current Light must be preserved exactly;
- candidate Dark values for Welcome/Auth after the structural migration;
- whether wordmark/provider-adjacent marks require distinct roles or can use existing primary/secondary roles;
- unresolved human/device/night evidence explicitly marked OPEN.

### LogMate / Codex
Do not begin by changing Dark hex values across screens.

Implementation order:
1. inventory;
2. establish the shared semantic core plus screen-scoped role mechanism;
3. preserve Welcome/Initial Onboarding as fixed Standard appearance surfaces;
4. migrate and approve screens Light/Dark one at a time;
5. promote only repeated semantics into the shared core;
6. add the device-local Dark text-luminance preference and Settings slider for post-onboarding surfaces;
7. run Standard/min/max/intermediate regression evidence;
8. continue remaining screens incrementally.

Do not rewrite Auth behavior or provider flow as part of the theme refactor. Do not let eligible screens consume the raw slider value directly; they consume resolved semantic roles.

### Quality
Define structural and visual regression oracles separately. Preserve existing Light evidence, add Dark/state evidence, and reject blind golden regeneration.

### Mobile / Systems
Return any platform/provider constraint that prevents the shared semantic shell from rendering as designed. Do not silently approximate provider behavior.

## OPEN / CHANGE WATCH

- Exhaustive LogMate hard-coded color/theme inventory is not yet complete.
- The owner-directed screen-by-screen design workflow and post-onboarding Dark text-luminance control still require canonical LogMate product-spec synchronization before code implementation.
- Exact slider range, role-specific response curves and minimum/maximum luminance values remain Design/Product-owned and OPEN until rendered validation.
- Device-local persistence mechanism for the appearance preference is not yet implemented.
- Final LogMate production Light/Dark palette is not selected by Engineering Studio.
- Whether a dedicated Flutter Theme extension is the final implementation mechanism remains a product implementation decision; the semantic ownership contract is independent of that choice.
- Apple provider-brand compliance for the current shared-shell/platform-symbol presentation remains OPEN in product evidence.
- Physical-device, calibrated-display, cockpit/night/glare and representative-pilot validation remain OPEN.
- Forced-colors and independent-browser transfer remain OPEN where relevant.
- Default branch is not production identity.

## Decision

**ENGINEERING RECOMMENDATION: ACCEPT THE SEMANTIC-THEME OWNERSHIP DIRECTION BEFORE CODE MODIFICATION.**

Promote the following as the pre-implementation architecture contract:

1. screen-by-screen Light/Dark design and owner approval is the visual workflow;
2. repeated semantics are promoted into a shared LogMate semantic core; genuine screen-specific roles may remain scoped;
3. Light/Dark mappings are separately authored rather than inverted;
4. Material `ColorScheme` is an adapter/projection, not competing product authority;
5. provider-owned presentation is isolated from LogMate-owned color tokens;
6. structural refactor is separated from intentional visual retuning;
7. Welcome and Initial Onboarding remain fixed Standard appearance surfaces;
8. post-onboarding Dark surfaces support a bounded fine-grained user text-luminance adjustment;
9. the adjustment operates through semantic-role resolution, never arbitrary per-screen color math;
10. existing Light regression is preserved; Dark Standard/min/max/state evidence is added;
11. remaining product surfaces are migrated and approved incrementally.

This is an architecture/project advisory result, not runtime PASS and not a final Color palette decision.
