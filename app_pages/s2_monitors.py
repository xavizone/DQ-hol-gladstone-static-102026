# Session 2 - Put monitors on it
# Co-authored with CoCo
import json

import streamlit as st

import story

import sample_data as D
from snippets import PAGES
from ui import (capability, checkpoints, expectations_table, explanations, footer, header, prompt, result_label,
                snowsight, sql_steps, table, tech, what_why)

P = "session_02"
header(P)
story.chapter(2)
capability("Data metric functions (system and custom) on a schedule, with **expectations** - the invariants that "
           "must always hold - and anomaly detection as the long-term safety net. Serverless, inside Snowflake.",
           "Session 2 (7 min)", "`SHOW DATA METRIC FUNCTIONS IN SCHEMA SNOWFLAKE.CORE` lists NEGATIVE_COUNT and REFERENTIAL_INTEGRITY_COUNT")
what_why(P)

st.divider()
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: what got attached")
result_label()
rows = [{"METRIC": r["METRIC_NAME"],
         "COLUMNS": ", ".join(a["name"] for a in json.loads(r["REF_ARGUMENTS"])) or "(table)",
         "SCHEDULE": r["SCHEDULE"], "STATUS": r["SCHEDULE_STATUS"]} for r in D.S2_ATTACHED]
st.markdown("**On `MEMBERS__MEMBER`** (`DATA_METRIC_FUNCTION_REFERENCES`)")
table(rows)

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: every expectation passes on clean data")
result_label("Captured from a real run, before any fault")
clean = D.S2_CLEAN_MEMBERS__MEMBER + D.S2_CLEAN_SYSTEM__PAYMENT + D.S2_CLEAN_SYSTEM__ATTENDANCE
c1, c2 = st.columns([1, 3])
c1.metric("Expectations evaluated", len(clean), help="Single-table expectations; the REPORTING lag check runs on its schedule")
c1.metric("Violated", sum(1 for r in clean if r["EXPECTATION_VIOLATED"]))
with c2:
    expectations_table(clean)
st.caption("`SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS` runs the checks now instead of waiting for the 5-minute schedule. "
           "The seventh expectation, `reporting_within_5min` on `REPORTING__DAILY_REVENUE`, compares two tables and runs on its schedule.")

checkpoints(P)
story.turn(2)
concepts = PAGES[P].get("concepts", [])
if concepts:
    st.markdown("##### :material/lightbulb: Key concepts")
    for c in concepts:
        with st.expander(f"**{c['term']}**"):
            st.markdown(c["definition"])
explanations(P)
tech(P)
sql_steps(P)
footer(P)
