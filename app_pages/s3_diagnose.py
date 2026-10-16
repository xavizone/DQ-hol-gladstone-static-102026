# Session 3 - Diagnose a broken answer (per-operator fault explorer)
# Co-authored with CoCo
import streamlit as st

import story

import sample_data as D
from ui import (capability, checkpoints, expectations_table, explanations, footer, header, prompt, result_label,
                snowsight, sql_steps, table, tech, what_why)

P = "session_03"
header(P)
story.chapter(3)
capability("Root-cause a wrong Nova answer: which expectation failed, which rows, which merge batch, and whether "
           "the pipeline itself stopped - using `SYSTEM$DATA_METRIC_SCAN`, task history and Dynamic Table refresh history.",
           "Session 3 (9 min)", "`SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS` returns rows for your schema")
what_why(P)

st.divider()
st.subheader("Minute 11: the facilitator injects one fault into every operator")
st.code("CALL GLADSTONE_DQ_LAB.ADMIN.INJECT_FAULTS('ALL');", language="sql")
if st.button("Inject faults (replay the captured run)", type="primary", icon=":material/bolt:"):
    st.session_state["faults_on"] = True
def faults_view():
    result_label("Captured from a real run, all 6 operators")
    st.markdown("**Fault per operator** (`ADMIN.V_FLEET_ANSWER_KEY` - facilitator only in the live lab)")
    table(D.F_ANSWER_KEY, cols=["SHORT_NAME", "FAULT_CODE", "DESCRIPTION"])

    st.divider()
    prompt(P, 0)
    snowsight(P, 0)

    OPS = {"NIELS": "Bifrost replay", "AMY": "Merge task stalled", "RAJ": "Refund sign flip",
           "SARA": "Orphan check-ins", "TOM": "Tenant leak", "LENA": "Status drift"}
    op = st.segmented_control("Look at operator", list(OPS), default="NIELS",
                              format_func=lambda o: f"{o} - {OPS[o]}", key="op_pick") or "NIELS"
    fault = next((r["FAULT_CODE"] for r in D.F_ANSWER_KEY if r["SHORT_NAME"] == op), None)
    story.ticket("s3", fault_code=fault, operator=f"CUST_{op}")
    st.markdown(f"#### `CUST_{op}`: what CoCo finds")
    evals = getattr(D, f"E_{op}_MEMBERS__MEMBER") + getattr(D, f"E_{op}_SYSTEM__PAYMENT") + getattr(D, f"E_{op}_SYSTEM__ATTENDANCE")
    bad = [r for r in evals if r["EXPECTATION_VIOLATED"]]
    c1, c2 = st.columns([1, 3])
    c1.metric("Expectations violated", len(bad), delta=f"of {len(evals)}", delta_color="off")
    if bad:
        c1.metric(bad[0]["EXPECTATION_NAME"].lower(), f"{float(bad[0]['VALUE']):,.0f}")
    with c2:
        expectations_table(evals)

    st.markdown("**Drill-down**")
    if op == "NIELS":
        st.markdown("Failing rows from `SYSTEM$DATA_METRIC_SCAN` on `DUPLICATE_COUNT(member_id)`:")
        table(D.D_NIELS_SCAN, cols=["MEMBER_ID", "OPERATOR_ID", "STATUS", "_BATCH_ID", "_LOADED_AT"])
        st.markdown("The batch applied twice (`_SYNC_META__MERGE_BATCH`):")
        table(D.D_NIELS_BATCH)
        a = D.D_NIELS_ACTIVE[0]
        st.metric("Active members (status) after the replay", f"{a['ACTIVE_MEMBERS']:,}",
                  delta=f"{a['ACTIVE_MEMBERS'] - D.S1_TWO_ACTIVE[0]['ACTIVE_MEMBERS']:+,} vs clean")
    elif op == "AMY":
        f = D.D_AMY_FRESH[0]
        st.metric("Seconds since last payment loaded", f["SECONDS_SINCE"], delta="expectation: < 180", delta_color="inverse")
        st.markdown("The merge task is suspended, and its history stops:")
        table(D.D_AMY_TASK)
        table(D.D_AMY_TASKHIST, cols=["NAME", "STATE", "SCHEDULED_TIME", "COMPLETED_TIME"])
        st.caption("REPORTING lag stays near 0 here: the source stopped, not REPORTING. That's why freshness and lag are separate checks.")
    elif op == "RAJ":
        st.markdown("Failing rows from `SYSTEM$DATA_METRIC_SCAN` on `NEGATIVE_COUNT(amount)`:")
        table(D.D_RAJ_SCAN, cols=["PAYMENT_ID", "MEMBER_ID", "PAYMENT_DATE", "AMOUNT", "PAYMENT_TYPE", "_BATCH_ID"])
        table(D.D_RAJ_BATCH)
        st.markdown("Today's net revenue collapses in `REPORTING__DAILY_REVENUE`:")
        table(D.D_RAJ_REVENUE)
    elif op == "SARA":
        st.markdown("Check-ins whose booking doesn't exist (`REFERENTIAL_INTEGRITY_COUNT(booking_id -> SYSTEM__BOOKING)`):")
        table(D.D_SARA_ORPHANS)
    elif op == "TOM":
        st.markdown("Rows by `operator_id` in TOM's member table - another operator's rows have arrived:")
        table(D.D_TOM_OPERATORS)
        st.caption("This is also a GDPR incident. Bonus B2 shows a row access policy hiding these rows immediately.")
    else:
        a = D.D_LENA_ACTIVE[0]
        m1, m2 = st.columns(2)
        m1.metric("Active members (status)", f"{a['ACTIVE_MEMBERS']:,}", delta=f"{a['ACTIVE_MEMBERS'] - D.S1_TWO_ACTIVE[0]['ACTIVE_MEMBERS']:+,} vs clean")
        m2.metric("Active members (paid in 35 days)", f"{a['PAID_MEMBERS_35D']:,}", delta="unchanged", delta_color="off")
        st.markdown("Members marked ACTIVE who have a leaving date (`DQ_COMMON.ACTIVE_BUT_LEFT`):")
        table(D.D_LENA_ROWS)


if st.session_state.get("faults_on"):
    faults_view()
else:
    st.caption("Press the button to see what each operator received.")

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: the monitoring view and refresh history")
result_label()
st.markdown("**Latest failing expectations for `CUST_NIELS`** (expectation status view, after the scheduled run)")
table(D.S3_FAILING)
st.markdown("**Dynamic Table refresh history** - refreshes keep succeeding, so the bad rows flow straight into REPORTING")
table(D.S3_DT_HISTORY, cols=["NAME", "STATE", "REFRESH_ACTION", "REFRESH_TRIGGER", "DATA_TIMESTAMP"])

checkpoints(P)
story.turn(3)
explanations(P)
tech(P)
sql_steps(P)
footer(P)
