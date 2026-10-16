# Stretch - agents, automation, migration
# Co-authored with CoCo
import streamlit as st

import sample_data as D
from ui import capability, explanations, footer, prompt, result_label, snowsight, sql_steps, what_why

P = "stretch"
st.title("Stretch: agents, automation and migration")
capability("A Cortex Agent over `SV_OPERATOR_KPIS` (the Nova pattern), a scheduled data quality digest, and "
           "reconciliation checks for a migrated operator.",
           "After Session 5, if time allows", "`CREATE AGENT` succeeds in your operator schema")
what_why(P)

st.divider()
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: the agent's answer")
result_label("Captured from a real run (Cortex Agent via DATA_AGENT_RUN)")
with st.chat_message("user"):
    st.markdown(D.AGENT_QUESTION)
with st.chat_message("assistant", avatar=":material/smart_toy:"):
    st.markdown(D.AGENT_ANSWER)
    if D.AGENT_USED_VERIFIED_QUERY:
        st.caption(":material/verified: Answered from the verified query `vq_active_members`")
st.warning(f"The dashboard (status-based metric) said **{D.S1_TWO_ACTIVE[0]['ACTIVE_MEMBERS']:,}**; the agent says "
           f"**{D.S1_TWO_ACTIVE[0]['PAID_MEMBERS_35D']:,}**. Both are right for their definition - this is the discrepancy "
           "operators ring Customer Success about.", icon=":material/compare_arrows:")
explanations(P)

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.divider()
prompt(P, 2)
sql_steps(P, "Agent definition (what CoCo generates)")
footer(P)
