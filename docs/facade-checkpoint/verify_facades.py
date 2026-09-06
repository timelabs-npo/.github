#!/usr/bin/env python3
"""verify_facades.py — local, read-only publication verification helper.

Reads baselines.json (15 repo/README targets) and validates, without ever
writing to any repo:

  * every README has balanced ``` fences
  * every relative markdown/HTML link (and img/href) resolves to a real file
  * `git diff --check` is clean (run with cwd = the actual repo checkout)
  * the set of changed paths in each repo matches a fixed allowlist
  * for Blueshoes docs/index.html and docs/rhea/index.html: local hrefs/srcs
    resolve (site-root "/" paths resolve into docs/, and routes declared in
    docs/_redirects are recognized), element ids are unique per file, and
    docs/rhea/index.html references exactly 15 distinct
    github.com/timelabs-npo/<repo> URLs.

Writes verification.json next to this script. Exits 1 if any error was
found, 0 otherwise. This tool never edits repos, never reads private
source-analysis/dialogue files, and never commits/pushes/deploys/touches
secrets — it only reads what baselines.json points at plus files those
targets link to.
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASELINES = ROOT / "baselines.json"
OUT = ROOT / "verification.json"

FENCE_RE = re.compile(r"```")
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"')
ID_RE = re.compile(r'\bid="([^"]+)"')
REPO_URL_RE = re.compile(r"github\.com/timelabs-npo/[A-Za-z0-9_.-]+")

SATELLITE_ALLOW = {"README.md"}
ALLOWLISTS = {
    "timelabs-npo/Blueshoes": {
        "README.md",
        "docs/index.html",
        "docs/rhea/index.html",
        "docs/DOMAIN_PLAYBOOK.md",
        "docs/_redirects",
    },
    "timelabs-npo/.github": {
        "profile/README.md",
        "docs/FACADE_WORK_MAP.md",
        "docs/FACADE_PATTERN.md",
        "docs/FACADE_RECEIPT.md",
    },
}


def is_external(link: str) -> bool:
    if not link or link.startswith("#"):
        return True
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link))


def strip_anchor(link: str) -> str:
    return link.split("#", 1)[0]


def check_fences(text: str):
    return [] if len(FENCE_RE.findall(text)) % 2 == 0 else ["unbalanced ``` fence count"]


def check_links(md_path: Path, text: str, errors: list):
    base_dir = md_path.parent
    links = MD_LINK_RE.findall(text) + HTML_ATTR_RE.findall(text)
    for raw in links:
        if is_external(raw):
            continue
        target = strip_anchor(raw)
        if not target:
            continue
        candidate = (base_dir / target).resolve()
        if not candidate.exists():
            errors.append(f"{md_path}: broken relative link -> {raw}")


def allowed_changed_paths(repo: str) -> set:
    if repo in ALLOWLISTS:
        return ALLOWLISTS[repo]
    return SATELLITE_ALLOW


def git(cwd: Path, *args):
    return subprocess.run(
        ["git", *args], cwd=str(cwd), capture_output=True, text=True
    )


def resolve_site_link(raw: str, html_path: Path, site_root: Path, redirects: dict, errors: list, label: str):
    if is_external(raw):
        return
    target = strip_anchor(raw)
    if not target:
        return
    if target.startswith("/"):
        rel = target.lstrip("/")
        if rel == "" or rel.endswith("/"):
            # route-style path; a directory index or a declared redirect
            # both count as resolved
            index_candidate = (site_root / rel / "index.html").resolve()
            if index_candidate.exists():
                return
            route = "/" + rel.rstrip("/")
            if route in redirects:
                return
            errors.append(f"{label}: unresolved site route {raw}")
            return
        candidate = (site_root / rel).resolve()
        if candidate.exists():
            return
        route = "/" + rel
        if route in redirects:
            return
        errors.append(f"{label}: broken site-root link -> {raw}")
    else:
        candidate = (html_path.parent / target).resolve()
        if not candidate.exists():
            errors.append(f"{label}: broken relative link -> {raw}")


def parse_redirects(redirects_path: Path) -> dict:
    table = {}
    if not redirects_path.exists():
        return table
    for line in redirects_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            table[parts[0]] = parts[1]
    return table


def check_ids_unique(html_path: Path, text: str, errors: list):
    ids = ID_RE.findall(text)
    seen = set()
    for i in ids:
        if i in seen:
            errors.append(f"{html_path}: duplicate id={i!r}")
        seen.add(i)


def verify_blueshoes_html(checkout: Path, errors: list, report: dict):
    docs = checkout / "docs"
    redirects = parse_redirects(docs / "_redirects")
    for rel in ("index.html", "rhea/index.html"):
        html_path = docs / rel
        if not html_path.exists():
            errors.append(f"missing Blueshoes HTML target: {rel}")
            continue
        text = html_path.read_text(encoding="utf-8", errors="replace")
        check_ids_unique(html_path, text, errors)
        for raw in sorted(set(HTML_ATTR_RE.findall(text))):
            resolve_site_link(raw, html_path, docs, redirects, errors, str(html_path))
        if rel == "rhea/index.html":
            urls = set(REPO_URL_RE.findall(text))
            report["rhea_repo_url_count"] = len(urls)
            report["rhea_repo_urls"] = sorted(urls)
            if len(urls) != 15:
                errors.append(
                    f"docs/rhea/index.html: expected 15 distinct timelabs-npo repo URLs, found {len(urls)}"
                )


def main():
    baselines = json.loads(BASELINES.read_text(encoding="utf-8"))
    report = {"repos": [], "errors": []}
    any_error = False

    for entry in baselines:
        repo = entry["repo"]
        checkout = Path(entry["checkout"])
        target = entry["target"]
        repo_report = {"repo": repo, "target": target, "errors": []}
        errs = repo_report["errors"]

        readme_path = checkout / target
        if not readme_path.exists():
            errs.append(f"target file missing on disk: {target}")
        else:
            text = readme_path.read_text(encoding="utf-8", errors="replace")
            errs.extend(f"{target}: {e}" for e in check_fences(text))
            link_errs = []
            check_links(readme_path, text, link_errs)
            errs.extend(link_errs)

        # git diff --check, run with cwd = actual repo checkout
        if (checkout / ".git").exists():
            diffcheck = git(checkout, "diff", "--check")
            if diffcheck.returncode not in (0, 1):
                errs.append(f"git diff --check failed to run: {diffcheck.stderr.strip()}")
            elif diffcheck.stdout.strip():
                errs.append("git diff --check reported issues:\n" + diffcheck.stdout.strip())

            status = git(checkout, "status", "--porcelain", "-uall")
            changed = []
            for line in status.stdout.splitlines():
                path = line[3:].strip()
                changed.append(path)
            allow = allowed_changed_paths(repo)
            disallowed = [p for p in changed if p not in allow]
            repo_report["changed_paths"] = changed
            if disallowed:
                errs.append(f"changed paths outside allowlist: {disallowed}")
        else:
            errs.append("not a git checkout (no .git); skipped diff/status checks")

        if repo == "timelabs-npo/Blueshoes":
            verify_blueshoes_html(checkout, errs, repo_report)

        if errs:
            any_error = True
        report["repos"].append(repo_report)

    report["ok"] = not any_error
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 1 if any_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
