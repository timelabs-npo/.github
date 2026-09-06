# Facade checkpoint tooling

Saved when the task owner requested a stop and GitHub checkpoint on 2026-09-06. These files preserve progress; they do not trigger publication or deployment.

`verify_facades.py` was implemented and executed by GitHub Copilot CLI 1.0.83. It checks the fifteen README targets, local file links, fence counts, whitespace, changed-path allowlists, site element IDs and the fifteen family repository URLs. It does not validate Markdown anchors, external link availability, semantics, runtime behavior or deployment. The frozen report passed before the checkpoint files and visual reference were added.

To reproduce, copy this directory to a scratch workspace, clone the listed repositories into the relative `repos/` paths in `baselines.json` (`.github` uses `repos/org-profile`), then run `python3 verify_facades.py` from that workspace. The script writes `verification.json`. Baseline SHAs identify the original source snapshot; changed-path checks inspect the current working tree, not a historical commit range.

The verifier's allowlists describe the editing wave. Checkpoint files and the subsequently supplied reference image are additional preservation artifacts, recorded in the publication receipt. A rerun on clean clones can check the current file links but does not reproduce the original pending-diff check.

See [the publication receipt](../FACADE_RECEIPT.md) for commits, known failures, deployment status and the next step. Private inspiration exports, provider account details and local diagnostic output are not included.
