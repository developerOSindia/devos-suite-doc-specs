"""
DeveloperOS Documentation & Specs Suite - Interactive Application
"""

import streamlit as st
from core.markdown_parser import generate_markdown_table, analyze_markdown_structure
from ui.components import render_suite_header, render_suite_footer, render_main_promotional_banner

st.set_page_config(
    page_title="DeveloperOS - Docs Suite",
    page_icon="📝",
    layout="wide",
)


def main():
    render_suite_header(
        title="Markdown Editor & GFM Table Generator",
        description="Preview GitHub Flavored Markdown documents in real-time and generate formatted markdown tables with structural analytics.",
    )

    tab_preview, tab_table = st.tabs(["Markdown Live Preview", "GFM Table Builder"])

    with tab_preview:
        sample_md = """# DeveloperOS Project Overview
A unified ecosystem of **open-source developer tools** built for high productivity.

## Key Principles
- 🛡️ Zero-trust privacy & ephemeral processing
- 📦 Decoupled, independently deployable suites
- 🚀 Free-tier hosting on Cloudflare & Streamlit

Learn more at [DeveloperOS Official Site](https://developeros.in).
"""
        doc_input = st.text_area("Markdown Source:", value=sample_md, height=180)

        if doc_input:
            stats = analyze_markdown_structure(doc_input)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Headings", stats["heading_count"])
            col2.metric("Links", stats["link_count"])
            col3.metric("Words", stats["word_count"])
            col4.metric("Lines", stats["line_count"])

            st.divider()
            st.subheader("Rendered HTML Preview")
            st.markdown(doc_input)

    with tab_table:
        st.subheader("Generate Markdown Table")
        col_hdr = st.text_input("Headers (comma separated):", value="Suite ID, Name, Target Env")
        row1 = st.text_input("Row 1 (comma separated):", value="suite-web-craft, Web Craft, Streamlit")
        row2 = st.text_input("Row 2 (comma separated):", value="suite-api-network, API Network, Streamlit")

        if st.button("Generate GFM Table"):
            headers = [h.strip() for h in col_hdr.split(",") if h.strip()]
            rows = [
                [c.strip() for c in row1.split(",")],
                [c.strip() for c in row2.split(",")],
            ]
            table_md = generate_markdown_table(headers, rows)
            st.code(table_md, language="markdown")

    render_main_promotional_banner()
    render_suite_footer()


if __name__ == "__main__":
    main()
