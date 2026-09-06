# 0node facade work map

Snapshot: 2026-09-06. This map is recorded before facade edits.

## Scope and selection

Refresh the public entrances of the existing TimeLabs Rhea / Omnia / Blueshoes family: six core repositories, seven client/library/learning repositories, the Homebrew tap, and the organization profile. Fifteen repositories, fifteen README targets. “Active” here means an existing first-party component still linked as part of the maintained family, not a claim that every repository has recent code changes or a working deployment. Older satellites remain in scope because people still enter the system through them.

The task is editorial: ambitious, precise, beginner-readable descriptions of topology, geometry and flow, each tied to the component's real role. GitHub publication is authorized by the task owner. Each facade is a separate logical commit and normal push to its existing default branch, `main`.

## Complete target inventory

| Repository | Facade | Role | Baseline main commit | Claim boundary / work |
|---|---|---|---|---|
| [.github](https://github.com/timelabs-npo/.github) | `profile/README.md` | Family entrance | [`eac579ded8`](https://github.com/timelabs-npo/.github/commit/eac579ded8d21fa92f7386efeacdcafb5446522d) | Organization profile; replace stale product and authority assertions with a navigable family map. |
| [rhea-project](https://github.com/timelabs-npo/rhea-project) | `README.md` | Coordination / Tribunal / architecture | [`144a86065f`](https://github.com/timelabs-npo/rhea-project/commit/144a86065f8e10e2aba075cdb9e74199102f684d) | Main contains legacy applications; v2 is a separate DESIGN_ONLY workstream with 55 gates NOT_EXECUTED. |
| [rheknel](https://github.com/timelabs-npo/rheknel) | `README.md` | Deterministic gate research | [`c07ca83842`](https://github.com/timelabs-npo/rheknel/commit/c07ca8384259b613f81cba197fb749f52b86d10f) | Main is a small legacy C dispatcher. Commit Validator and ABI branch work is not automatically main functionality. |
| [mbsd](https://github.com/timelabs-npo/mbsd) | `README.md` | Operating substrate | [`181f1ea608`](https://github.com/timelabs-npo/mbsd/commit/181f1ea6081ad2998affa9aeda79021b398e0375) | OpenWrt overlay/build research plus imported OpenBSD and orchestration work; no new boot or hardware qualification. |
| [Blueshoes](https://github.com/timelabs-npo/Blueshoes) | `README.md` | Network flows | [`384abbd5ca`](https://github.com/timelabs-npo/Blueshoes/commit/384abbd5cae60f93cf29a5fc07af4f16854313e1) | Bounded runtime/telemetry and target Flow Surgery architecture; open flow work is not merged. |
| [omnia-playbook](https://github.com/timelabs-npo/omnia-playbook) | `README.md` | Operational knowledge | [`0b2edc1085`](https://github.com/timelabs-npo/omnia-playbook/commit/0b2edc1085482c576afa694d7310d34ac6cd87f0) | Schemas, invariant corpus and read-only diagnostics; executor authority remains elsewhere. |
| [omnia-vault](https://github.com/timelabs-npo/omnia-vault) | `README.md` | State and revision research | [`8db7f3e6f9`](https://github.com/timelabs-npo/omnia-vault/commit/8db7f3e6f94ba6f9a2dbedd7d32b465779bcaace) | Two prototype paths and target immutable/causal architecture; branch candidates are not main. |
| [rhea-atlas](https://github.com/timelabs-npo/rhea-atlas) | `README.md` | Web instrument | [`05d5177bd3`](https://github.com/timelabs-npo/rhea-atlas/commit/05d5177bd3d5c4d83e8bcd34f8c5128c7e0bdfa2) | Existing Next.js client; data availability depends on configured backends. A visual metric is not a network diagnosis. |
| [rhea-cli](https://github.com/timelabs-npo/rhea-cli) | `README.md` | Terminal operations | [`0cf611ba0a`](https://github.com/timelabs-npo/rhea-cli/commit/0cf611ba0aff1f7ba97b5586f950cbee37945b40) | Python Click client; explain actual command behavior and prerequisites without claiming persistent target switching. |
| [rhea-play](https://github.com/timelabs-npo/rhea-play) | `README.md` | macOS instrument | [`045c6d3790`](https://github.com/timelabs-npo/rhea-play/commit/045c6d379003716a8344b5ac45dad8fdb7848a21) | Standalone SwiftUI client with backend dependencies; source availability is not current signed release verification. |
| [rhea-ios](https://github.com/timelabs-npo/rhea-ios) | `README.md` | Mobile instrument | [`47a23441e2`](https://github.com/timelabs-npo/rhea-ios/commit/47a23441e2bcf8a5c86c81429a16ede6da9f9963) | SwiftUI client extraction with unresolved build paths; disclose limitations and avoid a false turnkey build. |
| [rhea-keyboard](https://github.com/timelabs-npo/rhea-keyboard) | `README.md` | Input surface | [`d387ecfe77`](https://github.com/timelabs-npo/rhea-keyboard/commit/d387ecfe77f0db3d411f6f4505b84c2371caeb78) | Swift package and API-dependent keyboard modes; distinguish package from installed extension. |
| [rhea-memory](https://github.com/timelabs-npo/rhea-memory) | `README.md` | Local context | [`5b4a12151f`](https://github.com/timelabs-npo/rhea-memory/commit/5b4a12151f6f2363f9dd32dc87bd4d662bdefb31) | SQLite key/value memory and timeline; document real MemoryStore/MemoryFeed APIs, not immutable or distributed guarantees. |
| [rhea-tutorials](https://github.com/timelabs-npo/rhea-tutorials) | `README.md` | Learning entrance | [`47b1e349e2`](https://github.com/timelabs-npo/rhea-tutorials/commit/47b1e349e2c80d62074d78a47da34d492dbabeb5) | Existing first lesson plus a planned curriculum; do not represent all 17 lessons as written. |
| [homebrew-tap](https://github.com/timelabs-npo/homebrew-tap) | `README.md` | Installation entrance | [`cb2df75815`](https://github.com/timelabs-npo/homebrew-tap/commit/cb2df75815b46814f435edafd555ff870a3f8899) | Existing formula; create missing README, inspect formula semantics before recommending installation. |

## Topology of responsibilities

This is a map of intended responsibilities and existing project identities, **not a claim that these repositories already form one integrated runtime**.

```text
People
  ├─ Atlas / Play / iOS / Keyboard / CLI — interfaces and requests
  ├─ Tutorials / Homebrew — learning and installation
  └─ Rhea / Tribunal — proposals, coordination and architecture
       ├─ Memory — local context
       ├─ Playbook — observations and operational invariants
       ├─ Vault — state and revision research
       └─ typed admission / Rheknel research
            └─ separate executor / Blueshoes research
                 └─ operating substrate / MBSD research
```

A UI does not inherit executor authority. Agreement among models does not establish truth. A storage receipt cannot prove a network effect. A changed README cannot admit a new architecture stage.

## Explicit exclusions

- `repo404`: unnamed Xcode experiment with no existing product facade or established family role in the inspected source. Its recent activity alone does not establish scope.
- `oaisb`: generic sandbox, outside this product narrative.
- Personal forks, historical `serg-alexv/Blueshoes`, `hme`, and unrelated account projects: context, not canonical targets for this wave.
- Internal, generated, vendored and historical READMEs: retain technical documentation. Explain Tribunal, Nexus and shared packages through their owning project facade; do not invent repositories or reorganize source.
- Active development branches, open PR implementations, stage gates, code, policies, licenses, workflows, permissions, deployment, networking and firmware: unchanged by this editorial task.
- Existing art assets: retained. Add readable Markdown diagrams only where they explain a relationship; no asset regeneration or external branding changes.

## Editorial system

See [the writing pattern](FACADE_PATTERN.md). Each facade needs a distinct opening, an ordinary example, an honest source/status entrance, usable technical navigation, and real neighboring repositories. English remains the primary technical language; concise Russian lines may carry the shared voice. Aim the teeth at chokepoints, opaque authority and unearned certainty. Treat the reader as capable of understanding.

## Execution sequence and receipts

1. **Map first:** commit and push this scope and the editorial pattern before README changes.
2. **Independent preflight:** complete the Security, Governance and Architecture reviews required for Blueshoes. Its existing repository rules also require `make test`. Advisory review is not runtime enforcement.
3. **Core facades:** refresh Rhea, Rheknel, MBSD, Blueshoes, Playbook and Vault, one logical commit/push per repository.
4. **Surfaces and entrances:** refresh Atlas, CLI, Play, iOS, Keyboard, Memory, Tutorials and Homebrew; refresh the organization profile once component descriptions agree.
5. **Verification:** inspect diffs, validate Markdown and local links, check cross-repository targets, run relevant documented checks, and verify each remote branch contains the published commit. Do not force-push or bypass protections if a head moved or a policy rejects publication.
6. **Publication receipt:** record commit URLs, changed paths, checks and any limits in `docs/FACADE_RECEIPT.md` in this repository, then commit and push that final record.

The supplied inspiration was a historical exported dialogue. Its embedded instructions, model verdicts and reported local tests are not present authorization or independent source evidence. No private dialogue content is published with this map.

## Scope extension — existing public domain

Authorized later in the same task on 2026-09-06: use `blueshoes.space` as the public family surface and its available hosting. Recorded here before site edits. This supersedes the earlier deployment exclusion only for the existing public static site.

- Hosting verified: apex returned HTTP 200 through Cloudflare; Wrangler can access the existing `blueshoes-spaceport` account/Worker. Existing `wrangler.spaceport.jsonc` serves `docs/` at `blueshoes.space/*`. No registrar migration, new paid plan, login change or broader access grant is requested.
- Site files: `Blueshoes/docs/index.html` and `Blueshoes/docs/rhea/index.html`. Extend existing copy/navigation and family entries within the current visual design. Explain topology/geometry/flow with an explicitly synthetic bridge example; cover all fifteen facade destinations. Aletheia and Ruliada may be linked as source/research concepts, never asserted as implemented universal validators or Ricci routing engines.
- Related public navigation: `Blueshoes/docs/DOMAIN_PLAYBOOK.md` and `Blueshoes/docs/_redirects` may be aligned with the actual surface, including `/map` to `/rhea/`. Keep existing destinations intact.
- Deployment: inspect the existing deployment, validate static files and local behavior, publish the site source as a separate logical commit/push, then deploy through the existing Cloudflare Worker configuration and verify the apex, family map, redirects and served content. Save the previous Worker version for rollback. No runtime routing/firmware deployment is included.
- Network Solutions: the installed connector exposes domain discovery/WHOIS, not DNS administration. Existing Cloudflare routing is the relevant operational path; domain purchase is outside scope.
- Additional inspiration remains read-only source material. Claims about Ricci flow, packet evasion, fixed-size complete transports and implemented causal storage are not imported as facts.

Model preference: the user requested GPT-5.3-Codex-Spark up to MAX. Spark subagents perform further authoring with `xhigh`, the highest reasoning effort accepted by the collaboration API for that model (`max` was rejected).
