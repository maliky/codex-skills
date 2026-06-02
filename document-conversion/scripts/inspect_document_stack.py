#!/usr/bin/env python3
"""Inspect document-conversion inputs and available local conversion tools."""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from pathlib import Path
from typing import Any


TOOLS = ("pandoc", "soffice", "libreoffice", "pdflatex", "lualatex", "xelatex", "mutool", "pdfinfo", "unzip", "zip")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect source format and conversion-tool availability.")
    parser.add_argument("source", help="Source document path.")
    parser.add_argument("--target", default="", help="Optional target format such as docx, odt, pdf, org, or tex.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def text_signals(path: Path) -> dict[str, int | bool]:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}
    return {
        "headings": text.count("\n* ") + int(text.startswith("* ")),
        "latex_commands": text.count("\\"),
        "org_tables": text.count("\n|"),
        "raw_latex_blocks": text.count("#+BEGIN_EXPORT latex") + text.count("#+begin_export latex"),
        "has_title": "#+TITLE:" in text.upper() or "\\title{" in text,
        "has_bibliography": "bibliography" in text.lower() or "\\cite" in text,
    }


def zip_signals(path: Path) -> dict[str, Any]:
    if path.suffix.lower() not in {".docx", ".odt"} or not zipfile.is_zipfile(path):
        return {}
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    return {
        "zip_entries": len(names),
        "has_word_document": "word/document.xml" in names,
        "has_content_xml": "content.xml" in names,
        "media_files": sum(1 for name in names if "/media/" in name or name.startswith("Pictures/")),
        "style_files": [name for name in names if "style" in name.lower()][:10],
    }


def inspect(path: Path, target: str) -> dict[str, Any]:
    suffix = path.suffix.lower().lstrip(".")
    return {
        "source": str(path),
        "exists": path.exists(),
        "suffix": suffix,
        "target": target,
        "size_bytes": path.stat().st_size if path.exists() else None,
        "tools": {tool: shutil.which(tool) for tool in TOOLS},
        "text_signals": text_signals(path) if path.exists() and suffix in {"org", "tex", "txt", "md"} else {},
        "archive_signals": zip_signals(path) if path.exists() else {},
    }


def print_text(data: dict[str, Any]) -> None:
    print(f"source: {data['source']}")
    print(f"exists: {data['exists']}")
    print(f"suffix: {data['suffix']}")
    print(f"target: {data['target'] or '<unspecified>'}")
    print(f"size_bytes: {data['size_bytes']}")
    print("tools:")
    for tool, path in data["tools"].items():
        print(f"  {tool}: {path or '<missing>'}")
    if data["text_signals"]:
        print("text_signals:")
        for key, value in data["text_signals"].items():
            print(f"  {key}: {value}")
    if data["archive_signals"]:
        print("archive_signals:")
        for key, value in data["archive_signals"].items():
            print(f"  {key}: {value}")


def main() -> int:
    args = parse_args()
    data = inspect(Path(args.source).expanduser(), args.target.lower())
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print_text(data)
    return 0 if data["exists"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
