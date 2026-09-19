#!/usr/bin/env python3
"""
Batch convert PDFs to Markdown using PyMuPDF4LLM.

Usage:
    python scripts/pdf_to_md_pymupdf4llm.py \
        --input-dir papers/raw \
        --output-dir papers/markdown \
        --recursive

Optional:
    --write-images       Extract images into a sibling image directory.
    --page-separators    Insert page separators in Markdown.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import traceback

import pymupdf4llm


def convert_pdf_to_markdown(
    pdf_path: Path,
    output_path: Path,
    write_images: bool = False,
    page_separators: bool = True,
    show_progress: bool = False,
) -> dict:
    """Convert one PDF file to Markdown using PyMuPDF4LLM."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    image_path = ""
    if write_images:
        image_dir = output_path.parent / f"{output_path.stem}_images"
        image_dir.mkdir(parents=True, exist_ok=True)
        image_path = str(image_dir)

    md_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        write_images=write_images,
        image_path=image_path,
        page_separators=page_separators,
        show_progress=show_progress,
    )

    if not isinstance(md_text, str):
        raise TypeError(
            f"Expected Markdown string from pymupdf4llm.to_markdown(), "
            f"got {type(md_text)}"
        )

    header = (
        f"# {pdf_path.stem}\n\n"
        f"- Source file: `{pdf_path.as_posix()}`\n"
        f"- Converter: `pymupdf4llm.to_markdown`\n\n"
        "---\n\n"
    )

    output_path.write_text(header + md_text, encoding="utf-8")

    return {
        "pdf": pdf_path.as_posix(),
        "markdown": output_path.as_posix(),
        "chars": len(md_text),
        "write_images": write_images,
        "image_path": image_path,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-dir",
        default="papers/raw",
        help="Directory containing PDF files.",
    )
    parser.add_argument(
        "--output-dir",
        default="papers/markdown",
        help="Directory for Markdown outputs.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively search for PDF files.",
    )
    parser.add_argument(
        "--write-images",
        action="store_true",
        help="Extract images referenced by the Markdown output.",
    )
    parser.add_argument(
        "--no-page-separators",
        action="store_true",
        help="Disable page separators in Markdown.",
    )
    parser.add_argument(
        "--show-progress",
        action="store_true",
        help="Show PyMuPDF4LLM conversion progress.",
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    pattern = "**/*.pdf" if args.recursive else "*.pdf"
    pdf_files = sorted(input_dir.glob(pattern))

    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    print(f"Found {len(pdf_files)} PDF file(s).")

    ok_count = 0
    failed_count = 0

    for pdf_path in pdf_files:
        relative_path = pdf_path.relative_to(input_dir)
        output_path = output_dir / relative_path.with_suffix(".md")

        try:
            info = convert_pdf_to_markdown(
                pdf_path=pdf_path,
                output_path=output_path,
                write_images=args.write_images,
                page_separators=not args.no_page_separators,
                show_progress=args.show_progress,
            )

            ok_count += 1
            print(
                f"[OK] {info['pdf']} -> {info['markdown']} "
                f"(chars={info['chars']})"
            )

        except Exception as exc:
            failed_count += 1
            print(f"[FAILED] {pdf_path}: {exc}")
            traceback.print_exc()

    print()
    print(f"Done. OK={ok_count}, FAILED={failed_count}")


if __name__ == "__main__":
    main()
