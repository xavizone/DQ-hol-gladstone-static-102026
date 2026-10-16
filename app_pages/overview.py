# Overview - the problem, the pipeline, the agenda
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

import story

from ui import footer

_STATIC = Path(__file__).parent.parent / "static"

with st.container(horizontal=True, vertical_alignment="center", gap="large"):
    st.image(str(_STATIC / "gladstone_logo.jpg"), width=110)
    st.image(str(_STATIC / "snowflake_full_logo.png"), width=180)
st.title("Trust Nova's answers - data quality hands-on lab")

st.info("""**Capability:** Native data quality for Gladstone MRM's Nova pipelines - data metric functions, expectations,
Dynamic Tables, Tasks, semantic views and Cortex Agents - driven by prompts in **CoCo Desktop or CLI**.

**This app:** a read-only preview. Every result shown was captured from a real run of the lab; nothing connects to Snowflake.""",
        icon=":material/info:")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Core lab", "30 min", help="Sessions 1-5")
c2.metric("Prompts", "10 core", help="Plus stretch and bonus prompts")
c3.metric("Faults to find", "6", help="One per operator, round-robin")
c4.metric("Bonus labs", "3", help="Budgets, governance + GDPR, DCM DevOps")

st.markdown("### Who's in this story")
story.cast()
st.markdown("### Two versions of the same morning")
story.timelines()

st.markdown("""
### Why this matters
Nova went live on 28 September. A leisure operator rings Customer Success:

> *"Nova's **active members** and **last week's revenue** don't match what our front desk sees."*

The answer came from a Cortex Agent, reading a semantic view, reading REPORTING Dynamic Tables, built from Bronze tables
that Bifrost merges in from the operator's Azure SQL. Something upstream broke - a replayed merge batch, a stalled sync task,
refunds with the wrong sign, another operator's rows, or two definitions of "active member". Today Gladstone finds out from
the customer, one operator at a time, across hundreds of operator databases.

### What we'll demonstrate
1. Map one operator's pipeline end to end (Session 1)
2. Attach monitors and expectations (Session 2)
3. Find the root cause of a wrong Nova answer (Session 3)
4. Contain it with a circuit breaker and alert on it (Session 4)
5. See every operator's health in one view (Session 5)

### Outcome
Checks that run inside Snowflake on every operator database, catch each of the six faults on the first bad run, and stop bad
data before Nova answers with it.
""")

st.markdown("### Your operator pipeline")
st.graphviz_chart("""
digraph {
  rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#F0F4F8", color="#29B5E8", fontname="Helvetica"];
  src [label="Operator Azure SQL\\n(source)"]; task [label="TSK_BIFROST_MERGE\\n(simulated Bifrost, 1 min)"];
  bronze [label="Bronze\\nMEMBERS__* / SHARED__* / SYSTEM__*"]; dt [label="Silver REPORTING\\nDynamic Tables"];
  sv [label="Gold\\nSV_OPERATOR_KPIS\\n+ verified query"]; agent [label="Nova agent\\n(Cortex Agent)"];
  dq [label="Data metric functions\\n+ expectations", fillcolor="#E3F5FC"];
  src -> task -> bronze -> dt -> sv -> agent;
  dq -> bronze [style=dashed, arrowhead=none]; dq -> dt [style=dashed, arrowhead=none];
}""", width="stretch")

st.markdown("### Agenda")
st.markdown("""
| Time | Section | You do (in CoCo) | Snowflake capability |
|---|---|---|---|
| 0-4 | **1. Meet your operator pipeline** | Explain the pipeline; ask Nova's two KPIs | Lineage, Dynamic Tables, Tasks, semantic view |
| 4-11 | **2. Put monitors on it** | Freshness, volume, duplicates, tenant check, expectations | Data metric functions, expectations, custom DMFs |
| 11 | *Facilitator injects one fault into every operator* | - | - |
| 11-20 | **3. Diagnose a broken answer** | "Nova's numbers look wrong - find out why" | DQ results, failing rows, task and DT history, verified queries |
| 20-26 | **4. Contain and alert** | Circuit breaker task; notification on the critical check | Tasks, `SYSTEM$SET_RETURN_VALUE`, DQ notifications |
| 26-30 | **5. Fleet view across operators** | Which operators are broken right now? | Results across schemas, data quality dashboard |
""")

st.markdown("### The six faults")
st.markdown("""
| Fault | What happened (in Nova terms) | Symptom in Nova | Caught by (captured run) |
|---|---|---|---|
| Bifrost replay | The same merge batch was applied twice | Active members inflated | `DUPLICATE_COUNT` = 150 |
| Merge task stalled | The sync task stopped | Stale revenue, no new bookings | `FRESHNESS` 346 s (limit 180 s) |
| Refund sign flip | Refunds arrived as negative payments | Today's revenue collapses | `NEGATIVE_COUNT` = 40 |
| Orphan attendance | Check-ins arrived without their bookings | Utilisation over 100% for some classes | `REFERENTIAL_INTEGRITY_COUNT` = 60 |
| Tenant leak | Another operator's members routed in | Wrong member count; a GDPR incident | `FOREIGN_OPERATOR_ROWS` = 50 |
| Status drift | Cancelled members re-sent as ACTIVE | Two answers to "how many active members?" | `ACTIVE_BUT_LEFT` = 292 |
""")

st.markdown("### What this lab answers")
st.markdown("""
| Gladstone need | Covered in |
|---|---|
| Trust the data behind Nova before it reaches operators | Sessions 2-4 |
| Quality of semantic views and verified queries; lineage for discrepancy investigations | Sessions 3, 5 |
| Detailed data quality on the pipeline side, not only in BI | Whole lab |
| Detect cross-tenant data in an operator database | Session 2, Bonus B2 |
| Usage monitoring and overage warnings | Bonus B1 |
| Manage pipelines and checks as code with DCM Projects | Bonus B3 |
| Dynamic Table refresh objectives visible and monitored | Sessions 2-3 |
""")
footer("home")
