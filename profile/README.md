<div align="center">

# timelabs

**No single model should be the final authority on truth.**

---

</div>

We are a non-profit building open infrastructure for **consensus-driven verification** — tools that force AI models to disagree, debate, and prove claims before anyone acts on them.

### Why this exists

Modern AI gives confident answers. Confidence is not correctness. A single model will tell you a drug candidate passes Lipinski's Rule of Five — but won't mention the 40% of approved drugs that violate it. We think the scientific method deserves better than autocomplete.

**Our position:**
- Truth is not a probability score from one model. It's what survives adversarial debate across many.
- Infrastructure that verifies claims should be free, auditable, and owned by no one.
- 5% of every payment funds carbon-neutral compute, open-science grants, and animal welfare.
- The humans who use our tools are not "users." They are researchers, builders, and skeptics.

### Theoretical basis

Our verification framework stands on two pillars:

**Stephen Wolfram's Ruliad** — the entangled limit of all possible computations. We implement the idea that truth emerges not from any single computational path, but from the convergence of many. When 3-5 models independently reach the same conclusion through different reasoning chains, that's a signal. When they diverge, that's a more important signal.

**DeepMind's adversarial verification** — debate as an alignment protocol. Instead of asking "is this correct?", we ask "can this survive attack?" Every claim passes through a dedicated sceptic whose only job is destruction. What survives is stronger than what was merely generated.

The synthesis: **gradient → flux → constraint** replaces "prompt → response" as the primitive. Claims flow through an adversarial field. Constraints (evidence, logic, cross-model agreement) shape what emerges. The Ruliad provides the space; adversarial debate provides the selection pressure.

### What we maintain

<table>
<tr>
<td width="50%">

**[rhea-project](https://github.com/timelabs-npo/rhea-project)** — Core tribunal API, Aletheia proof chain, multi-provider bridge. FastAPI backend serving every surface. The backbone.

**[rhea-memory](https://github.com/timelabs-npo/rhea-memory)** — Persistent memory for AI agents. SQLite KV + timeline + compact context. `pip install rhea-memory`.

**[rhea-tutorials](https://github.com/timelabs-npo/rhea-tutorials)** — Build this entire system from scratch. 17 lessons: from "ask 3 models a question" to "deploy to cloud and switch between desktop, CLI, and phone."

</td>
<td width="50%">

**[rhea-play](https://github.com/timelabs-npo/rhea-play)** — Native macOS operations centre. 12 panes in one window: live radio feed, interactive tribunal, governor metrics, task queue, Aletheia proof browser, Ruliad ontology explorer, NDI video, and process monitor. Built for people who run AI systems, not just use them.

**[rhea-ios](https://github.com/timelabs-npo/rhea-ios)** — iOS tribunal client. 8 tabs, Keychain auth, same API. Start a tribunal on your phone, review proofs on your Mac. [TestFlight beta](https://testflight.apple.com/join/BNya22Jg).

</td>
</tr>
</table>

### The switching principle

```
Desktop (Play)  ←──→  localhost:8400  ←──→  Cloud (Fly.io)  ←──→  Phone (iOS)
     │                      │                     │                    │
     └──────── Same API ────┴──── Same proofs ────┴──── Same auth ─────┘
```

One server. Many surfaces. The cloud isn't a separate product — it's the same Python file running somewhere your phone can reach. Switch between desktop and phone mid-session. Your proofs, your history, your credits follow you.

### Principles

1. **Argue first, conclude second.** Every claim passes through 3-5 models + a dedicated sceptic before it becomes a proof.
2. **Memory is not optional.** Verified claims persist as immutable, citable artifacts. Science needs a trail.
3. **Cheap by default.** Route to the cheapest model that can do the job. Escalate only when the claim demands it.
4. **No lock-in.** You own your data, your proofs, your keys. Export everything. Run it yourself.

<div align="center">

---

<sub>Amsterdam · Open Source · Non-Profit · <a href="https://rhea-tribunal.fly.dev">rhea-tribunal.fly.dev</a></sub>

</div>

---

## Repositories

| Repo | Description | Platform |
|------|-------------|----------|
| rhea-project | Core tribunal API + multi-model bridge | Python/Fly.io |
| rhea-ios | iOS app — auth + 8-tab SwiftUI client | iOS/Swift |
| rhea-play | macOS operations centre — 12-pane command centre | macOS/Swift |
| rhea-atlas | Plugin-based web operations UI | Next.js |
| rhea-keyboard | iOS keyboard extension — tribunal + pipeline builder | iOS/Swift |
| rhea-memory | Python memory layer — SQLite KV store + timeline | Python |
| rhea-cli | Unified CLI for Rhea ops | Rust |
| homebrew-tap | Homebrew formulae for Rhea tools | Shell |
| rhea-tutorials | Learn to build a multi-model AI system | Docs |

## Architecture

All repos connect to the tribunal API (rhea-project) as their backend.
Shared libraries: RheaKit (Swift), rhea-memory (Python).

## Enterprise Conventions

- Semantic versioning (SemVer) for all packages
- CLAUDE.md in every repo for AI-assisted development
- MIT License
- Conventional commits (feat/fix/chore/docs)

---

# Revision: one system, preserved history

> Appended 2026-07-24. The profile above is preserved as a historical public
> state. This revision adds current direction and evidence boundaries; it does
> not erase the earlier claims, repos, experiments, or vocabulary.

## Institutional direction

**TimeLabs Non-Profit Corp** is not disposable branding. It is the project's
core institutional direction: an international technical player, foundation
initiator, and community core intended to carry the work into its next
evolutionary stage.

Institutional ambition and legal facts are different fields. Exact
incorporation status, jurisdiction, registration identifiers, charitable
status, payment commitments, and official addresses must be attached when
verified rather than inferred from a README.

## The long path is the product

TimeLabs products are a long sequence of blinded but persistently
right-oriented steps. Together they form system-level deliverables:

- **Omnia Networks** — owner-controlled network evidence, deterministic state,
  policy, recovery, and bounded automation.
- **Rhea Tribunal** — multi-model disagreement and adversarial review.
- **Local hyper-compact Tribunal** — a small private dissent capsule with no
  execution authority.
- **World 2.0** — the school, mathematical theory, and living-system
  representation work.
- **Memory and DTS** — continuity plus logical ordering across sessions and
  devices.
- **Native, web, CLI, keyboard, atlas, and experimental surfaces** — different
  ways to reach the same system.
- **Deprecated packages** — conserved knowledge. Deprecation records actual
  maturity and replacement paths; it does not revoke the work's dignity or
  delete its history.

Every repository must mark its real state as one of: historical, concept,
prototype, tested, released, operated, deprecated, or quarantined. A state
label is evidence metadata, not an insult.

## Revised system contract

```text
schema / contract
  → bounded observation
  → DTS logical order
  → redact / validate
  → log.0
  → named SQLite views:
       catalog.sqlite
       assurance.sqlite
       workflow.sqlite
  → deterministic checks
       PASS → signed policy gate
       FAIL / ERROR → abort + receipt
       UNKNOWN → quarantine
  → bounded automation
  → verify → close / bounded retry / emergency stop
```

`log.0` is the reconstruction record. Named SQLite views are rebuildable and
may answer different questions. Rhea, a dashboard, search, or a living 3D
surface is a view or reviewer—not a second hidden source of truth.

The current Omnia implementation is experimental and read-only. Its v0 DTS is
a central committed logical sequence, not yet a claim of distributed
causality, CRDT convergence, or consensus.

## Authority and credential isolation

- The Owner retains root policy and independent recovery.
- The Owner is not required to approve every normal event inside signed policy.
- Every dedicated node, worker, and executor uses its own least-privilege,
  revocable credential and attributable identity.
- Workers do not borrow the Owner's personal credential for model
  conversations, repository writes, deployments, or external effects.
- One worker's credential cannot silently become another worker's authority.
- Tribunal output may criticize or dissent; it cannot widen policy or authorize
  execution.

## Knowledge preservation rule

**APPEND prior state before REPLACE.**

Before a public narrative, schema, package, or system surface is replaced:

1. preserve the prior state in reachable history or a named archive;
2. record why it changed and what supersedes it;
3. keep provenance and migration links;
4. mark false, unsafe, or obsolete claims without pretending they never
   existed;
5. delete only material that must be removed for privacy, security, licensing,
   or an explicit owner decision—and retain a non-sensitive deletion receipt.

Replacement or destruction of information without preserving its historical
state violates the TimeLabs knowledge contract.

The withdrawn owner-controlled-evidence rewrite is therefore preserved at
[`revisions/README-2026-07-24-owner-controlled-evidence-draft.md`](revisions/README-2026-07-24-owner-controlled-evidence-draft.md).

## Evidence boundary

The original profile contains ambitious and historically important claims.
Current publication must distinguish the direction from demonstrated state:

- model agreement is a review signal, not truth or scientific proof;
- a hash is content identity, not truth, actor identity, or trusted time;
- `UNKNOWN` is not `PASS`;
- a documented design is not automatically implemented, released, or operated;
- legal, payment, licensing, privacy, and deployment claims require current
  owner-approved evidence.

This boundary preserves ambition by making the next successful claim harder to
dismiss.
