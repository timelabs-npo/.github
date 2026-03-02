<div align="center">

# TimeLabs

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

**[rhea-project](https://github.com/timelabs-npo/rhea-project)** — Core tribunal API, Aletheia proof chain, landing page. FastAPI + Rust + Python. The backbone.

**[rhea-memory](https://github.com/timelabs-npo/rhea-memory)** — Persistent memory layer for AI agents. SQLite KV store + timeline + compact context generator. `pip install rhea-memory`.

</td>
<td width="50%">

**[rhea-play](https://github.com/timelabs-npo/rhea-play)** — Native macOS operations centre. 12-pane SwiftUI window: Radio, Tribunal, Governor, Tasks, Aletheia, Ruliad, NDI, and more. One screen, everything at a glance.

**[rhea-ios](https://github.com/timelabs-npo/rhea-ios)** — iOS tribunal client. 8-tab native app with Keychain auth, proof browsing, live agent feed. [TestFlight beta](https://testflight.apple.com/join/BNya22Jg).

</td>
</tr>
</table>

### Principles

1. **Argue first, conclude second.** Every claim passes through 3-5 models + a dedicated sceptic before it becomes a proof.
2. **Memory is not optional.** Verified claims persist as immutable, citable artifacts. Science needs a trail.
3. **Cheap by default.** Route to the cheapest model that can do the job. Escalate only when the claim demands it.
4. **No lock-in.** You own your data, your proofs, your keys. Export everything. Run it yourself.

<div align="center">

---

<sub>Amsterdam · Open Source · Non-Profit · <a href="https://rhea-tribunal.fly.dev">rhea-tribunal.fly.dev</a></sub>

</div>
