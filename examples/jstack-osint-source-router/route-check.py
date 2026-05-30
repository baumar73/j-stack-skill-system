#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "sources" / "osint-sources.json"

REQUIRED_FIELDS = {
    "id", "name", "category", "jurisdiction", "url", "access", "automation",
    "license_tos", "data_types", "best_for", "caution", "personal_data_risk",
    "evidence_weight", "citation_note", "tags",
}
ALLOWED_RISK = {"low", "medium", "high"}
ALLOWED_WEIGHT = {"primary", "secondary", "index", "lead-only"}
ROUTE_TAGS = {
    "company-register",
    "procurement",
    "spending",
    "sanctions",
    "debarment",
    "archive",
}


def main() -> int:
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    sources = atlas["sources"]
    ids = [source["id"] for source in sources]
    errors: list[str] = []

    if len(sources) < 50:
        errors.append(f"expected at least 50 seed sources, got {len(sources)}")
    if len(ids) != len(set(ids)):
        errors.append("source ids are not unique")

    for source in sources:
        missing = REQUIRED_FIELDS - set(source)
        if missing:
            errors.append(f"{source.get('id', '<unknown>')}: missing {sorted(missing)}")
        if source.get("personal_data_risk") not in ALLOWED_RISK:
            errors.append(f"{source.get('id')}: invalid personal_data_risk")
        if source.get("evidence_weight") not in ALLOWED_WEIGHT:
            errors.append(f"{source.get('id')}: invalid evidence_weight")
        if source.get("personal_data_risk") == "high" and source.get("automation") == "bulk-download-ok":
            errors.append(f"{source.get('id')}: high personal-data risk cannot default to bulk-download-ok")

    routed = [
        source for source in sources
        if ROUTE_TAGS.intersection(source["tags"])
        and source["automation"] != "do-not-automate"
    ]
    routed.sort(key=lambda source: (
        source["evidence_weight"] != "primary",
        source["personal_data_risk"] == "high",
        source["id"],
    ))

    summary = {
        "atlas_version": atlas["version"],
        "source_count": len(sources),
        "category_count": len({source["category"] for source in sources}),
        "high_personal_data_risk_count": sum(1 for source in sources if source["personal_data_risk"] == "high"),
        "fictional_route": [source["id"] for source in routed[:14]],
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
