"""
Pure business logic for Markdown metrics and table generation.
Zero Streamlit or UI dependencies.
"""

from typing import Dict, Any, List


def generate_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """Generates standard GitHub Flavored Markdown (GFM) table syntax."""
    if not headers:
        return ""

    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"

    row_lines = []
    for row in rows:
        # Pad row with empty cells if row is shorter than headers
        padded_row = row + [""] * (len(headers) - len(row))
        row_lines.append("| " + " | ".join(padded_row[:len(headers)]) + " |")

    return "\n".join([header_line, separator_line] + row_lines)


def analyze_markdown_structure(content: str) -> Dict[str, Any]:
    """Analyzes Markdown document headings, links, and words."""
    lines = content.splitlines()
    headings = [l for l in lines if l.strip().startswith("#")]
    links = [l for l in lines if "[" in l and "](" in l]
    word_count = len(content.split()) if content else 0

    return {
        "heading_count": len(headings),
        "link_count": len(links),
        "word_count": word_count,
        "line_count": len(lines),
    }
