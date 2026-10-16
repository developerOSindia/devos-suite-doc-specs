"""
Pure business logic for Markdown metrics and table generation.
Zero Streamlit or UI dependencies.
"""

import re
from typing import Dict, Any, List


def generate_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """Generates standard GitHub Flavored Markdown (GFM) table syntax."""
    if not headers:
        return ""

    safe_headers = [str(h).strip().replace("|", "\\|") for h in headers]
    header_line = "| " + " | ".join(safe_headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"

    row_lines = []
    for row in (rows or []):
        padded_row = [str(cell).strip().replace("|", "\\|") for cell in row] + [""] * (len(headers) - len(row))
        row_lines.append("| " + " | ".join(padded_row[:len(headers)]) + " |")

    return "\n".join([header_line, separator_line] + row_lines)


def analyze_markdown_structure(content: str) -> Dict[str, Any]:
    """Analyzes Markdown document headings, links, and words."""
    safe_content = content or ""
    lines = safe_content.splitlines()
    headings = [l for l in lines if l.strip().startswith("#")]
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", safe_content)
    code_blocks = re.findall(r"```([a-zA-Z0-9_-]*)\n(.*?)```", safe_content, flags=re.DOTALL)
    word_count = len(safe_content.split()) if safe_content else 0

    return {
        "heading_count": len(headings),
        "link_count": len(links),
        "code_block_count": len(code_blocks),
        "word_count": word_count,
        "line_count": len(lines),
        "character_count": len(safe_content),
    }


def generate_heading_slug(text: str) -> str:
    """Generates standard GitHub markdown anchor slug from heading text."""
    clean = re.sub(r"[^\w\s-]", "", (text or "").lower())
    return re.sub(r"[\s_-]+", "-", clean).strip("-")
