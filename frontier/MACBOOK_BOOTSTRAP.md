# MacBook Frontier Bootstrap 0.1

This is the local execution handoff. Remote orchestration may prepare contracts and GitHub tasks, but must not claim local Mac commands ran unless Mac post-state evidence exists.

## 1. Doctor

```bash
python3 frontier/frontier-evolve.py doctor
```

Preserve `artifacts/doctor.json`. Confirm actual paths/versions for `git`, `gh`, `codex`, `gemini`, optional `rhea`, and any Trae automation interface.

## 2. Wave-0 dry run

```bash
python3 frontier/frontier-evolve.py wave0 --dry-run
```

This emits one-cell task capsules only.

## 3. Local independent lanes

After reviewing capsules:

```bash
export FRONTIER_WORKSPACE="$HOME/src"
python3 frontier/frontier-evolve.py wave0 --execute --agents codex,gemini --max-parallel 4
```

Wave 0 is audit-only. The script only uses already-present local checkouts. It never auto-clones, merges, deploys, edits routers, changes billing or publishes releases.

## 4. Trae

Do not guess command syntax. `doctor` records whether a `trae` executable exists. If the actual local automation command is known, bind it through `FRONTIER_TRAE_CMD`; otherwise open the emitted capsule in Trae manually and preserve the resulting branch/evidence.

## 5. GitHub Copilot / partner agents

For cloud-suitable tasks, create/assign a GitHub issue from the exact task capsule. Do not include local secrets or private topology. The resulting PR is a candidate; local target verification remains separate.

## 6. Never auto-merge Wave 0

Compare independent results first. Promote exactly one small falsifiable implementation experiment per cell into later waves.
