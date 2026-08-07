#!/usr/bin/env python3
"""Timelabs Frontier Wave-0 orchestrator.

Dry-run by default. It never auto-merges and never guesses a Trae CLI.
The objective is task/evidence generation and isolated first-pass agent lanes.
"""
from __future__ import annotations
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = pathlib.Path(__file__).resolve().parent
REGISTRY = ROOT / "PROJECT_REGISTRY.json"
ART = ROOT / "artifacts"


def run(cmd, cwd=None, check=False, capture=True):
    p = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    if check and p.returncode:
        raise RuntimeError(f"command failed {p.returncode}: {cmd}\n{p.stdout}")
    return p


def tool(name):
    return shutil.which(name)


def doctor():
    facts = {
        "python": sys.version.split()[0],
        "git": tool("git"),
        "gh": tool("gh"),
        "codex": tool("codex"),
        "gemini": tool("gemini"),
        "trae": tool("trae"),
        "rhea": tool("rhea"),
    }
    for key, value in list(facts.items()):
        if key == "python" or not value:
            continue
        p = run([value, "--version"])
        facts[key + "_version"] = (p.stdout or "").strip()[:500]
    out = ART / "doctor.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(facts, indent=2) + "\n")
    print(json.dumps(facts, indent=2))
    return 0


def load_registry():
    return json.loads(REGISTRY.read_text())


def capsule_for(project):
    task_id = "W0-" + project["repo"].replace("/", "-").upper()[:48]
    return {
        "schema": "timelabs.frontier.task/0.1",
        "task_id": task_id,
        "primary_cell": project["cell"],
        "repo": project["repo"],
        "objective": (
            "Audit current claims, source-of-truth, tests and drift; propose exactly "
            "one next falsifiable experiment. Do not change product behavior."
        ),
        "claim_ceiling": "OBSERVED",
        "allowed_reads": [
            "repository files",
            "git history",
            "tests",
            "official current docs when required",
        ],
        "allowed_writes": ["FRONTIER.md proposal", "evidence receipt"],
        "forbidden_actions": [
            "production mutation",
            "credential access",
            "release",
            "merge",
            "billing changes",
            "network/router mutation",
            "cross-repo implementation",
        ],
        "budgets": {
            "wall_minutes": 30,
            "cost_usd_max": 2.0,
            "parallel_lanes_max": 4,
        },
        "acceptance": [
            "canonical source of truth identified",
            "unsupported claims listed",
            "one next falsifiable experiment proposed",
            "residual uncertainty explicit",
        ],
        "evidence_required": [
            "git HEAD",
            "test/build commands discovered",
            "claim-to-evidence table",
            "changed-file list if any",
        ],
        "cross_boundary_output": None,
    }


def emit_capsules():
    registry = load_registry()
    out = ART / "wave0" / "capsules"
    out.mkdir(parents=True, exist_ok=True)
    count = 0
    for project in registry["projects"]:
        if not project.get("auto_evolve"):
            continue
        capsule = capsule_for(project)
        path = out / (capsule["task_id"] + ".json")
        path.write_text(json.dumps(capsule, indent=2) + "\n")
        count += 1
    print(f"emitted {count} Wave-0 capsules to {out}")
    return count


def lane_prompt(capsule):
    return (
        "You are one independent Timelabs Wave-0 audit lane.\n\n"
        + "TASK CAPSULE:\n"
        + json.dumps(capsule, indent=2)
        + "\n\nRules:\n"
        + "- Audit only; do not change product behavior.\n"
        + "- Never upgrade model agreement/hash existence into semantic truth.\n"
        + "- Mark VERIFIED/OBSERVED/DERIVED/PROPOSED separately.\n"
        + "- Identify exact repo-local source of truth and README/docs overclaims.\n"
        + "- Propose exactly one small falsifiable next experiment.\n"
        + "- Return a concise JSON-compatible report with evidence paths/commands and residual uncertainty.\n"
    )


def run_lane(agent, capsule, cwd):
    start = time.time()
    result = {
        "agent": agent,
        "task_id": capsule["task_id"],
        "repo": capsule["repo"],
        "started": start,
    }
    if agent == "codex":
        exe = tool("codex")
        if not exe:
            result.update(status="SKIPPED", reason="codex not found")
            return result
        p = run([exe, "exec", lane_prompt(capsule)], cwd=cwd)
    elif agent == "gemini":
        exe = tool("gemini")
        if not exe:
            result.update(status="SKIPPED", reason="gemini not found")
            return result
        p = run([exe, "-p", lane_prompt(capsule), "--output-format", "json"], cwd=cwd)
    elif agent == "trae":
        cmd = os.environ.get("FRONTIER_TRAE_CMD")
        if not cmd:
            result.update(
                status="READY_MANUAL",
                reason=(
                    "Set FRONTIER_TRAE_CMD only after doctor/local inspection discovers "
                    "the actual Trae automation interface"
                ),
            )
            return result
        p = run(["/bin/sh", "-lc", cmd], cwd=cwd)
    else:
        result.update(status="SKIPPED", reason="unknown local lane")
        return result

    result.update(
        status="OK" if p.returncode == 0 else "FAILED",
        exit_code=p.returncode,
        output=(p.stdout or "")[-20000:],
        elapsed_s=round(time.time() - start, 3),
    )
    return result


def wave0(args):
    emit_capsules()
    registry = load_registry()
    active = [p for p in registry["projects"] if p.get("auto_evolve")]
    print(f"Wave 0 active cells: {len(active)}")

    if args.dry_run or not args.execute:
        print("DRY RUN: no agent processes launched; no repos mutated.")
        return 0

    workspace = pathlib.Path(
        os.environ.get("FRONTIER_WORKSPACE", pathlib.Path.home() / "src")
    )
    agents = [a.strip() for a in args.agents.split(",") if a.strip()]
    jobs = []

    # Wave 0 uses already-present local checkouts; it never clones automatically.
    for project in active:
        owner, name = project["repo"].split("/", 1)
        candidates = [workspace / name, workspace / owner / name]
        cwd = next((x for x in candidates if (x / ".git").exists()), None)
        if not cwd:
            print(f"SKIP {project['repo']}: no local checkout under {workspace}")
            continue
        capsule = capsule_for(project)
        for agent in agents:
            jobs.append((agent, capsule, cwd))

    out = ART / "wave0" / "lanes"
    out.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=min(args.max_parallel, 8)) as executor:
        futures = {executor.submit(run_lane, *job): job for job in jobs}
        for future in as_completed(futures):
            result = future.result()
            directory = out / result["task_id"]
            directory.mkdir(parents=True, exist_ok=True)
            (directory / (result["agent"] + ".json")).write_text(
                json.dumps(result, indent=2) + "\n"
            )
            print(result["status"], result["repo"], result["agent"])

    print("No merge performed. Review lane artifacts before any implementation wave.")
    return 0


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor")
    wave = sub.add_parser("wave0")
    wave.add_argument("--dry-run", action="store_true")
    wave.add_argument("--execute", action="store_true")
    wave.add_argument("--agents", default="codex,gemini")
    wave.add_argument("--max-parallel", type=int, default=4)
    args = parser.parse_args()
    return doctor() if args.cmd == "doctor" else wave0(args)


if __name__ == "__main__":
    raise SystemExit(main())
