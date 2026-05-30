#!/usr/bin/env python3
"""Deterministic metadata check for the fictional SEO distribution example."""

SEO_TITLE = "Toy Data Story: Fictional Service Desk Hours"
META_DESCRIPTION = (
    "A J-Stack SEO example that packages a fictional service-hours dataset "
    "with truthful search intent, metadata, newsletter copy, and review gates."
)
SLUG = "toy-service-hours-data-story"
UNSAFE_TERMS = ["scandal", "failure", "exposed", "corruption", "denied access"]


def status(length: int, limit: int) -> str:
    return "PASS" if length <= limit else "FAIL"


def main() -> int:
    checks = [
        ("seo_title_chars", len(SEO_TITLE), 60),
        ("meta_description_chars", len(META_DESCRIPTION), 160),
        ("slug_chars", len(SLUG), 80),
    ]
    failed = False
    for name, length, limit in checks:
        result = status(length, limit)
        failed = failed or result != "PASS"
        print(f"{name}={length} limit={limit} status={result}")

    combined = " ".join([SEO_TITLE, META_DESCRIPTION, SLUG]).lower()
    hits = [term for term in UNSAFE_TERMS if term in combined]
    print(f"unsafe_terms_hits={hits}")
    failed = failed or bool(hits)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
