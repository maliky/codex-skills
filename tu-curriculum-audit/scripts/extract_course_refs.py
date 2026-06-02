#!/usr/bin/env python3
"""Extract candidate course references from text-like curriculum sources."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


COURSE_RE = re.compile(r"\b([A-Z]{2,6})\s*[- ]?\s*(\d{3,4}[A-Z]?)\b")
FALSE_PREFIXES = {"ISBN", "HTTP", "HTTPS", "PAGE"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract candidate TU course references.")
    parser.add_argument("source", help="Text, Org, Markdown, TeX, or XML-ish source file.")
    parser.add_argument("--tsv", help="Write TSV output to this path. Defaults to stdout.")
    return parser.parse_args()


def normalize(prefix: str, number: str) -> str:
    return f"{prefix.upper()} {number.upper()}"


def iter_refs(path: Path):
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line_no, line in enumerate(handle, start=1):
            for match in COURSE_RE.finditer(line):
                prefix = match.group(1).upper()
                number = match.group(2).upper()
                if prefix in FALSE_PREFIXES:
                    continue
                yield {
                    "line": line_no,
                    "raw": match.group(0),
                    "code": normalize(prefix, number),
                    "prefix": prefix,
                    "number": number,
                    "context": line.strip(),
                }


def write_rows(rows: list[dict[str, str | int]], output: Path | None) -> None:
    fieldnames = ["line", "raw", "code", "prefix", "number", "context"]
    handle = output.open("w", encoding="utf-8", newline="") if output else sys.stdout
    close = output is not None
    try:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    finally:
        if close:
            handle.close()


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser()
    if not source.exists():
        print(f"Error: source not found: {source}", file=sys.stderr)
        return 1
    rows = list(iter_refs(source))
    write_rows(rows, Path(args.tsv).expanduser() if args.tsv else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
