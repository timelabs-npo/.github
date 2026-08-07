# Agent Swarm Protocol 0.1

## Purpose
Run Codex, Gemini, Trae, and GitHub Copilot as independent implementation/review lanes without collapsing them into one shared hallucination surface.

## Lane contract
Each lane receives the same frozen Task Capsule and fixture set, but not sibling candidate diffs until first-pass evidence is sealed.

### Codex lane
- Local Mac worktree.
- May build/test and inspect post-state within task scope.
- Non-interactive automation is allowed only when the installed CLI exposes the relevant command.

### Gemini lane
- Local isolated worktree or read-only audit clone.
- Prefer structured headless output for evidence capture.
- Installed CLI/runtime policy is discovered locally; no remote document grants authority.

### Trae lane
- Treat the local Trae interface as discoverable runtime state.
- Record whether an automation/CLI surface actually exists.
- Until discovered, use the same task capsule as a manual IDE task; never invent command syntax.

### Copilot lane
- Cloud issue/Agents task with no local secrets.
- Acceptance criteria and claim ceiling must exist before assignment.
- Resulting PR is a candidate, not verified local post-state.

### Rhea lane
- Advisory/reviewer only.
- May aggregate disagreement and preserve evidence.
- Cannot substitute consensus for deterministic verification or human authority.

## Isolation
Branch convention: `agent/<agent>/<task-id>` or the tool-native equivalent (`codex/`, `trae/`, `copilot/`).

No lane reads a sibling candidate diff before freezing its own first-pass evidence receipt.

## Evidence receipt
Every lane emits `timelabs.frontier.evidence/0.1` and explicitly records:

```text
INTENT -> ACTION -> RESULT -> POST-STATE -> EVIDENCE
```

plus residual uncertainty.

## Comparison
After first-pass freeze:

1. reveal candidates;
2. run identical acceptance tests;
3. compare behavior, changed files, complexity, claims and failure modes;
4. appoint a red-team lane that did not author the preferred candidate;
5. human accepts, synthesizes or rejects;
6. clean-checkout post-merge verification;
7. update claim register from observed post-state.

## No self-merging
No lane can merge its own candidate solely on self-produced evidence. A model vote, branch name, hash or green self-authored test is insufficient by itself.
