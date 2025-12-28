from __future__ import annotations

import re
from pathlib import Path

import bibtexparser
from slugify import slugify
import yaml


# =========================
# CONFIG
# =========================
BIB_PATH = Path("../authors/Sangdon Park/papers.bib")  # input BibTeX
OUT_DIR = Path(".")                                   # output bundles (current dir)


# =========================
# HELPERS
# =========================
def clean_latex(s: str) -> str:
    if not s:
        return ""
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\\&", "&", s)
    return s.strip()


def parse_authors(author_field: str) -> list[str]:
    if not author_field:
        return []
    authors: list[str] = []
    for a in author_field.split(" and "):
        a = a.strip()
        if "," in a:
            last, first = a.split(",", 1)
            authors.append(f"{first.strip()} {last.strip()}")
        else:
            authors.append(a)
    return authors


def guess_date(entry: dict) -> str:
    raw_date = (entry.get("date") or "").strip()
    if raw_date:
        m = re.match(r"^\s*(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?\s*$", raw_date)
        if m:
            y = int(m.group(1))
            mm = int(m.group(2) or 1)
            dd = int(m.group(3) or 1)
            mm = max(1, min(12, mm))
            dd = max(1, min(31, dd))
            return f"{y:04d}-{mm:02d}-{dd:02d}"

    def first_int(s: str) -> int | None:
        m = re.search(r"\d+", s or "")
        return int(m.group(0)) if m else None

    year = first_int((entry.get("year") or "").strip())
    if not year:
        return "2000-01-01"

    month_raw = (entry.get("month") or "").strip().lower()
    day_raw = (entry.get("day") or "").strip()

    month_map = {
        "jan": 1, "january": 1,
        "feb": 2, "february": 2,
        "mar": 3, "march": 3,
        "apr": 4, "april": 4,
        "may": 5,
        "jun": 6, "june": 6,
        "jul": 7, "july": 7,
        "aug": 8, "august": 8,
        "sep": 9, "september": 9,
        "oct": 10, "october": 10,
        "nov": 11, "november": 11,
        "dec": 12, "december": 12,
    }

    mm = first_int(month_raw)
    if mm is None:
        mm = month_map.get(month_raw, 1)
    mm = max(1, min(12, mm))

    dd = first_int(day_raw) or 1
    dd = max(1, min(31, dd))

    return f"{year:04d}-{mm:02d}-{dd:02d}"


def publication_venue(entry: dict) -> str:
    for k in ("booktitle", "journal", "publisher"):
        v = entry.get(k)
        if v:
            return clean_latex(v)
    return ""


def publication_nickname(entry: dict) -> str:
    for k in ("nickname", "shortbooktitle", "shorttitle", "venue"):
        v = entry.get(k)
        if v:
            return clean_latex(v)
    return ""


def publication_type(entry: dict) -> list[str]:
    if entry.get("booktitle"):
        return ["1"]  # conference
    if entry.get("journal"):
        return ["2"]  # journal
    return ["0"]      # other


def build_links(entry: dict) -> list[dict]:
    links: list[dict] = []

    doi = (entry.get("doi") or "").strip()
    url = (entry.get("url") or "").strip()

    arxiv = (entry.get("eprint") or "").strip()
    archiveprefix = (entry.get("archiveprefix") or "").strip().lower()

    if archiveprefix == "arxiv" and arxiv:
        links.append({"name": "arXiv", "url": f"https://arxiv.org/abs/{arxiv}"})

    if doi:
        links.append({"name": "DOI", "url": f"https://doi.org/{doi}"})

    if url:
        if not (doi and url.lower().startswith("https://doi.org/")):
            links.append({"name": "URL", "url": url})

    pdf = (entry.get("pdf") or "").strip()
    code = (entry.get("code") or "").strip()
    project = (entry.get("project") or "").strip()

    if pdf:
        links.append({"name": "PDF", "url": pdf})
    if code:
        links.append({"name": "Code", "url": code})
    if project:
        links.append({"name": "Project", "url": project})

    seen = set()
    deduped: list[dict] = []
    for l in links:
        u = l.get("url", "")
        if u and u not in seen:
            seen.add(u)
            deduped.append(l)
    return deduped


def parse_highlight(entry: dict) -> str:
    """
    BibTeX `highlight` is a short note to show in text (badge/annotation).
    Examples: "Oral", "Best Paper", "Spotlight", "Invited"
    """
    raw = (entry.get("highlight") or "").strip()
    if not raw:
        return ""

    low = raw.lower()
    if low in {"0", "false", "no", "n", "off"}:
        return ""
    if low in {"1", "true", "yes", "y", "on", "*"}:
        return "Highlight"

    return clean_latex(raw)


# =========================
# MAIN
# =========================
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with BIB_PATH.open("r", encoding="utf-8") as f:
        bib = bibtexparser.load(f)

    for entry in bib.entries:
        title = clean_latex(entry.get("title", "untitled"))

        date = guess_date(entry)
        slug = f"{date}-{slugify(title)[:65]}"

        pub_dir = OUT_DIR / slug
        pub_dir.mkdir(parents=True, exist_ok=True)

        authors = parse_authors(entry.get("author", ""))
        venue_full = publication_venue(entry)
        venue_short = publication_nickname(entry)
        abstract = clean_latex(entry.get("abstract", ""))

        highlight = parse_highlight(entry)

        front_matter = {
            "title": title,
            "date": date,
            "authors": authors,
            "publication": venue_full,
            "publication_short": venue_short or None,
            "publication_types": publication_type(entry),
            "doi": (entry.get("doi") or "").strip() or None,
            "links": build_links(entry) or None,
            "highlight": highlight or None,  # ✅ text annotation
        }

        front_matter = {k: v for k, v in front_matter.items() if v not in (None, "", [])}

        index_md = pub_dir / "index.md"
        with index_md.open("w", encoding="utf-8") as out:
            out.write("---\n")
            out.write(yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True))
            out.write("---\n\n")
            if abstract:
                out.write(abstract + "\n")

        print(f"✓ {slug}")

    print("\nDone. Publications generated.")


if __name__ == "__main__":
    main()
