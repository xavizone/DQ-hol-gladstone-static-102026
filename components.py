# Compatibility shim so reference pages copied from the live guide render unchanged in the static app
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

SQL_DIR = Path(__file__).resolve().parent / "sql"
CTX = {"NAME": "NIELS", "SCHEMA": "CUST_NIELS", "FQ_SCHEMA": "GLADSTONE_DQ_LAB.CUST_NIELS",
       "ROLE": "DQ_LAB_NIELS", "DB": "GLADSTONE_DQ_LAB", "WH": "DQ_LAB_WH"}


def ctx() -> dict:
    return dict(CTX)


def fill(text: str) -> str:
    for k, v in CTX.items():
        text = text.replace("{" + k + "}", v)
    return text


def sql_file(rel_path: str) -> str:
    return (SQL_DIR / rel_path).read_text()


def render_sql_file(rel_path: str, label: str | None = None, expanded: bool = False):
    with st.expander(label or f":material/description: `{rel_path}`", expanded=expanded):
        st.code(sql_file(rel_path), language="sql", line_numbers=True)


def render_real_world_examples(items: list[dict]):
    st.divider()
    with st.expander(":material/apartment: Real-world use cases at Gladstone", expanded=False):
        for it in items:
            st.markdown(f"- **{it['title']}** - {it['body']}")


def render_references(links: dict):
    from links import VERIFIED_ON

    st.markdown("##### :material/menu_book: References")
    for group, items in links.items():
        if not items:
            continue
        st.markdown(f"**{group}**")
        for title, url, note in items:
            st.markdown(f"- [{title}]({url})" + (f" - {note}" if note else ""))
    st.caption(f"Links verified {VERIFIED_ON}.")
