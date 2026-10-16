# Session 4 - Contain and alert
# Co-authored with CoCo
import streamlit as st

import sample_data as D
from snippets import PAGES
from ui import (capability, checkpoints, expectations_table, explanations, footer, header, prompt, result_label,
                snowsight, sql_steps, table, tech, what_why)

P = "session_04"
header(P)
capability("A **circuit breaker** task that freezes REPORTING Dynamic Tables while any Bronze expectation is "
           "violated and resumes them when clean, plus per-check data quality notifications.",
           "Session 4 (6 min)", "`ALTER DYNAMIC TABLE ... SUSPEND` and `SYSTEM$SET_RETURN_VALUE` run in a task")
what_why(P)

st.divider()
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: the breaker opens, then closes")
result_label("Captured from a real run - OPEN on CUST_RAJ (refund sign flip), CLOSED on CUST_NIELS after the fix")
state = st.segmented_control("Breaker state", ["Fault present", "After the fix"], default="Fault present", key="cb_state") or "Fault present"
if state == "Fault present":
    run = D.S4_CB_OPEN[0]
    st.error(f"**{run['RETURN_VALUE']}**", icon=":material/block:")
    table(D.S4_CB_OPEN)
    st.markdown("REPORTING Dynamic Tables frozen at their last good state:")
    table(D.S4_DTS_OPEN)
else:
    closed = [r for r in D.S4_CB_CLOSED if r["RETURN_VALUE"]]
    st.success(f"**{closed[0]['RETURN_VALUE']}**", icon=":material/check_circle:")
    table(closed)
    st.markdown("REPORTING Dynamic Tables running again:")
    table(D.S4_DTS_CLOSED)
st.caption("The task records its decision with `SYSTEM$SET_RETURN_VALUE`. Build the message in a variable first - "
           "passing an expression such as `'OPEN: ' || :bad` fails the task run.")

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: fix the data, prove it")
result_label()
c1, c2 = st.columns([1, 3])
c1.metric("Replayed rows removed", f"{D.S4_FIX_COUNT[0]['ROWS_REMOVED']:,}", help="DELETE ... WHERE _batch_id = 'B-REPLAY-01'")
with c2:
    st.markdown("`MEMBERS__MEMBER` expectations after the fix:")
    expectations_table(D.S4_AFTER_FIX_EVAL)

checkpoints(P)
built = PAGES[P].get("built", [])
if built:
    st.markdown("##### :material/check_circle: What you built")
    for b in built:
        st.markdown(f"- :green-badge[Done] {b}")
explanations(P)
tech(P)
sql_steps(P)
footer(P)
