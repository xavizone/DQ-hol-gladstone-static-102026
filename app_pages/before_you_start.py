# Before you start - attendee prep (same text as ATTENDEE_PREP.md)
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

from ui import footer

PREP = (Path(__file__).parent.parent / "ATTENDEE_PREP.md").read_text()

st.title("Before you start")
st.info("""**For attendees.** What to do the day before, what to know, and what to expect in the 30 minutes.

**Download** the same content as a one-page sheet below.""", icon=":material/event_available:")
st.download_button("Download ATTENDEE_PREP.md", data=PREP, file_name="ATTENDEE_PREP.md", mime="text/markdown",
                   icon=":material/download:")

sections = {}
for chunk in PREP.split("\n## ")[1:]:
    head, _, body = chunk.partition("\n")
    sections[head.strip()] = body
tabs = st.tabs([":material/checklist: Things to do", ":material/info: Things to know", ":material/schedule: What to expect"])
for tab, name in zip(tabs, ["Things to do", "Things to know", "What to expect"]):
    with tab, st.container(border=True):
        st.markdown(sections.get(name, ""))

st.markdown("### Getting started on the day")
st.markdown("""
1. In CoCo, connect to `GLADSTONESOFTWARE`, then set role **`DQ_LAB_<NAME>`** and warehouse **`DQ_LAB_WH`**.
2. Paste (with your name): `Confirm my current role, warehouse and that I can see schema GLADSTONE_DQ_LAB.CUST_<NAME>. List the tables, dynamic tables and tasks in it.`
3. You should see 8 Bronze tables, 3 `REPORTING__*` dynamic tables, task `TSK_BIFROST_MERGE` (started) and semantic view `SV_OPERATOR_KPIS`.
""")
footer("before_you_start")
