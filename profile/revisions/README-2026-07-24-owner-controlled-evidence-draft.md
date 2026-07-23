# Preserved revision draft: owner-controlled evidence

> This draft temporarily replaced the organization profile in
> `codex/council-posture`. It is preserved instead of discarded after review
> established the rule: revise and append; do not erase prior project state.

<div align="center">

# TimeLabs

**Create the invisible. Make it observable, reviewable, and owner-controlled.**

Experimental systems lab · open engineering · evidence before authority

</div>

---

TimeLabs builds infrastructure for turning intent into systems that can be
inspected before they act.

The work is larger than a collection of utilities. Applications, agents,
interfaces, and model providers are replaceable surfaces. The durable layer is
the contract underneath them:

```text
schema / contract → bounded observation → deterministic evaluation
                                              ├─ FAIL / ERROR → abort
                                              ├─ UNKNOWN → quarantine
                                              └─ PASS → signed policy gate
                                                               ↓
                                                    bounded automation
                                                               ↓
                                              verify → close / bounded retry
```

No model, application, or hosted service is the root authority. The Owner
retains keys, policy, recovery, and the right to operate without an AI gate.
The Owner sets the delegated envelope; they are not required to approve every
normal event.

## Current status

TimeLabs repositories are a mixed research portfolio. They include prototypes,
experiments, reusable components, and historical work. Presence in the
organization does not mean that a repository is released, supported,
production-ready, scientifically validated, or suitable for regulated use.

Public materials must preserve these distinctions:

- **concept** — an idea or design note;
- **prototype** — implemented enough to explore;
- **tested** — verified against a declared test scope;
- **released** — versioned artifact with provenance;
- **operated** — deployed with an explicit owner and support boundary.

`UNKNOWN` is not `PASS`. A hash is not proof of truth. Model agreement is not
scientific or legal verification.

## Direction

### Omnia

**[omnia-playbook](https://github.com/timelabs-npo/omnia-playbook)** is the
experimental owner-controlled assurance substrate.

Its intended core is local-first and dependency-light:

```text
multi-device events
  → DTS logical order
  → redact / validate
  → log.0
  → catalog.sqlite + assurance.sqlite + workflow.sqlite
```

The append-only log is the reconstruction source. Read models are rebuildable.
Provider tools may contribute bounded observations through narrow adapters, but
large third-party applications do not become Omnia's authority root.

The v0 Deterministic Time System (DTS) is a single-writer logical sequence, not
wall-clock ordering. It does not claim distributed causality, CRDT convergence,
or consensus. Omnia can record provenance and evaluate declared invariants. It
does not certify legal compliance or contain a mutating executor today.

### Rhea

**[rhea-project](https://github.com/timelabs-npo/rhea-project)** explores
multi-model critique, disagreement, and adversarial review.

Rhea is advisory research. A Tribunal can challenge a claim, expose divergent
assumptions, and help an Owner inspect a decision. Consensus does not convert a
claim into truth, and the Tribunal has no execution authority in Omnia.

### Surfaces and experiments

The remaining repositories explore memory, native interfaces, command-line
tools, edge runtimes, tutorials, and interaction patterns. They are inputs to
the lab, not a catalogue of guaranteed products. Each repository must state its
own maturity, support, license, data boundary, and release status.

## Engineering principles

1. **Owner authority is explicit.** Keys, signed policy, critical-deviation
   approval, and recovery remain owner-controlled.
2. **Evidence precedes conclusion.** Preserve provenance, limitations, and
   `PASS / FAIL / UNKNOWN / ERROR`.
3. **Minimize before persistence.** Sensitive raw output is not a default
   artifact.
4. **Source records are append-only.** Derived state is rebuildable and
   replaceable.
5. **AI is optional and advisory.** Deterministic checks define the assurance
   boundary; model output is evidence payload, not authorization.
6. **Mutation fails fast.** Only `PASS` may enter a signed policy gate.
   `FAIL/ERROR` abort, `UNKNOWN` quarantines, and retry is budgeted.
7. **Claims match evidence.** Concept, prototype, test, release, and operation
   are never used interchangeably.
8. **No blanket legal promises.** Legal status, jurisdiction, privacy,
   licensing, donations, and regulated-use claims require verified,
   owner-approved documentation.

## Public review boundary

Nothing in this organization is a compliance certificate, professional advice,
or a substitute for an independent security, privacy, scientific, or legal
assessment.

Before an artifact is sent to an external authority, its exact commit and
digests must be frozen; public claims, licenses, data handling, dependencies,
security reporting, and release provenance must pass a documented publication
gate.

---

<div align="center">

**Build boldly. Claim precisely. Leave a trail that can be examined.**

</div>
