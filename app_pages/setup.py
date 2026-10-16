# Setup (admin) - questionnaire, timeline, scripts, walk-ins
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

import sample_data as D
from ui import footer, result_label, table

ROOT = Path(__file__).parent.parent
SQL = ROOT / "sql"


def sql_file(name: str, label: str | None = None):
    with st.expander(label or f":material/description: `{name}`"):
        st.code((SQL / name).read_text(), language="sql", line_numbers=True)


st.title("Setup (admin)")
st.info("""**Capability:** One database (`GLADSTONE_DQ_LAB`), one warehouse (`DQ_LAB_WH`, 20-credit monitor) and one
zero-copy-cloned schema plus role per attendee - real isolation, seconds to create, one `DROP DATABASE` to remove.

**Who:** the Gladstone Snowflake admin, with ACCOUNTADMIN. **When:** questions at T-5 working days, setup at T-3 (~15 min).""",
        icon=":material/admin_panel_settings:")

before, setup, walkins, during = st.tabs([":material/event: Before the day", ":material/play_circle: Setup",
                                          ":material/person_add: Walk-ins", ":material/sports: During the session"])
with before:
    st.markdown("""
| When | Who | Do |
|---|---|---|
| T-5 working days | Facilitator | Send the questionnaire's six **T-5** items and the roster template. Send attendees the prep sheet. |
| T-5 | Admin | Check every roster user exists: `SHOW USERS LIKE '<user>';` |
| T-3 | Admin | Run the setup scripts, including spares. Send back the pre-flight output and `V_ROSTER`. |
| T-1 | Attendees | Log in, open CoCo, run the test prompt. |
| T-1 | Facilitator | `V_ROSTER`: everyone `ASSIGNED`, recent login, at least 2 `SPARE - free`. |
""")
    c1, c2, c3 = st.columns(3)
    for col, (f, label, mime) in zip([c1, c2, c3], [("ADMIN_PREFLIGHT_QUESTIONNAIRE.md", "Admin questionnaire", "text/markdown"),
                                                    ("ATTENDEE_ROSTER.csv", "Roster template (CSV)", "text/csv"),
                                                    ("ATTENDEE_PREP.md", "Attendee prep sheet", "text/markdown")]):
        col.download_button(label, data=(ROOT / f).read_text(), file_name=f, mime=mime, icon=":material/download:", key=f"dl_{f}")
    with st.container(border=True):
        st.markdown((ROOT / "ADMIN_PREFLIGHT_QUESTIONNAIRE.md").read_text().split("\n", 1)[-1])

with setup:
    st.markdown("""
| Requirement | Why |
|---|---|
| **ACCOUNTADMIN** for setup and teardown | Creates roles, warehouse, monitor, integration; alters users |
| **Enterprise Edition or higher** | Data metric functions, classification, masking and row access |
| Attendee Snowflake **users** exist, with CoCo access | `SETUP_ALL` grants roles (and optionally sets defaults) |
| A **verified email** | Email integration for DQ and budget notifications |
| A warehouse other than `DQ_LAB_WH` | Used by teardown before dropping the lab warehouse |
""")
    st.markdown("#### Run order")
    sql_file("00_admin_setup.sql", "1. `00_admin_setup.sql` - account objects, roles, lab database (edit LAB_ADMIN_EMAIL first)")
    sql_file("01_build_template.sql", "2. `01_build_template.sql` - synthetic gold-copy operator + central DMFs")
    sql_file("02_lab_procs.sql", "3. `02_lab_procs.sql` - setup, spare, fault, reset procedures and views")
    st.markdown("**4. One operator per attendee, plus spares**")
    st.code("""USE ROLE ACCOUNTADMIN;
USE WAREHOUSE DQ_LAB_WH;
CALL GLADSTONE_DQ_LAB.ADMIN.SETUP_ALL(PARSE_JSON('[
  {"user": "NJOHANSEN", "name": "NIELS"},
  {"user": "ASMITH",    "name": "AMY", "set_defaults": false}
]'));
CALL GLADSTONE_DQ_LAB.ADMIN.SETUP_SPARES(3);
SELECT * FROM GLADSTONE_DQ_LAB.ADMIN.V_ROSTER;""", language="sql")
    st.markdown("**Demo results: `V_ROSTER` after setup**")
    result_label("Captured from a real run with 6 operators and 2 spares, no users bound")
    table(D.A_ROSTER)

with walkins:
    st.markdown("""
| Situation | Action | Time |
|---|---|---|
| Has a Snowflake user, a spare is free | `CALL GLADSTONE_DQ_LAB.ADMIN.CLAIM_SPARE('<USER>');` - tell them the operator name it returns | ~1 s |
| Has a user, no spare left | Same call - it builds a new operator named after the user | ~20 s |
| User name not found | The call returns ERROR and claims nothing. `SHOW USERS LIKE '%<part>%';` | - |
| No Snowflake user | Pair with a neighbour, or create a temporary user if policy allows, then claim a spare | - |
| Arrives after faults were injected | `CALL GLADSTONE_DQ_LAB.ADMIN.INJECT_FAULTS('<NAME>');` once they finish Session 2 | ~2 s |
""")

with during:
    st.markdown("""
| When | Run | Effect |
|---|---|---|
| End of Session 2 (min 11) | `CALL GLADSTONE_DQ_LAB.ADMIN.INJECT_FAULTS('ALL');` | One fault per operator, by setup order |
| Anytime | `SELECT * FROM GLADSTONE_DQ_LAB.ADMIN.V_FLEET_ANSWER_KEY;` | Who got which fault (facilitator only) |
| Session 5 | `SELECT * FROM GLADSTONE_DQ_LAB.ADMIN.V_FLEET_DQ_HEALTH;` | Fleet view |
| Attendee stuck | `CALL GLADSTONE_DQ_LAB.ADMIN.RESET_ATTENDEE('NIELS');` | Fresh operator in seconds |
| End | `CALL GLADSTONE_DQ_LAB.ADMIN.SUSPEND_ALL();` | Stops tasks and DTs, notifications off |
""")
    sql_file("answer_key_core.sql", ":material/key: Core answer key (Sessions 2-4)")
    sql_file("99_reset_attendee.sql")

footer("admin_setup")
