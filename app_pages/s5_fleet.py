# Session 5 - Fleet view across operators
# Co-authored with CoCo
import json

import pandas as pd
import streamlit as st

import story

import sample_data as D
from ui import (capability, checkpoints, explanations, footer, header, prompt, result_label, snowsight, sql_steps,
                tech, what_why)

P = "session_05"
LAB_OPS = {"CUST_NIELS", "CUST_AMY", "CUST_RAJ", "CUST_SARA", "CUST_TOM", "CUST_LENA"}
header(P)
story.chapter(5)
capability("One view of data quality across every operator database, from the account-wide expectation status view - "
           "the pattern for watching hundreds of `CUST_*` databases at once.",
           "Session 5 (4 min)", "Snowsight » Governance & security » Data quality shows your checks")
what_why(P)


def fleet(rows):
    df = pd.DataFrame([r for r in rows if r["OPERATOR"] in LAB_OPS])
    df["FAILING"] = df["FAILING"].map(lambda s: ", ".join(json.loads(s)) if s else "")
    df["HEALTH"] = df["FAILING_CHECKS"].map(lambda n: "Failing" if int(n) else "Healthy")
    return df[["OPERATOR", "HEALTH", "CHECKS", "FAILING_CHECKS", "FAILING", "LAST_MEASURED"]]


st.divider()
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: the fleet")
result_label("Captured from a real run, 6 operators")
when = st.segmented_control("Snapshot", ["After faults", "After CUST_NIELS fixed its fault"], default="After faults", key="fleet_when") or "After faults"
df = fleet(D.S5_FLEET if when == "After faults" else D.S5_FLEET_AFTER)
m1, m2, m3 = st.columns(3)
m1.metric("Operators", len(df))
m2.metric("Failing", int((df["HEALTH"] == "Failing").sum()))
m3.metric("Checks per operator", int(df["CHECKS"].max()))
st.dataframe(df, hide_index=True, width="stretch",
             column_config={"HEALTH": st.column_config.TextColumn("Health"),
                            "FAILING": st.column_config.TextColumn("Failing check", width="large")})
st.bar_chart(df.assign(FAILING_CHECKS=df["FAILING_CHECKS"].astype(int)), x="OPERATOR", y="FAILING_CHECKS", height=220)
st.caption("Six operators, six different failing checks - each fault has its own signature. In production the same view "
           "covers every `CUST_*` database, because the expectation status view is account-wide.")

st.divider()
prompt(P, 1)

checkpoints(P)
story.turn(5)
story.epilogue()
explanations(P)
tech(P)
sql_steps(P)
footer(P)
