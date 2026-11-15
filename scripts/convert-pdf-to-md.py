#!/usr/bin/env python3
"""Convert PDF files to Markdown format."""

import sys
from pathlib import Path
from PyPDF2 import PdfReader


def pdf_to_md(pdf_path: str) -> str:
    """Convert a PDF to Markdown text."""
    reader = PdfReader(pdf_path)
    md_lines = []
    
    for page_num, page in enumerate(reader.pages, start=1):
        md_lines.append(f"# Page {page_num}")
        
        # Get page text
        text = page.extract_text() or ""
        
        if text.strip():
            md_lines.append(text)
            md_lines.append("")  # blank line between pages
        else:
            md_lines.append(f"[Page {page_num} is blank]")
            md_lines.append("")
    
    return "\n".join(md_lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert-pdf-to-md.py <input.pdf> [output.md]")
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf_path.with_suffix(".md")
    
    md_content = pdf_to_md(str(pdf_path))
    
    # Write to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"Converted {pdf_path} -> {output_path}")
