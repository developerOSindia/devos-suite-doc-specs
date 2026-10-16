"""
Unit tests for suite-doc-specs Markdown parser.
"""

import sys
import unittest
from pathlib import Path

SUITE_ROOT = Path(__file__).resolve().parent.parent
if str(SUITE_ROOT) not in sys.path:
    sys.path.insert(0, str(SUITE_ROOT))

from core.markdown_parser import generate_markdown_table, analyze_markdown_structure, generate_heading_slug


class TestMarkdown(unittest.TestCase):
    def test_table_generation(self):
        headers = ["Tool Name", "Category", "Status"]
        rows = [
            ["DevUtils", "Utilities", "Active"],
            ["API Sentinel", "Testing", "Active"],
        ]
        table = generate_markdown_table(headers, rows)
        self.assertIn("| Tool Name | Category | Status |", table)
        self.assertIn("| --- | --- | --- |", table)
        self.assertIn("| DevUtils | Utilities | Active |", table)

    def test_table_with_pipe_escaping(self):
        headers = ["Field | Alt", "Value"]
        rows = [["col | 1", "val"]]
        table = generate_markdown_table(headers, rows)
        self.assertIn(r"Field \| Alt", table)
        self.assertIn(r"col \| 1", table)

    def test_table_unequal_columns(self):
        headers = ["Col1", "Col2", "Col3"]
        rows = [["Only One"]]
        table = generate_markdown_table(headers, rows)
        self.assertIn("| Only One |  |  |", table)

    def test_empty_table(self):
        table = generate_markdown_table([], [])
        self.assertEqual(table, "")

    def test_analyze_structure(self):
        doc = """# DeveloperOS Documentation
## Getting Started
Welcome to the ecosystem. Visit [DeveloperOS](https://developeros.in).

```python
def hello():
    print("world")
```
"""
        metrics = analyze_markdown_structure(doc)
        self.assertEqual(metrics["heading_count"], 2)
        self.assertEqual(metrics["link_count"], 1)
        self.assertEqual(metrics["code_block_count"], 1)
        self.assertGreater(metrics["word_count"], 5)

    def test_analyze_empty_document(self):
        metrics = analyze_markdown_structure("")
        self.assertEqual(metrics["heading_count"], 0)
        self.assertEqual(metrics["link_count"], 0)
        self.assertEqual(metrics["word_count"], 0)

    def test_heading_slug_generator(self):
        slug1 = generate_heading_slug("Getting Started with DeveloperOS!")
        self.assertEqual(slug1, "getting-started-with-developeros")
        slug2 = generate_heading_slug("API & Network Suite (v2.0)")
        self.assertEqual(slug2, "api-network-suite-v20")


if __name__ == "__main__":
    unittest.main()
