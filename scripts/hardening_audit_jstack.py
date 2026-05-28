#!/usr/bin/env python3
"""Deterministic hardening audit for the J-Stack skill pack.

This is intentionally read-only: it checks structure, safety-boundary language,
manifest consistency, and obvious secret/risky automation patterns.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

try:
    import yaml
except Exception:  # pragma: no cover - fallback for minimal environments
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".csv", ".py", ".txt", ".yml", ".yaml"}
REQUIRED_TOP_LEVEL = [
    "README.md",
    "ARCHITECTURE.md",
    "GBRAIN-INTEGRATION.md",
    "QUALITY-GATES.md",
    "QUALITY-REPORT.md",
    "PUBLICATION-READINESS.md",
    "MANIFEST.md",
    "MANIFEST.json",
    "CHECKPOINT.md",
    "VALIDATION.json",
    "LICENSE",
    "CONTRIBUTING.md",
]
REQUIRED_SKILL_SECTIONS = [
    "## Overview",
    "## When to Use",
    "## GBrain Integration",
    "## Legal and Ethical Boundaries",
    "## Common Pitfalls",
    "## Verification Checklist",
]
SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[A-Za-z0-9_\-]{12,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----"),
]
RISKY_PATTERNS = [
    re.compile(r"(?i)(publish|send|post|file) automatically"),
    re.compile(r"(?i)no approval needed"),
    re.compile(r"(?i)ignore legal"),
    re.compile(r"(?i)guaranteed safe"),
]
SAFE_NEGATIONS = ("do not", "never", "not ", "without explicit human approval")


def load_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        raise ValueError("missing frontmatter start")
    match = re.search(r"\n---\s*\n", text[3:])
    if not match:
        raise ValueError("missing frontmatter close")
    fm_text = text[3 : 3 + match.start()]
    if yaml:
        data = yaml.safe_load(fm_text)
        if not isinstance(data, dict):
            raise ValueError("frontmatter is not a mapping")
        return data
    data = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def add_issue(issues: list[dict], severity: str, path: str, issue: str) -> None:
    issues.append({"severity": severity, "path": path, "issue": issue})


def main() -> int:
    issues: list[dict] = []
    skills: list[dict] = []
    files = [p for p in ROOT.rglob("*") if p.is_file()]

    for required in REQUIRED_TOP_LEVEL:
        if not (ROOT / required).exists():
            add_issue(issues, "important", required, "missing top-level artifact")

    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        try:
            fm = load_frontmatter(text)
        except Exception as exc:
            add_issue(issues, "blocker", rel, f"frontmatter error: {exc}")
            continue
        body = text.split("\n---\n", 1)[1] if "\n---\n" in text else ""
        title = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), "")
        checks = {
            "human_approval": any(term in body.lower() for term in ["human approval", "explicit human approval", "user approval"]),
            "no_external_actions": "without explicit human approval" in body.lower() or "without human approval" in body.lower(),
            "gbrain": "GBrain" in body,
            "legal_ethics": "## Legal and Ethical Boundaries" in body,
        }
        for section in REQUIRED_SKILL_SECTIONS:
            if section not in body:
                add_issue(issues, "blocker", rel, f"missing required section: {section}")
        for key, value in checks.items():
            if not value:
                add_issue(issues, "important", rel, f"weak safety/structure signal: {key}")
        if title.startswith("Jstack") or "Gbrain" in title or " Osint " in title or " Seo " in title:
            add_issue(issues, "nit", rel, f"unpolished title casing: {title}")
        skills.append({"name": fm.get("name"), "path": rel, "title": title, "checks": checks})

    manifest_path = ROOT / "MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_names = {entry.get("name") for entry in manifest.get("skills", [])}
        skill_names = {entry.get("name") for entry in skills}
        if manifest_names != skill_names:
            add_issue(issues, "blocker", "MANIFEST.json", f"manifest skill mismatch: {sorted(manifest_names ^ skill_names)}")

    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = str(path.relative_to(ROOT))
        if rel in {"scripts/hardening_audit_jstack.py", "HARDENING-AUDIT.json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                add_issue(issues, "blocker", rel, "possible embedded secret pattern")
                break
        for lineno, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            if any(pattern.search(line) for pattern in RISKY_PATTERNS) and not any(marker in lowered for marker in SAFE_NEGATIONS):
                add_issue(issues, "important", rel, f"risky automation phrase on line {lineno}: {line.strip()}")
                break

    result = {
        "file_count": len(files),
        "skill_count": len(skills),
        "bundle_count": len(list((ROOT / "bundles").glob("*"))) if (ROOT / "bundles").exists() else 0,
        "template_count": len(list((ROOT / "templates").glob("*"))) if (ROOT / "templates").exists() else 0,
        "reference_count": len(list((ROOT / "references").glob("*"))) if (ROOT / "references").exists() else 0,
        "issues": issues,
        "issue_counts": {
            "blocker": sum(1 for i in issues if i["severity"] == "blocker"),
            "important": sum(1 for i in issues if i["severity"] == "important"),
            "nit": sum(1 for i in issues if i["severity"] == "nit"),
        },
        "skills": skills,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["issue_counts"]["blocker"] or result["issue_counts"]["important"] else 0


if __name__ == "__main__":
    sys.exit(main())
