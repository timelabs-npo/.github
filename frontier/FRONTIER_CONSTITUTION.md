# TIMELABS FRONTIER CONSTITUTION
## Global alignment, claim ceilings, and bounded self-evolution

**Version:** 0.1  
**Freeze date:** 2026-08-07  
**Status:** WORKING CONSTITUTION / GOVERNANCE DRAFT  
**Authority:** human constitutional owner; agents are bounded workers and reviewers.

> **Mission.** Keep the ecosystem near the engineering/research frontier without collapsing it into one prompt-shaped blob. Every project remains a separate zoo cell with its own source of truth, ontology, tests, risk envelope, and claim ceiling. Cross-boundary fusion occurs only through typed, versioned, replayable contracts. Parallel agents buy speed; independent evidence buys confidence.

## Table of contents

1. Executive theorem
2. Truth and authority
3. Global ceilings
4. Active zoo cells
5. Claims / goals / methods / proof rules by family
6. Cross-boundary law
7. Agent council
8. Blind-parallel swarm protocol
9. Self-evolution loop
10. Merge tribunal
11. Mutation, privacy, cost and publication gates
12. Wave 0
13. Wave 1
14. Quarantine rule
15. Frontier-head checklist

---

## 1. Executive theorem

No model, UI, database, cloud service, resolver, dashboard, branch, consensus score, embedding, curvature metric, or ranking becomes authority merely because it is convenient.

**Authority must be explicit. Truth must be evidenced. Mutation must be bounded. Cross-boundary knowledge must preserve provenance.**

The system is a graph of cells, not a monolith:

```text
project-local observation / code / tests
                 |
                 v
        typed evidence contract
                 |
      +----------+----------+
      |          |          |
    Codex      Gemini      Trae       Copilot
      |          |          |            |
      +------ independent candidates ----+
                         |
                  deterministic tests
                         |
                  red-team comparison
                         |
                   human merge tribunal
```

Rhea may advise, aggregate disagreement, preserve evidence, and surface tasks. It is not a truth oracle and does not acquire mutation authority by consensus.

---

## 2. Truth and authority

### 2.1 State-change invariant

For every meaningful state-changing action preserve:

```text
INTENT -> ACTION -> RESULT -> POST-STATE -> EVIDENCE
```

A command returning zero is not proof that the intended system property holds. A file edit is not proof that a running process loaded it. A hash proves integrity/identity of bytes, not semantic truth.

### 2.2 Truth labels

| Label | Meaning | Claim ceiling |
|---|---|---|
| `PROPOSED` | design/hypothesis only | planned/hypothesized wording only |
| `DERIVED` | follows from preserved assumptions/evidence | assumptions must be exposed |
| `OBSERVED` | seen in one preserved run/environment | no portability/generalization |
| `VERIFIED_LOCAL` | reproduced under named bounded conditions | claim limited to those conditions |
| `VERIFIED_REPRODUCIBLE` | repeatable procedure + fixtures + evidence | reproducibility claim under stated conditions |
| `CONTRADICTED` | current evidence conflicts with claim | claim blocked pending reconciliation |
| `PARKED` | outside current execution wave | no implementation implication |

**Claim ceiling:** no internal or public wording may exceed the strongest preserved evidence.

### 2.3 Preferred source-of-truth order

1. live deterministic post-state relevant to the task;
2. code + reproducible tests + fixtures;
3. repository-local schemas/manifests/invariants;
4. canonical repository instructions;
5. current official external documentation;
6. architecture notes / README;
7. issue/task prose;
8. model output.

---

## 3. Global ceilings

### C1 — One-cell execution ceiling
A normal task has exactly **one primary repository/cell** and at most **one typed cross-boundary output**. Governance-only work is the explicit exception.

### C2 — Claim ceiling
No claim is promoted past its evidence label. Tests must exercise the claimed property rather than merely execute code.

### C3 — Authority ceiling
No LLM, Tribunal vote, TOPSIS score, Ricci curvature, confidence value, reviewer swarm, or historical success can widen execution policy.

### C4 — Mutation ceiling
Wave 0 is read-only/governance-only. Later mutation requires: bound target, before-state, bounded operation, resource/time budget, reversal/rollback statement, canary where applicable, and observed post-state.

### C5 — Merge ceiling
The authoring lane cannot be the sole validator. Merge requires independent validation or a deterministic external oracle plus acceptance tests.

### C6 — Concurrency ceiling
Default swarm has up to four named lanes: **Codex, Gemini, Trae, Copilot**. Hard maximum is **8 parallel lanes** without a versioned constitutional exception. Every lane works in isolation until its first evidence freeze.

### C7 — Blast-radius ceiling
A normal implementation PR modifies one primary cell and one declared contract. Cross-repo fusion is split into producer -> schema freeze -> consumer.

### C8 — Cost ceiling
Every executable task declares wall-clock, API/token and monetary budgets. No unbounded retry or silent paid-service escalation. Numeric values are task-local, not globally invented.

### C9 — Privacy ceiling
Credentials, account identifiers, raw private topology, private packet content and sensitive local diagnostics remain in explicitly authorized local boundaries. Public receipts are minimized/redacted.

### C10 — Context ceiling
Each agent receives the smallest useful task capsule. Vendor/reference repositories are read-only by default. Sibling candidate diffs remain hidden until independent first-pass work is frozen.

### C11 — Dependency ceiling
Cloud, DNS, model providers, hosted DBs and dashboards may be conveniences/witnesses. None becomes a hidden mandatory authority root without an ADR and degraded/offline behavior.

### C12 — Self-evolution ceiling
“Self-evolving” means continuously detecting drift, proposing bounded changes, implementing candidates, testing them, comparing independent lanes and opening reviewable PRs. It does **not** mean self-granted goals, self-expanded permissions, autonomous merges, or perpetual production mutation.

---

## 4. Active zoo cells

The Wave-0 active first-party set is intentionally narrower than every accessible GitHub repository.

### G — Governance
- `timelabs-npo/.github` — constitution, schemas, task/evidence contracts, org conventions.
- `timelabs-npo/oaisb` — sandbox only; no production authority.

### R — Rhea advisory / interfaces
- `timelabs-npo/rhea-project`
- `timelabs-npo/rhea-memory`
- `timelabs-npo/rhea-play`
- `timelabs-npo/rhea-ios`
- `timelabs-npo/rhea-keyboard`
- `timelabs-npo/rhea-atlas`
- `timelabs-npo/rhea-cli`
- `timelabs-npo/rhea-tutorials`
- `timelabs-npo/homebrew-tap`

### K — Deterministic kernel research
- `timelabs-npo/rheknel`

### N — Network sovereignty / embodied observability
- `timelabs-npo/Blueshoes` — canonical edge runtime.
- `timelabs-npo/omnia-playbook` — invariant/check/evidence substrate.
- `serg-alexv/hme` — deterministic embodiment of bounded measurements.
- `serg-alexv/network-hardening-blueprint` — deployment/profile examples.
- `serg-alexv/dev-UnitedNetworks` — AR/spatial diagnostics lab.
- Sovereign Resolution Lab — experimental concept: DNS is one evidence backend, not the epistemic boundary.

### O — Opportunity/research support
- `serg-alexv/ontofishing` — verification-first opportunity discovery/scoring.

All other accessible repositories are `auto_evolve=false` until lineage and scope are explicitly promoted.

---

## 5. Claims, goals, methods and proof rules

### 5.1 Rhea advisory family

**Allowed claim:** multiple models can independently evaluate an input and the system can preserve outputs, disagreement/agreement metrics, red-team challenges and evidence records.

**Blocked claim:** consensus proves truth; confidence percentage is calibrated reality; a hash chain proves semantic correctness.

**Goal:** fast multi-model adversarial advisory with durable provenance and bounded cost.

**Methods:** independent calls, sceptic/red-team lane, deterministic aggregation where possible, replay fixtures, explicit provider/output provenance.

**Proof rules:** fixed fixtures; timeout/failure tests; aggregation determinism; calibration experiment for any confidence claim; cryptographic integrity tested separately from semantic correctness.

### 5.2 Rhea memory

**Allowed claim:** records persist/retrieve under tested storage conditions.

**Blocked claim:** remembered content is true/current/authoritative because it was stored.

**Proof rules:** write/read/restart round trip; corruption handling; compaction equivalence; stale/version metadata.

### 5.3 Rhea clients: Play / iOS / Atlas / Keyboard

**Goal:** ergonomic projections and bounded interaction surfaces.

**Blocked claim:** UI projection is canonical backend truth.

**Proof rules:** contract fixtures, offline/degraded behavior, auth-boundary tests, named OS/device build/runtime evidence. `rhea-keyboard` keeps its `<30 MB` extension target until deliberately revised.

### 5.4 Rhea CLI

**Goal:** ergonomic coordination facade without erasing authority boundaries.

**Method:** every mutating command maps to a typed operation and evidence receipt.

**Proof rules:** target binding, dry-run where meaningful, before/post-state, exit semantics, rollback declaration, explicit non-reversibility where rollback is impossible. Emergency commands receive the strictest target binding.

### 5.5 Rheknel

**Allowed claim now:** tiny deterministic C event/filter kernel research exists.

**Targets, not facts until measured:** `<2 KB`, universal predictability, L4 safety, certification, real hardware kill-switch efficacy.

**Proof rules:** reproducible compiler/toolchain; binary/map size evidence; allocation audit; deterministic trace fixtures; fault injection; HIL testing for hardware claims; independent safety-standard review before certification wording.

### 5.6 Blueshoes

**Goal:** sovereign adaptive edge networking that remains locally observable and never makes an LLM the packet-path safety oracle.

**Methods:** read-only probes, local journals, typed capability graph, deterministic planner, snapshot/apply/validate/rollback, canary, platform adapters.

**Proof rules:** named hardware/OS evidence; planner fixtures; rollback fault injection; post-state comparison; platform-specific adapter tests. Command success never substitutes for observed network state.

### 5.7 Omnia

**Goal:** portable invariant/check/evidence substrate with rebuildable projections and explicit policy boundaries.

**Methods:** versioned checks, local append record, disposable views, fail-fast policy semantics, minimized collection.

**Proof rules:** exact-byte replay, torn-tail/corruption tests, projection rebuild equality, contract/schema fixtures, privacy regression tests. “Proof” wording is reserved for exactly defined properties.

### 5.8 HME / WorldEngine

**Goal:** embody bounded observations without increasing what the sensor knows.

**Hard epistemic law:** renderer/state mapping may transform declared measurements; it may not infer undeclared physical meaning.

**Proof rules:** golden traces, cross-implementation equality where claimed, schemas, stale/error states, provenance, replay/live distinction, preserved run hashes.

### 5.9 Sovereign Resolution Lab

**Hypothesis:** resolution is a local reasoning operation over distributed evidence; DNS can be a compatibility/evidence backend rather than the application’s authority root.

**Wave-1 method:** replay-only candidate set containing endpoint, provenance, verification state, observation time and expiry. No live DNS replacement or routing mutation in v0.

**Proof rules:** deterministic candidate ordering under frozen evidence; explicit conflicting witnesses; stale/expiry semantics; no claim that reachability proves identity; no claim that DNS can disappear for arbitrary legacy names whose only location evidence exists in DNS.

### 5.10 Ontofishing

**Goal:** smallest set of verifiable, executable, high-ROI opportunities.

**Ceiling:** no automatic application submission, purchase, contract acceptance or paid registration in self-evolution waves.

**Proof rules:** source provenance, hard rejection filters, reproducible score fixtures, explicit stale-date handling, human acceptance before external commitment.

---

## 6. Cross-boundary law

Cross-boundary coupling uses a versioned contract, not shared prose or hidden imports.

Minimum envelope:

```text
contract_id
version
producer_cell
consumer_cell
schema
provenance
freshness / expiry
error + unknown semantics
integrity field
claim ceiling
```

A producer cannot define the consumer’s ontology. A consumer cannot retroactively reinterpret producer evidence without a new contract version.

The first preferred fusion remains deliberately tiny:

```text
Blueshoes preserved telemetry
        -> timelabs.network-condition/0.1
        -> HME feature adapter
        -> deterministic offline replay
```

No router mutation is required to prove this fiber.

---

## 7. Agent council

### Codex
Primary local implementation/repo worker on the MacBook. Strong role: inspect -> edit -> build -> test -> emit receipt. Must preserve repository-local instructions and post-state evidence.

### Gemini
Independent implementation/research lane. Headless/scripted mode may participate, but its output remains a candidate. It must receive the same frozen task capsule and acceptance tests as sibling lanes.

### Trae
Independent IDE/agent lane. Local command syntax and authority are discovered from installed runtime state; never invented by this constitution. Existing Trae branches are evidence that this lane is already useful in the ecosystem.

### GitHub Copilot coding agent
Asynchronous GitHub-native implementation lane operating from reviewable issues/branches/PRs. It receives the same capsule and cannot auto-merge its own work.

### Rhea Tribunal
Reviewer/advisory surface. It may compare claims, expose disagreement and retain evidence. It does not grant authority or certify truth by vote.

---

## 8. Blind-parallel swarm protocol

1. **T0 Freeze** — task capsule, fixtures, claim ceiling and acceptance tests are immutable for the round.
2. **T1 Isolate** — lanes use distinct branch/worktree namespaces: `codex/`, `gemini/`, `trae/`, `copilot/`.
3. **T2 Blind first pass** — sibling diffs are hidden until each lane freezes its evidence receipt.
4. **T3 Same tests** — run identical deterministic acceptance tests.
5. **T4 Reveal** — compare diffs, receipts, complexity, regressions and unsupported claims.
6. **T5 Red-team** — an independent lane attacks assumptions and negative cases rather than polishing the winner.
7. **T6 Merge tribunal** — human chooses/synthesizes; model votes are advisory.
8. **T7 Clean-checkout verification** — post-merge tests execute from a clean checkout.
9. **T8 Claim update** — documentation/claim register changes only from verified post-state.

---

## 9. Self-evolution loop

```text
OBSERVE -> FIND DRIFT -> CAPSULE -> PARALLEL CANDIDATES -> TEST
       -> RED TEAM -> HUMAN MERGE -> CLEAN VERIFY -> RECEIPT -> NEXT
```

The loop stops or quarantines when scope is ambiguous, evidence conflicts, budget is exhausted, required secrets/production access are absent, or a task would cross the declared blast radius.

Self-evolution optimizes **evidence density per unit attention**, not commit count.

---

## 10. Merge tribunal

A candidate is mergeable only when:

- task capsule stayed within one-cell ceiling;
- claim ceiling is respected;
- deterministic acceptance tests pass;
- an independent validator exists;
- secrets/private evidence are absent from public diff;
- any mutation has before/post-state and reversal semantics;
- docs do not describe unverified targets as deployed facts;
- residual uncertainty is explicitly recorded.

`PASS` means the declared acceptance contract passed. It never means “globally correct.”

---

## 11. Mutation, privacy, cost and publication gates

Wave 0 must not change routers, production services, billing, credentials, releases or external accounts.

Future mutation capsules must bind exact target, allowed operation IDs, time/resource budget, retry ceiling, required checks, reversal support and notification/receipt destination.

Sensitive local inspection may exist, but it is not automatically uploadable evidence. Minimized evidence should be sufficient for most comparisons.

Publication must separate verified capability, historical report, target, hypothesis and narrative.

---

## 12. Wave 0 — global alignment

For every active first-party cell:

1. inventory canonical source of truth;
2. inventory build/test commands and known environment assumptions;
3. locate claim registers / README claims / public promises;
4. map each material claim to evidence label;
5. identify contradictory or stale architecture language;
6. identify project-local ceilings;
7. propose exactly one falsifiable next experiment;
8. produce a minimized evidence receipt;
9. do **not** mutate production, networking, credentials, billing or releases;
10. do **not** merge automatically.

Wave 0 may create branch-only governance/documentation candidates and review artifacts.

---

## 13. Wave 1 — first typed fibers

Priority sequence:

1. **F-001 Blueshoes -> HME**: offline replay adapter, deterministic first.
2. **Omnia reconciliation**: independently compare the Codex `log.0` candidate and Trae OpenBSD bounded-evidence candidate; preserve both concerns, no blind auto-merge.
3. **Rhea evidence semantics**: formally separate consensus, integrity, provenance and truth claims.
4. **Sovereign Resolution v0**: candidate/evidence API with DNS as one backend; replay before live querying.
5. **Rhea CLI receipt adapter**: harmless read-only command produces typed post-state receipt before mutating command work expands.

---

## 14. Quarantine rule

Legacy mirrors, upstream/vendor forks, reverse-engineering provider proxies, bypass/reference projects, binary-hooking repositories, large third-party libraries and unclassified personal repositories remain `auto_evolve=false`.

They may be read as evidence/reference. They do not receive autonomous edits until explicitly promoted with ownership/lineage, purpose, test surface, risk class and claim ceiling.

---

## 15. Frontier-head checklist

Before calling a direction “real”:

- What is the one primary cell?
- What exactly is observed versus proposed?
- What would falsify the claim?
- What is the smallest replay/fixture that exercises it?
- What is the typed boundary?
- Which independent lane attacks it?
- What is the resource/blast-radius ceiling?
- Can the system degrade without a cloud/DNS/model vendor?
- Is post-state observed?
- Is residual uncertainty visible?

**Desired operating aesthetic:** fewer mystical mega-prompts; more small beasts with sharp teeth, typed doors, reproducible tricks, and enough independent agents to keep one another from becoming theology.
