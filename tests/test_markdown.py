"""
Unit tests for suite-doc-specs business logic.
"""

import sys
import unittest
from pathlib import Path

# Ensure suite root is in sys.path
SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.markdown_parser import generate_markdown_table, analyze_markdown_structure


class TestMarkdown(unittest.TestCase):
    def test_generate_table(self):
        headers = ["Tool", "Category", "Status"]
        rows = [
            ["curl-parser", "API", "Active"],
            ["hasher", "Security", "Active"],
        ]
        table = generate_markdown_table(headers, rows)
        self.assertIn("| Tool | Category | Status |", table)
        self.assertIn("| --- | --- | --- |", table)
        self.assertIn("| curl-parser | API | Active |", table)

    def test_analyze_structure(self):
        doc = "# Title\n\nSome text [link](https://developeros.in)\n## Subtitle\nMore text"
        metrics = analyze_markdown_structure(doc)
        self.assertEqual(metrics["heading_count"], 2)
        self.assertEqual(metrics["link_count"], 1)
        self.assertGreater(metrics["word_count"], 5)


if __name__ == "__main__":
    unittest.main()
