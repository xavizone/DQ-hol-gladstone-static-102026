# Gladstone MRM - Data quality hands-on lab (static backup)

Read-only version of the Gladstone MRM data quality lab, in the style of the Clutch static lab. It needs **no
Snowflake connection**. Every result on every page was captured from a real run of the lab on a Snowflake demo
account (16 Oct 2026), with account and user identifiers replaced. All data is synthetic.

Use it as a backup if the live environment is unavailable, as a pre-read, or as a leave-behind.

## What's inside

| Path | What |
|---|---|
| `streamlit_app.py` | Entry point and navigation |
| `app_pages/` | Overview, prep, setup, Sessions 1-5, stretch, bonus B1-B3, reference and teardown pages |
| `sample_data.py` | Captured results behind every demo table and metric (generated - don't hand-edit) |
| `snippets.py` | CoCo prompts, Snowsight routes, SQL and use cases copied from the interactive guide (generated) |
| `ui.py`, `components.py` | Page building blocks |
| `sql/` | The same admin, answer-key, bonus and teardown scripts as the interactive lab |
| `ADMIN_PREFLIGHT_QUESTIONNAIRE.md`, `ATTENDEE_ROSTER.csv`, `ATTENDEE_PREP.md` | Hand-outs |
| `tools/test_app.py` | Headless render test of every page |

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
python tools/test_app.py
```

## Deploy to Streamlit Community Cloud

Create an app at share.streamlit.io: repository `xavizone/DQ-hol-gladstone-static-102026`, branch `main`,
main file `streamlit_app.py`. No secrets are needed.
