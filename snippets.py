"""Prompts, SQL, Snowsight routes, use cases and references copied from the live guide
(operator shown as NIELS). Generated from dq-lab/workshop_guide - do not hand-edit."""
import links as L

PAGES = {
  'admin_setup': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Repeatable training environment",
    "body": "The same scripts stand up a sandbox for new data engineers or for operator-facing demos."
  },
  {
    "title": "Template for production rollout",
    "body": "`SETUP_ATTENDEE` is a small model of operator onboarding: clone, own, attach checks, register. Spares are the same idea as a pre-provisioned pool for new operators."
  }
],
    'refs': {'Docs': [L.DQ_SQL, L.DQ_NOTIFY, L.RES_MON, L.DT_OVERVIEW, L.TASKS, L.COCO]},
  },
  'admin_teardown': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Clean sandboxes",
    "body": "One teardown script keeps training accounts free of stray roles, warehouses and cost."
  },
  {
    "title": "Erasure thinking",
    "body": "Dropping data still leaves Time Travel and Fail-safe copies - the same point as Bonus B2's GDPR exercise."
  }
],
    'refs': {'Docs': [L.TIME_TRAVEL, L.FAILSAFE, L.RES_MON]},
  },
  'agenda': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "A real triage rota",
    "body": "These six are the failure modes of any CDC pipeline: duplicate, late, wrong sign, missing parent, wrong tenant, semantic drift. Each one maps to one check."
  },
  {
    "title": "Operator-facing SLAs",
    "body": "Freshness and completeness expectations become the evidence behind \"Nova data is never more than N minutes old\"."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DT], 'Docs': [L.DQ_EXPECT, L.TASKS]},
  },
  'availability': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Pre-flight before the workshop",
    "body": "The admin runs the checks above in `GLADSTONESOFTWARE` the day before and records any gaps on this page."
  },
  {
    "title": "Planning Nova features",
    "body": "Treat preview or upcoming items as roadmap conversations, and design Nova so the core path uses GA features."
  }
],
    'refs': {'Docs': [L.DQ_INTRO, L.DQ_ANOMALY, L.DCM, L.CROSS_REGION, L.AGENTS]},
  },
  'before_you_start': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Onboarding a new operator team",
    "body": "The same checklist (login, CoCo, role, a test prompt) works when a new operator's support engineers get access to their `CUST_*` database."
  },
  {
    "title": "Safe changes in a shared account",
    "body": "\"Read the SQL, then approve\" is the habit that matters in production, where one account serves many operators."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.COCO, L.COCO_CLI]},
  },
  'bonus_b1': {
    'prompts': [
  {
    "id": "Prompt B1.1",
    "title": "What does my operator cost?",
    "text": "Show what my operator pipeline in GLADSTONE_DQ_LAB.CUST_NIELS costs: data quality (serverless DMF credits from SNOWFLAKE.ACCOUNT_USAGE.DATA_QUALITY_MONITORING_USAGE_HISTORY, filtered to my database and schema), and dynamic table refresh counts and duration from INFORMATION_SCHEMA. Explain which costs land on DQ_LAB_WH and which are serverless, and note any ACCOUNT_USAGE latency."
  },
  {
    "id": "Prompt B1.2",
    "title": "Tag my operator for cost attribution",
    "text": "Tag schema GLADSTONE_DQ_LAB.CUST_NIELS with GLADSTONE_DQ_LAB.FINOPS.OPERATOR_ID = 'CUST_NIELS' and GLADSTONE_DQ_LAB.FINOPS.COST_CENTRE = 'nova'. Explain how objects inside the schema inherit the tags and how long until tag-based cost views reflect them."
  },
  {
    "id": "Prompt B1.3",
    "title": "A budget for my operator",
    "text": "Create a custom budget GLADSTONE_DQ_LAB.FINOPS.CUST_NIELS_BUDGET with a spending limit of 5 credits per month. Add my schema GLADSTONE_DQ_LAB.CUST_NIELS to it as a resource. Send email notifications through integration DQ_LAB_EMAIL_INT to my verified email address, at 80% of projected spend. Then list the budget's linked resources and show how to query its spending history."
  },
  {
    "id": "Prompt B1.4",
    "title": "Draft a resource monitor (admin applies it)",
    "text": "Draft, but do not run, a resource monitor for a Nova operator warehouse NOVA_WH_NIELS: 30 credits per month, notify at 75% and 90%, suspend at 100%. Explain why a resource monitor and a budget are both useful, what each one covers (warehouses vs serverless), and why only ACCOUNTADMIN can create the monitor."
  }
],
    'fallbacks': [
  "ALTER SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS SET TAG\n  GLADSTONE_DQ_LAB.FINOPS.OPERATOR_ID = 'CUST_NIELS',\n  GLADSTONE_DQ_LAB.FINOPS.COST_CENTRE = 'nova';\nUSE SCHEMA GLADSTONE_DQ_LAB.FINOPS;\nCREATE SNOWFLAKE.CORE.BUDGET CUST_NIELS_BUDGET();\nCALL CUST_NIELS_BUDGET!SET_SPENDING_LIMIT(5);\nCALL CUST_NIELS_BUDGET!ADD_RESOURCE(SYSTEM$REFERENCE('SCHEMA', 'GLADSTONE_DQ_LAB.CUST_NIELS', 'SESSION', 'applybudget'));\nCALL CUST_NIELS_BUDGET!SET_EMAIL_NOTIFICATIONS('DQ_LAB_EMAIL_INT', '<your verified email>');\nCALL CUST_NIELS_BUDGET!SET_NOTIFICATION_THRESHOLD(80);\nCALL CUST_NIELS_BUDGET!GET_LINKED_RESOURCES();"
],
    'snowsight': [
  {
    "after": "Prompt B1.1",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Consumption**: filter by warehouse `DQ_LAB_WH` and service type.",
      "**Admin \u00bb Cost management \u00bb Consumption** \u00bb service type *Data quality monitoring* for serverless DMF credits."
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.2",
    "steps": [
      "**Catalog \u00bb Database Explorer** \u00bb `CUST_NIELS` \u00bb **\u2026** \u00bb **Edit tags** \u00bb add `FINOPS.OPERATOR_ID` and `FINOPS.COST_CENTRE`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.3",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Budgets \u00bb + Budget**.",
      "Location `GLADSTONE_DQ_LAB.FINOPS`, name `CUST_NIELS_BUDGET`, 5 credits, threshold 80%, your email.",
      "**Budget scope** \u00bb Resources \u00bb Schemas \u00bb `CUST_NIELS`. (Or Tags \u00bb `COST_CENTRE = nova` for every operator in a tier.)"
    ],
    "sql": None
  },
  {
    "after": "Prompt B1.4",
    "steps": [
      "**Admin \u00bb Cost management \u00bb Resource monitors \u00bb + Resource monitor** (ACCOUNTADMIN)."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B1.3",
    "text": "`GET_LINKED_RESOURCES` lists your schema. Spending history fills after the budget's background refresh (can take hours).",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Budgets vs resource monitors",
    "body": "\n| | Budget | Resource monitor |\n|---|---|---|\n| Covers | Warehouses **and serverless** (DMFs, serverless tasks, DT background work) | Warehouses only |\n| Action | Notify (projected overspend) | Notify, **suspend** |\n| Scope | Objects, schemas, databases, **tags** | One or more warehouses / account |\n| Who creates | Any role with BUDGET_CREATOR + CREATE BUDGET | ACCOUNTADMIN |\n\nAt Gladstone scale: a **tag-based budget per tier** (e.g. `COST_CENTRE = nova`) plus a **resource monitor per shared warehouse**.\n"
  }
],
    'examples': [
  {
    "title": "Usage and overage warnings per operator",
    "body": "A budget per operator (or per tag) emails before an operator's Nova or DQ usage runs over its contract."
  },
  {
    "title": "Showback to product lines",
    "body": "`COST_CENTRE` tags split Snowflake spend between Nova, reporting and platform without separate accounts."
  },
  {
    "title": "Hard stop on runaway sync",
    "body": "A resource monitor on the Bifrost/merge warehouse suspends it if a replay loop burns credits overnight."
  },
  {
    "title": "Cost of data quality itself",
    "body": "`DATA_QUALITY_MONITORING_USAGE_HISTORY` shows what checks cost per operator - and whether a schedule should move to TRIGGER_ON_CHANGES."
  }
],
    'header': {
  "label": "Bonus B1",
  "title": "Budgets and resource monitors",
  "duration": "20 min, self-paced",
  "building": "Cost attribution, a budget per operator, and a hard cap"
},
    'what': "See what your operator pipeline costs, tag it for cost attribution, put a monthly **budget** on it with an alert, and draft a **resource monitor** the admin would apply.",
    'why': "Data quality and Nova run per operator. Without per-operator cost visibility, overages show up at month-end. Budgets warn early (and cover serverless DMFs); resource monitors hard-stop warehouses.",
    'fallback_after': [
  "Prompt B1.4"
],
    'refs': {'Quickstarts': [L.QS_COST, L.QS_QUERY_COST, L.WAF_COST], 'Docs': [L.BUDGETS, L.BUDGETS_CUSTOM, L.BUDGETS_TUT, L.RES_MON, L.COST_ATTR, L.DQ_USAGE]},
  },
  'bonus_b2': {
    'prompts': [
  {
    "id": "Prompt B2.1",
    "title": "Classify",
    "text": "Classify GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER for personal and sensitive data. List each column with its suggested semantic and privacy category and confidence. Do not apply any tags yet. Which column would be special-category data under UK GDPR?"
  },
  {
    "id": "Prompt B2.2",
    "title": "Tag-based masking",
    "text": "In GLADSTONE_DQ_LAB.CUST_NIELS, create a tag PII_TYPE with allowed values email, phone, dob, name, postcode, health. Create a string masking policy that shows the real value only when role DQ_LAB_PII_READER is in the session (keep the email domain visible), and a date masking policy that keeps only the birth year. Attach both policies to the PII_TYPE tag, then tag the email, phone, date_of_birth, first_name, last_name, postcode and health_notes columns of MEMBERS__MEMBER."
  },
  {
    "id": "Prompt B2.3",
    "title": "Row access per operator",
    "text": "Create a row access policy RAP_OWN_OPERATOR in GLADSTONE_DQ_LAB.CUST_NIELS that only returns rows where operator_id = 'CUST_NIELS' (lab admins excepted) and add it to MEMBERS__MEMBER on operator_id. Grant SELECT on MEMBERS__MEMBER to roles DQ_LAB_PII_READER and DQ_LAB_OPERATOR_VIEWER.\nThen prove it: query a few member rows with health notes as my role, as DQ_LAB_PII_READER and as DQ_LAB_OPERATOR_VIEWER, and count rows where operator_id is not CUST_NIELS. Explain what each role saw."
  },
  {
    "id": "Prompt B2.4",
    "title": "Does Nova expose personal data? Who read it?",
    "text": "Check whether semantic view GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS exposes any personal-data columns from MEMBERS__MEMBER. Then show who queried MEMBERS__MEMBER in the last day from SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY (note its latency)."
  },
  {
    "id": "Prompt B2.5",
    "title": "Record GDPR categories, lawful basis and retention",
    "text": "Using tags in GLADSTONE_DQ_LAB.GOVERNANCE (GDPR_CATEGORY, LAWFUL_BASIS, RETENTION_DAYS), tag the columns of GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER and SYSTEM__PAYMENT: identifiers and contact details under contract (730 days), health_notes as special_category under explicit_consent (30 days), marketing_consent under consent, payment amount as financial under legal_obligation (2190 days). Then list every tagged column as a simple record of processing."
  },
  {
    "id": "Prompt B2.6",
    "title": "Subject access request",
    "text": "Create a stored procedure GLADSTONE_DQ_LAB.CUST_NIELS.SAR_EXPORT(member_id) with caller's rights that finds every table in CUST_NIELS with a MEMBER_ID column, collects that member's rows into one JSON document grouped by table, and logs the request in GLADSTONE_DQ_LAB.GOVERNANCE.GDPR_REQUESTS (request_type 'SAR', completed now). Run it for member M-01043 with role DQ_LAB_PII_READER as a secondary role so masking lets the real data through, then turn secondary roles off again."
  },
  {
    "id": "Prompt B2.7",
    "title": "Erasure you can prove",
    "text": "Log an ERASURE request for member M-01042 in GLADSTONE_DQ_LAB.GOVERNANCE.GDPR_REQUESTS. Create a procedure GLADSTONE_DQ_LAB.CUST_NIELS.ERASE_MEMBER(member_id) that: replaces member_id with a salted SHA2 token and nulls contact, date of birth, postcode and health notes in MEMBERS__MEMBER; pseudonymises member_id in MEMBERS__MEMBERSHIP and SYSTEM__PAYMENT (keep payments for tax); deletes the member's SYSTEM__BOOKING and SYSTEM__ATTENDANCE rows; and marks the request completed with row counts as evidence. Run it for M-01042."
  },
  {
    "id": "Prompt B2.8",
    "title": "A data quality check that proves it",
    "text": "Attach GLADSTONE_DQ_LAB.DQ_COMMON.ERASED_MEMBERS_STILL_PRESENT to MEMBERS__MEMBER and SYSTEM__PAYMENT in GLADSTONE_DQ_LAB.CUST_NIELS, using GLADSTONE_DQ_LAB.GOVERNANCE.GDPR_REQUESTS(member_id, request_type, completed_at) as the second table, with expectation erasure_complete (value = 0). Evaluate it now."
  },
  {
    "id": "Prompt B2.9",
    "title": "Copies that survive",
    "text": "Is member M-01042 still recoverable anywhere? Check Time Travel on GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER (query the table as it was 2 minutes ago), show the table's retention period, explain Fail-safe, and explain the risk from the template schema this operator was cloned from. Set MEMBERS__MEMBER retention to 1 day. Finally, show the account's CORTEX_ENABLED_CROSS_REGION setting and what it means for UK data residency with Nova."
  }
],
    'fallbacks': [
  "-- See sql/bonus/B2_answer_key.sql for the full Part A + Part B answer key.\nUSE SECONDARY ROLES DQ_LAB_PII_READER;\nCALL GLADSTONE_DQ_LAB.CUST_NIELS.SAR_EXPORT('M-01043');\nUSE SECONDARY ROLES NONE;\nCALL GLADSTONE_DQ_LAB.CUST_NIELS.ERASE_MEMBER('M-01042');\nSELECT COUNT(*) FROM GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER AT(OFFSET => -120) WHERE member_id = 'M-01042';"
],
    'snowsight': [
  {
    "after": "Prompt B2.1",
    "steps": [
      "**Governance & security \u00bb Trust Center \u00bb Data security \u00bb Sensitive data** (or open the table \u00bb **\u2026** \u00bb **Classify data**).",
      "Review suggestions per column; apply or reject."
    ],
    "sql": "CALL SYSTEM$CLASSIFY('GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER', NULL);"
  },
  {
    "after": "Prompt B2.2",
    "steps": [
      "**Governance & security \u00bb Tags & policies \u00bb Policies \u00bb + Policy** \u00bb Masking policy (string) and (date).",
      "**Tags \u00bb + Tag** `PII_TYPE` \u00bb **Policies** \u00bb attach both masking policies.",
      "Open `MEMBERS__MEMBER` \u00bb **Columns** \u00bb set `PII_TYPE` on each personal column."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.3",
    "steps": [
      "**Governance & security \u00bb Tags & policies \u00bb Policies \u00bb + Policy** \u00bb Row access policy.",
      "Open `MEMBERS__MEMBER` \u00bb **Policies** \u00bb add row access policy on `operator_id`.",
      "Switch role in the worksheet's role picker to compare results."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.4",
    "steps": [
      "Open `SV_OPERATOR_KPIS` \u00bb **Definition**.",
      "**Monitoring \u00bb Query history** filtered by object, or query `ACCESS_HISTORY`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.5",
    "steps": [
      "Open each table \u00bb **Columns** \u00bb **Edit tags** \u00bb `GOVERNANCE.GDPR_CATEGORY`, `LAWFUL_BASIS`, `RETENTION_DAYS`."
    ],
    "sql": None
  },
  {
    "after": "Prompt B2.6",
    "steps": [
      "Create the procedure in a worksheet, then run `USE SECONDARY ROLES DQ_LAB_PII_READER; CALL SAR_EXPORT('M-01043');`."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B2.3",
    "text": "Your role sees `*** MASKED ***`; `DQ_LAB_PII_READER` sees real values; nobody sees rows from another operator (this also hides a **tenant leak**).",
    "sql": None
  },
  {
    "after": "Prompt B2.8",
    "text": "`erasure_complete` passes (0) on both tables. Try it: comment out the payment update in ERASE_MEMBER, erase another member, and watch the check fail.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why tag-based masking at Gladstone scale",
    "body": "\nA masking policy attached to a **tag** protects every column that carries the tag - in every operator database. Classification\n(or a classification profile with a tag map) applies the tag; the policy follows automatically. One policy, hundreds of `CUST_*` databases.\n\n**Lab note:** attendees have `APPLY MASKING POLICY` and `APPLY ROW ACCESS POLICY` on the account so each can build their own.\nIn production give these to a central governance role only.\n"
  },
  {
    "title": "Why caller's rights and a secondary role?",
    "body": "\nAn owner's-rights procedure runs as your operator role, so the masking policy masks the export - a useless SAR. With\n**caller's rights** and `DQ_LAB_PII_READER` active as a **secondary role**, `IS_ROLE_IN_SESSION` lets real values through,\nand only people with the privacy role can produce an unmasked SAR.\n"
  },
  {
    "title": "What the lab shows",
    "body": "\n- **Time Travel** still returns the pre-erasure row until retention passes; **Fail-safe** keeps it 7 more days (permanent tables), recoverable only by Snowflake.\n- The **template** (`ADMIN_OPERATOR_TEMPLATE`) still holds M-01042 - just like dev/test clones of a production operator. Erasure has to cover clones.\n- Shorter retention on personal-data tables reduces this window; transient tables have no Fail-safe.\n- `CORTEX_ENABLED_CROSS_REGION` controls whether Cortex can process prompts outside the account's region. For UK-only processing, the admin restricts it.\n"
  }
],
    'examples': [
  {
    "title": "Health notes never reach Nova",
    "body": "Tagged as `health`, masked for every role except a privacy role, and absent from the semantic view."
  },
  {
    "title": "SARs for any operator",
    "body": "One SAR procedure pattern, deployed to every `CUST_*` database, answers within the one-month deadline with an audit trail."
  },
  {
    "title": "Erasure with evidence",
    "body": "The erasure check turns \"we deleted it\" into a scheduled, provable result per operator."
  },
  {
    "title": "Tenant leak = data incident",
    "body": "Row access by operator hides leaked rows immediately, while the DQ check and access history give the evidence for a breach assessment."
  }
],
    'header': {
  "label": "Bonus B2",
  "title": "Data governance and GDPR",
  "duration": "40 min, self-paced",
  "building": "Classification, masking, row access, then SAR, erasure and retention"
},
    'what': "Run the three GDPR workflows Gladstone faces as a processor for leisure operators: record **why** you hold each field, answer a **subject access request**, and carry out an **erasure** you can prove.",
    'why': "Members ask operators for their data and for deletion. With one database per operator, Gladstone needs a repeatable, auditable way to do this in Snowflake - including the copies (Time Travel, clones) that survive a DELETE.",
    'fallback_after': [
  "Prompt B2.9"
],
    'refs': {'Quickstarts': [L.QS_HORIZON, L.QS_GOV_ADV, L.WAF_SEC], 'Docs': [L.CLASSIFY, L.CLASSIFY_SP, L.TAG_MASK, L.RAP, L.ACCESS_HIST, L.TIME_TRAVEL, L.FAILSAFE, L.CROSS_REGION, L.AI_REDACT, L.TRUST_CENTER], 'UK GDPR guidance': [L.ICO_SAR, L.ICO_ERASURE, L.ICO_STORAGE, L.ICO_SPECIAL, L.ICO_BREACH]},
  },
  'bonus_b3': {
    'prompts': [
  {
    "id": "Prompt B3.1",
    "title": "Create the project",
    "text": "Create a DCM project for my operator pipeline.\n- Project identifier: GLADSTONE_DQ_LAB.CUST_NIELS_DCM.OPERATOR_PIPELINE, owner role DQ_LAB_NIELS, local folder ./operator_pipeline\n- manifest v2 with a target NIELS and templating variables db, schema (CUST_NIELS_DCM), operator_id (CUST_NIELS), wh (DQ_LAB_WH), dq_schedule ('5 MINUTE'), reporting_lag ('1 minute')\n- Bronze tables MEMBERS__MEMBER and SYSTEM__PAYMENT (same columns as in GLADSTONE_DQ_LAB.CUST_NIELS) with change tracking and DATA_METRIC_SCHEDULE\n- dynamic tables REPORTING__DAILY_REVENUE and REPORTING__ACTIVE_MEMBERS, incremental\n- expectations: no duplicate member_id, GLADSTONE_DQ_LAB.DQ_COMMON.FOREIGN_OPERATOR_ROWS, DQ_COMMON.ACTIVE_BUT_LEFT, no negative amounts, net_revenue never null\nRegister the project in Snowflake and validate it. Don't deploy yet."
  },
  {
    "id": "Prompt B3.2",
    "title": "Plan, then deploy",
    "text": "Run a plan for target NIELS and summarise what it will create, alter or drop. Explain any entry you weren't expecting. If it looks right, deploy with the alias first-deploy."
  },
  {
    "id": "Prompt B3.3",
    "title": "Test, break, test again",
    "text": "Run snow dcm test for target NIELS. Then insert two rows with the same member_id into GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER and run the test again. What exit code does the CLI return, and why does that matter for CI?"
  },
  {
    "id": "Prompt B3.4",
    "title": "Change and onboard",
    "text": "1. Change reporting_lag to '5 minutes' and plan again - show me that only the two dynamic tables change.\n2. Show how I'd onboard a second operator CUST_ACME: what to add to manifest.yml and which commands to run.\n3. Write a GitHub Actions workflow that runs plan + test on pull requests and deploy + test on main, using the Snowflake CLI."
  }
],
    'fallbacks': [],
    'snowsight': [
  {
    "after": "Prompt B3.1",
    "steps": [
      "**Projects \u00bb Workspaces** \u00bb **+ Add new \u00bb DCM project** \u00bb choose `GLADSTONE_DQ_LAB.CUST_NIELS_DCM`.",
      "Add the definition files (see the answer key below) to the workspace."
    ],
    "sql": None
  },
  {
    "after": "Prompt B3.2",
    "steps": [
      "In the DCM workspace \u00bb **Plan** \u00bb review the change set \u00bb **Deploy**."
    ],
    "sql": None
  }
],
    'checkpoints': [
  {
    "after": "Prompt B3.2",
    "text": "Plan shows 4 creates (2 tables, 2 dynamic tables) and an `ALTER ROLE` that only records ownership of the new objects; deploy succeeds.",
    "sql": None
  },
  {
    "after": "Prompt B3.3",
    "text": "First run: 5/5 pass. After the duplicate: `NO_DUPLICATE_MEMBERS` fails and the CLI exits with **1** - a failed pipeline step in CI.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why DCM for operator databases",
    "body": "\n- **Declarative**: definitions describe the end state; `plan` shows the diff before anything changes.\n- **Templated targets**: one set of definitions, one target per operator (or per tier), different variables.\n- **Data quality ships with the pipeline**: `ATTACH DATA METRIC FUNCTION ... EXPECTATION` lives next to the table it protects.\n- **Test as a gate**: `snow dcm test` exits non-zero on a failed expectation.\n- **Note**: a DCM project can't define its own parent database or schema - they must exist (that's why the admin pre-creates `CUST_<NAME>_DCM`).\n"
  }
],
    'examples': [
  {
    "title": "Operator onboarding as a pull request",
    "body": "A new operator is a new target in the manifest; review the plan in the PR, merge to deploy."
  },
  {
    "title": "Same checks everywhere",
    "body": "A new expectation added once reaches every operator on the next deploy - no drift between `CUST_*` databases."
  },
  {
    "title": "Safer REPORTING changes",
    "body": "`plan` shows whether a change alters or recreates a dynamic table before it touches production."
  },
  {
    "title": "Promotion DEV to PROD",
    "body": "Separate targets and accounts (dev, reporting, production) with the same definitions."
  }
],
    'header': {
  "label": "Bonus B3",
  "title": "DevOps with DCM Projects",
  "duration": "30 min, self-paced",
  "building": "One operator's pipeline and its data quality checks as code"
},
    'what': "Turn what you built by hand into a **DCM project**: Bronze tables, REPORTING Dynamic Tables and their expectations, declared once, deployed per operator with `plan`, `deploy` and `test`.",
    'why': "Hundreds of operator databases can't be configured by hand. With DCM, onboarding operator N is a new target and a `deploy`; every operator gets the same data quality from day one, and `snow dcm test` is a CI gate.",
    'refs': {'Quickstarts': [L.QS_DCM, L.QS_DCM_PIPE, L.QS_DCM_DT, L.QS_DCM_TASKS, L.QS_DEVOPS], 'Docs': [L.DCM, L.SNOW_CLI, L.DQ_EXPECT]},
  },
  'getting_started': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Same pattern in production",
    "body": "A support engineer connects CoCo with a read role for one `CUST_*` database and investigates without touching other operators."
  },
  {
    "title": "CLI for repeatable runs",
    "body": "The CoCo CLI can be scripted, so the same prompts can run across operators from a terminal or a scheduled job."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI, L.QS_COCO_BP], 'Docs': [L.COCO, L.COCO_CLI]},
  },
  'home': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Before a Nova answer reaches an operator",
    "body": "Checks on the REPORTING tables the semantic view reads, so a bad sync stops at Silver instead of reaching the Nova Portal."
  },
  {
    "title": "Onboarding a new operator",
    "body": "The same monitors attach to the new `CUST_*` database on day one, so the first Bifrost sync is already checked."
  },
  {
    "title": "Customer Success escalations",
    "body": "\"Nova gave me the wrong number\" becomes a five-minute CoCo root-cause conversation, with evidence to send back to the operator."
  },
  {
    "title": "GCP-to-Azure migration",
    "body": "The same checks prove the migrated operator data matches before cut-over."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.DQ_INTRO, L.DT_OVERVIEW, L.SV_OVERVIEW, L.AGENTS, L.COCO]},
  },
  'install_coco': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Rolling CoCo out to the data team",
    "body": "The same checklist - access role, account identifier, SSO connection, a test prompt - works for every Gladstone engineer, not just the lab."
  },
  {
    "title": "IT-managed laptops",
    "body": "The Windows System installer and CoCo Desktop managed settings let IT deploy and configure CoCo centrally."
  }
],
    'refs': {'Downloads': [L.COCO_DOWNLOADS, L.SNOW_CLI_RELEASES], 'Quickstarts': [L.QS_COCO_DESKTOP, L.QS_COCO_CLI], 'Docs': [L.COCO_DESKTOP, L.COCO_DESKTOP_SETUP, L.COCO_DESKTOP_FAQ, L.COCO_CLI, L.COCO_CLI_REF, L.SNOW_CLI_INSTALL, L.CROSS_REGION, L.ACCOUNT_ID]},
  },
  'reference_coco': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Support playbook",
    "body": "Save these prompts as a CoCo skill so every CS and data engineer investigates an operator the same way."
  },
  {
    "title": "Scripted fleet checks",
    "body": "Run the same prompts with the CoCo CLI against several operator databases from a terminal or a scheduled job."
  }
],
    'refs': {'Quickstarts': [L.QS_COCO_BP, L.QS_COCO_DE, L.QS_COCO_CLI], 'Docs': [L.COCO, L.COCO_CLI, L.DQ_DASH]},
  },
  'scaling': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "500 operator databases, one change",
    "body": "A new expectation added to the DCM project reaches every operator on the next deploy."
  },
  {
    "title": "Reporting account",
    "body": "Results and the fleet view can also be shared to `GLADSTONEREPORTING` for CS and leadership dashboards."
  },
  {
    "title": "Migration waves",
    "body": "Each GCP-to-Azure migration wave runs the same reconciliation checks per operator before cut-over."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DCM_PIPE, L.WAF_SEC], 'Docs': [L.DQ_SCHEMA, L.DQ_GROUP, L.DQ_DASH, L.DQ_USAGE, L.DCM]},
  },
  'session_01': {
    'prompts': [
  {
    "id": "Prompt 1.1",
    "title": "Explain the pipeline",
    "text": "In GLADSTONE_DQ_LAB.CUST_NIELS, explain the data pipeline end to end:\n- which tables are Bronze (MEMBERS__, SHARED__, SYSTEM__ prefixes) and what the _SYNC_META__MERGE_BATCH table records\n- what task TSK_BIFROST_MERGE does and how often it runs\n- what each REPORTING__ dynamic table computes, its target lag, refresh mode, and which Bronze tables feed it\n- what semantic view SV_OPERATOR_KPIS exposes (metrics and verified queries)\nDraw the lineage as a simple left-to-right diagram. Do not change anything."
  },
  {
    "id": "Prompt 1.2",
    "title": "Ask Nova's two KPIs",
    "text": "Using semantic view GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS, answer:\n1. How many active members do we have?\n2. What was our net revenue and class utilisation over the last 7 days?\nShow me which metric or verified query you used for each answer. If \"active members\" can be calculated two ways in this semantic view, show both numbers side by side and explain the difference."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS;\nSHOW DYNAMIC TABLES;\nSHOW TASKS;\nSELECT * FROM SEMANTIC_VIEW(SV_OPERATOR_KPIS METRICS am.active_members, ms.paid_members_35d);\nSELECT * FROM SEMANTIC_VIEW(SV_OPERATOR_KPIS METRICS rev.net_revenue, util.utilisation_pct, util.no_show_rate);"
],
    'snowsight': [
  {
    "after": "Prompt 1.1",
    "steps": [
      "**Catalog \u00bb Database Explorer** \u00bb `GLADSTONE_DQ_LAB` \u00bb `CUST_NIELS`.",
      "Open `REPORTING__DAILY_REVENUE` \u00bb **Lineage** tab to see its upstream Bronze table.",
      "**Transformation \u00bb Dynamic tables**: target lag, refresh mode and refresh history.",
      "**Transformation \u00bb Tasks** \u00bb `TSK_BIFROST_MERGE` \u00bb **Run history**.",
      "**AI & ML \u00bb Cortex Analyst** \u00bb `SV_OPERATOR_KPIS` to browse metrics and verified queries."
    ],
    "sql": "USE SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS;\nSHOW DYNAMIC TABLES;   -- target_lag, refresh_mode, scheduling_state\nSHOW TASKS;\nDESCRIBE SEMANTIC VIEW SV_OPERATOR_KPIS;"
  },
  {
    "after": "Prompt 1.2",
    "steps": [
      "**AI & ML \u00bb Cortex Analyst** \u00bb open `SV_OPERATOR_KPIS` \u00bb **Playground** and ask the same questions.",
      "Note which answer uses the verified query `vq_active_members`."
    ],
    "sql": "SELECT * FROM SEMANTIC_VIEW(GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS\n  METRICS am.active_members, ms.paid_members_35d);"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 1.2",
    "text": "You can name the 4 layers and you have seen **two different numbers for active members** (status-based vs paid in the last 35 days). Note them - they matter in Session 3.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why two answers?",
    "body": "\n`am.active_members` counts members whose **source status** is `ACTIVE`. The verified query (`vq_active_members`) uses the\n**finance definition** - members who **paid in the last 35 days**. About 6% of ACTIVE members haven't paid in more than\n35 days, so the two numbers differ even on clean data.\n\nThis is the \"discrepancy investigation\" problem: when an operator says Nova is wrong, first check **which definition** answered.\nA semantic-layer quality check (Session 3) compares the two and alerts when the gap moves.\n"
  }
],
    'examples': [
  {
    "title": "Customer Success first response",
    "body": "Before escalating to engineering, CS asks CoCo to map the operator's pipeline and which definition Nova used."
  },
  {
    "title": "Onboarding a data engineer",
    "body": "A new joiner gets a plain-English map of any `CUST_*` database in minutes, from live metadata rather than out-of-date docs."
  }
],
    'header': {
  "label": "Session 1",
  "title": "Meet your operator pipeline",
  "duration": "4 min",
  "building": "Your mental model of one operator's Nova pipeline"
},
    'what': "Ask CoCo to explain your operator's pipeline end to end, then ask Nova's semantic view the two questions operators ask most.",
    'why': "You cannot monitor what you cannot see. Gladstone runs one database per operator, so every investigation starts by mapping that operator's Bronze, REPORTING and Gold objects.",
    'fallback_after': [
  "Prompt 1.2"
],
    'tech': [
  {
    "name": "Dynamic Tables",
    "icon": "sync",
    "description": "REPORTING layer, incremental refresh, 1-minute target lag"
  },
  {
    "name": "Tasks",
    "icon": "schedule",
    "description": "TSK_BIFROST_MERGE simulates the Bifrost merge"
  },
  {
    "name": "Semantic view",
    "icon": "schema",
    "description": "Gold layer Nova answers from, with a verified query"
  }
],
    'refs': {'Quickstarts': [L.QS_SV, L.QS_DT], 'Docs': [L.LINEAGE, L.DT_MONITOR, L.SV_CREATE]},
  },
  'session_02': {
    'prompts': [
  {
    "id": "Prompt 2.1",
    "title": "Monitor freshness, volume and invariants",
    "text": "Set up data quality monitoring in GLADSTONE_DQ_LAB.CUST_NIELS. Run every check every 5 minutes.\nOn MEMBERS__MEMBER:\n- no duplicate member_id (expect 0)\n- no rows from another operator: use GLADSTONE_DQ_LAB.DQ_COMMON.FOREIGN_OPERATOR_ROWS on operator_id (expect 0)\n- no ACTIVE members with a leave date: use GLADSTONE_DQ_LAB.DQ_COMMON.ACTIVE_BUT_LEFT on (status, left_on) (expect 0)\nOn SYSTEM__PAYMENT:\n- no negative amounts (expect 0)\n- table updated in the last 3 minutes (FRESHNESS on the table itself, expect under 180 seconds)\n- row count with anomaly detection turned on\nOn SYSTEM__ATTENDANCE:\n- every booking_id exists in SYSTEM__BOOKING (referential integrity, expect 0 orphans)\nGive each expectation a clear name. Show me the SQL before running it."
  },
  {
    "id": "Prompt 2.2",
    "title": "Monitor the REPORTING layer and check now",
    "text": "On dynamic table GLADSTONE_DQ_LAB.CUST_NIELS.REPORTING__DAILY_REVENUE, add an expectation that it trails its Bronze source SYSTEM__PAYMENT by less than 5 minutes: use GLADSTONE_DQ_LAB.DQ_COMMON.REPORTING_LAG_SECONDS on (last_loaded_at) with SYSTEM__PAYMENT(_loaded_at) as the second table, and run it every 5 minutes.\nThen evaluate every expectation in my schema right now (do not wait for the schedule) and show a table of check, value and pass/fail."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS;\nALTER TABLE MEMBERS__MEMBER    SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__PAYMENT    SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__ATTENDANCE SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER DYNAMIC TABLE REPORTING__DAILY_REVENUE SET DATA_METRIC_SCHEDULE = '5 MINUTE';\nALTER TABLE SYSTEM__PAYMENT ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ROW_COUNT ON () ANOMALY_DETECTION = TRUE;\nALTER TABLE MEMBERS__MEMBER ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.DUPLICATE_COUNT ON (member_id)\n  EXPECTATION no_duplicate_members (VALUE = 0);\nALTER TABLE MEMBERS__MEMBER ADD DATA METRIC FUNCTION GLADSTONE_DQ_LAB.DQ_COMMON.FOREIGN_OPERATOR_ROWS ON (operator_id)\n  EXPECTATION no_other_operator_rows (VALUE = 0);\nALTER TABLE MEMBERS__MEMBER ADD DATA METRIC FUNCTION GLADSTONE_DQ_LAB.DQ_COMMON.ACTIVE_BUT_LEFT ON (status, left_on)\n  EXPECTATION no_active_leavers (VALUE = 0);\nALTER TABLE SYSTEM__PAYMENT ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.NEGATIVE_COUNT ON (amount)\n  EXPECTATION no_negative_amounts (VALUE = 0);\nALTER TABLE SYSTEM__PAYMENT ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.FRESHNESS ON ()\n  EXPECTATION payments_fresh_3min (VALUE < 180);\nALTER TABLE SYSTEM__ATTENDANCE ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.REFERENTIAL_INTEGRITY_COUNT\n  ON (booking_id, TABLE(GLADSTONE_DQ_LAB.CUST_NIELS.SYSTEM__BOOKING(booking_id)))\n  EXPECTATION no_orphan_checkins (VALUE = 0);\nALTER DYNAMIC TABLE REPORTING__DAILY_REVENUE ADD DATA METRIC FUNCTION GLADSTONE_DQ_LAB.DQ_COMMON.REPORTING_LAG_SECONDS\n  ON (last_loaded_at, TABLE(GLADSTONE_DQ_LAB.CUST_NIELS.SYSTEM__PAYMENT(_loaded_at)))\n  EXPECTATION reporting_within_5min (VALUE < 300);"
],
    'snowsight': [
  {
    "after": "Prompt 2.1",
    "steps": [
      "Open **Catalog \u00bb Database Explorer** \u00bb `CUST_NIELS` \u00bb `MEMBERS__MEMBER` \u00bb **Data Quality** tab.",
      "Select **Monitor** \u00bb set the schedule to every 5 minutes.",
      "Add **Duplicate count** on `member_id`; add the expectation *Value = 0*.",
      "Add **Custom DMF** `DQ_COMMON.FOREIGN_OPERATOR_ROWS` on `operator_id` with *Value = 0*.",
      "Repeat on `SYSTEM__PAYMENT` (Negative count, Freshness, Row count) and `SYSTEM__ATTENDANCE` (Referential integrity to `SYSTEM__BOOKING.booking_id`).",
      "The table's Data Quality tab lists each check, its schedule, last value and pass/fail."
    ],
    "sql": None
  },
  {
    "after": "Prompt 2.2",
    "steps": [
      "Open `REPORTING__DAILY_REVENUE` \u00bb **Data Quality** \u00bb add custom DMF `DQ_COMMON.REPORTING_LAG_SECONDS`.",
      "Run the worksheet query below to evaluate expectations immediately."
    ],
    "sql": "SELECT * FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(\n  REF_ENTITY_NAME => 'GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER'));\nSELECT * FROM TABLE(SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS(\n  REF_ENTITY_NAME => 'GLADSTONE_DQ_LAB.CUST_NIELS.SYSTEM__PAYMENT'));"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 2.2",
    "text": "All **7 expectations pass** on clean data. FRESHNESS should be under 180 seconds because the merge task runs every minute. Tell the facilitator you're ready - faults go in next.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "Why expectations, and not only anomaly detection?",
    "body": "\n**Anomaly detection** (on ROW_COUNT and FRESHNESS) learns normal behaviour and needs **at least two weeks** of history before it\nflags anything - during this lab it shows `TRAINING_IN_PROGRESS`. Turn it on now so it's working in two weeks.\n\n**Expectations** encode rules that must **always** hold (no duplicates, no foreign operator rows, no negative payments) and\nfail on the first bad run. Use both: expectations for invariants, anomaly detection for \"this looks unusual\".\n"
  }
],
    'examples': [
  {
    "title": "Replacing homegrown DATA_MONITORING_WH checks",
    "body": "Checks scheduled on a warehouse become serverless DMFs with history, pass/fail and notifications built in."
  },
  {
    "title": "Cross-tenant leak detection",
    "body": "`FOREIGN_OPERATOR_ROWS` on every operator database turns a GDPR incident into a 5-minute alert."
  },
  {
    "title": "Bifrost sync SLAs",
    "body": "FRESHNESS and Bronze-to-REPORTING lag per operator give CS and engineering one shared definition of \"late\"."
  },
  {
    "title": "Payments integrity",
    "body": "NEGATIVE_COUNT and referential integrity catch sign bugs and partial syncs before revenue dashboards move."
  }
],
    'header': {
  "label": "Session 2",
  "title": "Put monitors on it",
  "duration": "7 min",
  "building": "Data metric functions and expectations on Bronze and REPORTING"
},
    'what': "Attach Snowflake data metric functions (DMFs) to your Bronze tables and a REPORTING Dynamic Table, and turn each invariant into an **expectation** that passes or fails.",
    'why': "These run serverless inside Snowflake, next to the data, on a schedule - no extra warehouse, no external tool. Defined once, the same checks attach to every operator database.",
    'fallback_after': [
  "Prompt 2.2"
],
    'tech': [
  {
    "name": "System DMFs",
    "icon": "fact_check",
    "description": "DUPLICATE_COUNT, NEGATIVE_COUNT, FRESHNESS, ROW_COUNT, REFERENTIAL_INTEGRITY_COUNT"
  },
  {
    "name": "Custom DMFs",
    "icon": "function",
    "description": "Central DQ_COMMON checks: foreign operator rows, active-but-left, Bronze-to-REPORTING lag"
  },
  {
    "name": "Expectations",
    "icon": "rule",
    "description": "Pass/fail rules on any DMF; results in SNOWFLAKE.LOCAL views"
  }
],
    'concepts': [
  {
    "term": "Data metric function (DMF)",
    "definition": "A function attached to a table, view or dynamic table that returns one number on a schedule. Runs on serverless compute."
  },
  {
    "term": "Expectation",
    "definition": "A boolean rule on a DMF's value, e.g. `VALUE = 0`. A violation is recorded in `SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS` and can trigger a notification."
  },
  {
    "term": "Multi-table DMF",
    "definition": "A DMF with two table arguments (REFERENTIAL_INTEGRITY_COUNT, REPORTING_LAG_SECONDS) - compares Bronze with REPORTING, or a child with its parent."
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DQM], 'Docs': [L.DQ_SQL, L.DQ_EXPECT, L.DQ_CUSTOM, L.DQ_RI, L.DQ_ANOMALY, L.DQ_SCHEMA]},
  },
  'session_03': {
    'prompts': [
  {
    "id": "Prompt 3.1",
    "title": "Investigate the complaint",
    "text": "My operator says Nova's numbers are wrong this week. Investigate GLADSTONE_DQ_LAB.CUST_NIELS:\n1. Which data quality expectations are failing right now? Use the latest scheduled results, and evaluate now if results are stale.\n2. For each failing check, show me sample failing rows and the merge batch (_batch_id / _SYNC_META__MERGE_BATCH) that introduced them.\n3. Is the pipeline healthy? Check TSK_BIFROST_MERGE run history and the REPORTING__ dynamic table refresh history.\n4. Which Nova metrics in SV_OPERATOR_KPIS are affected, and by roughly how much?\nGive me a one-paragraph root cause I could send to the operator."
  },
  {
    "id": "Prompt 3.2",
    "title": "Check the semantic layer",
    "text": "Compare the two definitions of active members in GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS: the active_members metric (source status) and the verified query vq_active_members (paid in the last 35 days). How big is the gap now, in members and percent? On clean data it was about 5% (78 members). If it has moved, which Bronze change explains it?"
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS;\n-- failing checks\nSELECT table_name, metric_name, expectation_name, value, measurement_time\nFROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\nWHERE table_database = 'GLADSTONE_DQ_LAB' AND table_schema = 'CUST_NIELS' AND expectation_violated\nQUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1;\n-- failing rows (example: duplicates)\nSELECT * FROM TABLE(SYSTEM$DATA_METRIC_SCAN(\n  REF_ENTITY_NAME => 'GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBER',\n  METRIC_NAME => 'SNOWFLAKE.CORE.DUPLICATE_COUNT', ARGUMENT_NAME => 'member_id')) LIMIT 20;\n-- suspicious batches\nSELECT batch_id, table_name, COUNT(*) times_applied FROM _SYNC_META__MERGE_BATCH GROUP BY 1, 2 HAVING COUNT(*) > 1;\nSELECT _batch_id, COUNT(*) FROM SYSTEM__PAYMENT WHERE amount < 0 GROUP BY 1;\nSELECT operator_id, _batch_id, COUNT(*) FROM MEMBERS__MEMBER GROUP BY 1, 2 ORDER BY 3 DESC;\n-- pipeline health\nSHOW TASKS LIKE 'TSK_BIFROST_MERGE';\nSELECT name, state, scheduled_time, error_message\nFROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'TSK_BIFROST_MERGE', RESULT_LIMIT => 10))\nORDER BY scheduled_time DESC;\n-- Nova impact\nSELECT * FROM SEMANTIC_VIEW(SV_OPERATOR_KPIS METRICS am.active_members, ms.paid_members_35d);"
],
    'snowsight': [
  {
    "after": "Prompt 3.1",
    "steps": [
      "**Governance & security \u00bb Data quality**: open incidents across the account. Select your failing check \u00bb **Investigate** opens CoCo with the incident loaded.",
      "Open the failing table \u00bb **Data Quality** tab \u00bb select the check to see value history.",
      "**Transformation \u00bb Tasks** \u00bb `TSK_BIFROST_MERGE` \u00bb **Run history** (suspended? no runs?).",
      "**Transformation \u00bb Dynamic tables** \u00bb refresh history for each `REPORTING__` table."
    ],
    "sql": "SELECT table_name, metric_name, expectation_name, value, measurement_time\nFROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\nWHERE table_database = 'GLADSTONE_DQ_LAB' AND table_schema = 'CUST_NIELS' AND expectation_violated\nQUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1;"
  },
  {
    "after": "Prompt 3.2",
    "steps": [
      "**AI & ML \u00bb Cortex Analyst** \u00bb `SV_OPERATOR_KPIS` \u00bb ask *How many active members do we have?* and compare with the `am.active_members` metric."
    ],
    "sql": "SELECT * FROM SEMANTIC_VIEW(GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS\n  METRICS am.active_members, ms.paid_members_35d);"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 3.2",
    "text": "You can state your fault in one sentence (which check, which batch, which Nova metric). Compare with your neighbour - each of you got a different fault.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "What each fault looks like",
    "body": "\n| If CoCo finds... | It's the... | Notice |\n|---|---|---|\n| `DUPLICATE_COUNT(member_id)` > 0, batch `B-REPLAY-01` applied twice | Bifrost replay | Active members inflated |\n| `FRESHNESS` over 180s, task SUSPENDED | Merge task stalled | REPORTING lag stays **0** - REPORTING isn't behind its source; the **source** stopped. That's why you need both checks. |\n| `NEGATIVE_COUNT(amount)` > 0, batch `B-SIGNBUG-01` | Refund sign flip | Today's net revenue drops |\n| `REFERENTIAL_INTEGRITY_COUNT` > 0, `BK-GHOST-*` | Orphan attendance | Utilisation can exceed 100% |\n| `FOREIGN_OPERATOR_ROWS` > 0, `CUST_NEIGHBOUR` | Tenant leak | Also a **GDPR** incident - see Bonus B2 |\n| `ACTIVE_BUT_LEFT` > 0, gap between definitions grows | Status drift | A semantic-layer problem, not a pipeline failure |\n"
  }
],
    'examples': [
  {
    "title": "CS escalation in five minutes",
    "body": "The one-paragraph root cause from Prompt 3.1 is what goes back to the operator - with the batch id and the fix."
  },
  {
    "title": "Bifrost incident review",
    "body": "Batch-level evidence (`_SYNC_META`) shows whether a replay or partial sync hit one operator or many."
  },
  {
    "title": "Verified query drift",
    "body": "Comparing a metric with its verified query catches semantic-layer drift that no row-level check would."
  }
],
    'header': {
  "label": "Session 3",
  "title": "Diagnose a broken answer",
  "duration": "9 min",
  "building": "A root-cause investigation, start to finish, from one prompt"
},
    'what': "Give CoCo the complaint the way an operator would phrase it. Let it find which check failed, which rows and batch caused it, and whether the pipeline itself is healthy.",
    'why': "This is the Customer Success escalation Gladstone handles today by hand. CoCo's data-quality skill follows the same evidence trail an engineer would, in minutes, and shows its working.",
    'fallback_after': [
  "Prompt 3.2"
],
    'tech': [
  {
    "name": "DQ results views",
    "icon": "table_view",
    "description": "SNOWFLAKE.LOCAL expectation status and results history"
  },
  {
    "name": "SYSTEM$DATA_METRIC_SCAN",
    "icon": "search",
    "description": "Returns the rows that made a system DMF fail"
  },
  {
    "name": "Task and DT history",
    "icon": "history",
    "description": "TASK_HISTORY and DYNAMIC_TABLE_REFRESH_HISTORY"
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_COCO_DE], 'Docs': [L.DQ_DASH, L.DQ_SCAN, L.TASK_HISTORY, L.DT_MONITOR, L.SV_CREATE]},
  },
  'session_04': {
    'prompts': [
  {
    "id": "Prompt 4.1",
    "title": "Build a circuit breaker",
    "text": "In GLADSTONE_DQ_LAB.CUST_NIELS, create a task TSK_DQ_CIRCUIT_BREAKER on warehouse DQ_LAB_WH that runs every minute and:\n- reads the latest result per expectation from SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS for tables MEMBERS__MEMBER, SYSTEM__PAYMENT and SYSTEM__ATTENDANCE in schema CUST_NIELS\n- if any is violated: suspends dynamic tables REPORTING__ACTIVE_MEMBERS and REPORTING__DAILY_REVENUE\n- otherwise: resumes them\n- records what it did with SYSTEM$SET_RETURN_VALUE (for example \"OPEN: 1 failing check\" or \"CLOSED: Bronze clean\"); build the message in a variable first, because SYSTEM$SET_RETURN_VALUE does not accept an expression\nResume the task, wait for one run, and show me its return value and the dynamic tables' scheduling state."
  },
  {
    "id": "Prompt 4.2",
    "title": "Fix the fault, close the breaker, choose alerts",
    "text": "Based on the root cause you found in Session 3, fix the Bronze data in GLADSTONE_DQ_LAB.CUST_NIELS (for example delete the bad batch, or resume a suspended task). Show me the SQL first.\nThen re-evaluate the expectations, confirm the circuit breaker closes and the REPORTING dynamic tables resume.\nFinally, notifications are already enabled for this database by the admin: keep email notifications ON only for no_other_operator_rows and no_duplicate_members, and turn them OFF for every other check in my schema."
  }
],
    'fallbacks': [
  "USE SCHEMA GLADSTONE_DQ_LAB.CUST_NIELS;\nCREATE OR REPLACE TASK TSK_DQ_CIRCUIT_BREAKER WAREHOUSE = DQ_LAB_WH SCHEDULE = '1 MINUTE'\nAS\nEXECUTE IMMEDIATE $$\nDECLARE bad NUMBER; msg VARCHAR;\nBEGIN\n  SELECT COUNT(*) INTO :bad FROM (\n    SELECT expectation_violated FROM SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS\n    WHERE table_database = 'GLADSTONE_DQ_LAB' AND table_schema = 'CUST_NIELS'\n      AND table_name IN ('MEMBERS__MEMBER', 'SYSTEM__PAYMENT', 'SYSTEM__ATTENDANCE')\n    QUALIFY ROW_NUMBER() OVER (PARTITION BY table_name, expectation_name ORDER BY measurement_time DESC) = 1)\n  WHERE expectation_violated;\n  IF (bad > 0) THEN\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LAB.CUST_NIELS.REPORTING__ACTIVE_MEMBERS SUSPEND;\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LAB.CUST_NIELS.REPORTING__DAILY_REVENUE SUSPEND;\n    msg := 'OPEN: ' || :bad || ' failing Bronze check(s)';   -- SET_RETURN_VALUE needs a variable, not an expression\n    CALL SYSTEM$SET_RETURN_VALUE(:msg);\n  ELSE\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LAB.CUST_NIELS.REPORTING__ACTIVE_MEMBERS RESUME;\n    ALTER DYNAMIC TABLE GLADSTONE_DQ_LAB.CUST_NIELS.REPORTING__DAILY_REVENUE RESUME;\n    CALL SYSTEM$SET_RETURN_VALUE('CLOSED: Bronze clean');\n  END IF;\nEND;\n$$;\nALTER TASK TSK_DQ_CIRCUIT_BREAKER RESUME;\n\n-- notifications: keep the two critical checks, silence the rest (repeat SET ... FALSE per check)\nALTER TABLE MEMBERS__MEMBER MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.DUPLICATE_COUNT ON (member_id)\n  SET DATA_QUALITY_NOTIFICATION = TRUE;\nALTER TABLE SYSTEM__PAYMENT MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.FRESHNESS ON ()\n  SET DATA_QUALITY_NOTIFICATION = FALSE;"
],
    'snowsight': [
  {
    "after": "Prompt 4.1",
    "steps": [
      "**Projects \u00bb Workspaces** (or a worksheet): paste the task SQL from *Behind? Run this* and run it.",
      "**Transformation \u00bb Tasks** \u00bb `TSK_DQ_CIRCUIT_BREAKER` \u00bb **Run history** shows each return value.",
      "**Transformation \u00bb Dynamic tables** shows `REPORTING__*` as **Suspended** while the breaker is open."
    ],
    "sql": None
  },
  {
    "after": "Prompt 4.2",
    "steps": [
      "Open the table \u00bb **Data Quality** \u00bb select a check \u00bb **Notifications** toggle.",
      "Re-check: **Transformation \u00bb Tasks** \u00bb breaker run history should read *CLOSED: Bronze clean*."
    ],
    "sql": "ALTER TABLE GLADSTONE_DQ_LAB.CUST_NIELS.SYSTEM__PAYMENT\n  MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.NEGATIVE_COUNT ON (amount)\n  SET DATA_QUALITY_NOTIFICATION = FALSE;"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 4.2",
    "text": "Breaker run history shows **OPEN** then **CLOSED: Bronze clean**, and `REPORTING__*` are active again.",
    "sql": "SELECT state, return_value, completed_time\nFROM TABLE(GLADSTONE_DQ_LAB.INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'TSK_DQ_CIRCUIT_BREAKER', RESULT_LIMIT => 5))\nWHERE state <> 'SCHEDULED' ORDER BY completed_time DESC;"
  }
],
    'explanations': [
  {
    "title": "Fixes by fault",
    "body": "\n| Fault | Fix |\n|---|---|\n| Bifrost replay | `DELETE FROM MEMBERS__MEMBER WHERE _batch_id = 'B-REPLAY-01';` |\n| Merge task stalled | `ALTER TASK TSK_BIFROST_MERGE RESUME;` (FRESHNESS recovers within a minute) |\n| Refund sign flip | `DELETE FROM SYSTEM__PAYMENT WHERE _batch_id = 'B-SIGNBUG-01';` (in production: reload as REFUND with positive amount) |\n| Orphan attendance | `DELETE FROM SYSTEM__ATTENDANCE WHERE booking_id LIKE 'BK-GHOST-%';` (in production: re-sync the bookings) |\n| Tenant leak | `DELETE FROM MEMBERS__MEMBER WHERE operator_id <> 'CUST_NIELS';` - then treat it as a personal-data incident (Bonus B2) |\n| Status drift | `UPDATE MEMBERS__MEMBER SET status = 'CANCELLED' WHERE status = 'ACTIVE' AND left_on IS NOT NULL;` |\n\n**Why only the circuit breaker on Bronze checks?** The breaker freezes the REPORTING tables. If it also watched REPORTING checks,\nfreezing REPORTING could keep it failing - so it would never close.\n\n**How notifications work:** the database owner turns them on once for the whole database (`DATA_QUALITY_MONITORING_SETTINGS`);\neach table owner then chooses which checks notify. In production that's one setting per operator database, with the same email or Slack/Teams webhook integration.\n"
  }
],
    'examples': [
  {
    "title": "Protect Nova before month-end",
    "body": "Operators run finance reports at month-end. A breaker keeps Nova answering from yesterday's good data during a bad sync."
  },
  {
    "title": "Slack or Teams for the on-call engineer",
    "body": "Swap the email integration for a webhook integration so tenant-leak alerts page the right channel."
  },
  {
    "title": "Per-tier alert policies",
    "body": "Enterprise operators get notifications on every invariant; smaller operators on the critical two."
  }
],
    'header': {
  "label": "Session 4",
  "title": "Contain and alert",
  "duration": "6 min",
  "building": "A circuit breaker task and a notification on the critical check"
},
    'what': "Stop bad Bronze data reaching Nova: a task that freezes the REPORTING Dynamic Tables while any Bronze expectation fails, and resumes them when it's clean. Then decide which checks should email you.",
    'why': "Detection alone still lets Nova serve a wrong number. Pausing REPORTING stops further bad batches reaching Nova - stale beats wrong. (With 5-minute checks and 1-minute REPORTING, the first bad batch can already be in; checks triggered on change close that gap.) Notifications on only the critical checks avoid alert fatigue across hundreds of operators.",
    'fallback_after': [
  "Prompt 4.2"
],
    'tech': [
  {
    "name": "Tasks",
    "icon": "schedule",
    "description": "Serverful task with a Snowflake Scripting body and a return value"
  },
  {
    "name": "Dynamic Table suspend / resume",
    "icon": "pause_circle",
    "description": "Pause REPORTING while Bronze is failing"
  },
  {
    "name": "DQ notifications",
    "icon": "notifications",
    "description": "Database-level setting, per-check toggle, email or webhook"
  }
],
    'built': [
  "Seven monitors and expectations on `CUST_NIELS`",
  "A root-cause analysis of a real fault",
  "A circuit breaker protecting Nova's REPORTING layer",
  "Alerts on the two checks that matter most"
],
    'refs': {'Quickstarts': [L.QS_STREAMS_TASKS, L.QS_TRAIL], 'Docs': [L.TASKS, L.TASK_RETURN, L.DT_MONITOR, L.DQ_NOTIFY]},
  },
  'session_05': {
    'prompts': [
  {
    "id": "Prompt 5.1",
    "title": "Which operators are broken?",
    "text": "Query GLADSTONE_DQ_LAB.ADMIN.V_FLEET_DQ_HEALTH. Which operators have failing data quality checks right now, and which checks? Group operators by the type of failure and suggest the most likely root cause for each group. Show me where my operator CUST_NIELS sits."
  },
  {
    "id": "Prompt 5.2",
    "title": "Design the production rollout",
    "text": "We run one Snowflake database per operator (CUST_*), hundreds of them. Based on what I built in GLADSTONE_DQ_LAB.CUST_NIELS, outline how to roll these data quality checks out to every operator database:\n- where the custom DMFs should live and who owns them\n- how to attach the same checks to a new operator automatically\n- how to aggregate results into one fleet view\n- what it costs (DMFs are serverless) and how to keep that cost predictable\nKeep it to one page."
  }
],
    'fallbacks': [
  "SELECT operator, checks, failing_checks, failing, last_measured FROM GLADSTONE_DQ_LAB.ADMIN.V_FLEET_DQ_HEALTH;"
],
    'snowsight': [
  {
    "after": "Prompt 5.1",
    "steps": [
      "**Governance & security \u00bb Data quality**: **Monitored schemas** lists every `CUST_*` schema with failing expectations and coverage.",
      "Select several incidents \u00bb **Investigate** opens one CoCo thread with all of them."
    ],
    "sql": "SELECT * FROM GLADSTONE_DQ_LAB.ADMIN.V_FLEET_DQ_HEALTH;"
  }
],
    'checkpoints': [
  {
    "after": "Prompt 5.2",
    "text": "You can see **six different failure signatures** across the room (if six or more operators). Your operator should now show 0 failing checks.",
    "sql": None
  }
],
    'explanations': [
  {
    "title": "How the fleet view works",
    "body": "\n`V_FLEET_DQ_HEALTH` reads `SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS`, keeps the latest result per\noperator, table and expectation, and counts the failures. It's owned by the lab admin, so you can read the summary but not\nother operators' data.\n\nIn production the same query, filtered to `table_database LIKE 'CUST_%'`, is the fleet view - one place for Platform and CS\nto see every operator. See **Reference \u00bb Scaling to every operator**.\n"
  }
],
    'examples': [
  {
    "title": "Daily fleet triage",
    "body": "Platform reviews failing operators each morning; repeat offenders get a Bifrost or source-system ticket."
  },
  {
    "title": "Operator health in account reviews",
    "body": "Data quality pass rate per operator becomes a KPI in operator QBRs."
  },
  {
    "title": "Release safety",
    "body": "After a Bifrost or REPORTING release, the fleet view shows within one schedule whether any operator regressed."
  }
],
    'header': {
  "label": "Session 5",
  "title": "Fleet view across operators",
  "duration": "4 min",
  "building": "One view of every operator's data quality"
},
    'what': "Look across every operator in the room at once: which are failing, which check, since when.",
    'why': "Gladstone has hundreds of operator databases. Nobody can open each one. The same results that power your operator's checks roll up into one fleet view - the start of a Gladstone-wide data quality SLA.",
    'fallback_after': [
  "Prompt 5.2"
],
    'tech': [
  {
    "name": "Data quality dashboard",
    "icon": "dashboard",
    "description": "Account-wide incidents, monitored schemas, Investigate with CoCo"
  },
  {
    "name": "Results views",
    "icon": "table_view",
    "description": "One results store across every database in the account"
  },
  {
    "name": "Secure summary view",
    "icon": "visibility",
    "description": "Owner's-rights view: see the summary, not the data"
  }
],
    'refs': {'Quickstarts': [L.QS_DQ, L.QS_DQM], 'Docs': [L.DQ_DASH, L.DQ_SCHEMA, L.DQ_GROUP]},
  },
  'snowsight_map': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Analysts without CoCo",
    "body": "Business users and CS can follow the same checks from Snowsight menus, with no prompts needed."
  },
  {
    "title": "Incident handover",
    "body": "On-call shares a Snowsight link to the failing check's Data Quality tab instead of screenshots."
  }
],
    'refs': {'Docs': [L.DQ_DASH, L.DT_MONITOR, L.LINEAGE, L.BUDGETS, L.TRUST_CENTER, L.DCM]},
  },
  'stretch': {
    'prompts': [
  {
    "id": "Prompt S.1",
    "title": "Create and question the agent",
    "text": "Create a Cortex Agent GLADSTONE_DQ_LAB.CUST_NIELS.NOVA_OPERATOR_AGENT that uses semantic view GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS as a Cortex Analyst tool on warehouse DQ_LAB_WH. Instruct it to always say which metric or verified query it used.\nThen ask it: \"How many active members do we have?\" and \"What was net revenue yesterday?\"\nCompare its answers with the active_members metric and the verified query, and with my current data quality results. Would you trust each answer? Why?"
  },
  {
    "id": "Prompt S.2",
    "title": "Daily digest for Customer Success",
    "text": "In GLADSTONE_DQ_LAB.CUST_NIELS, create a view V_DQ_DIGEST that lists, for the last 24 hours, every expectation in my schema with: latest value, pass/fail, number of failed runs and first failure time. Then create a task that runs it daily at 07:00 Europe/London and writes the result into a table DQ_DIGEST_HISTORY. Keep the task suspended - show me how I would resume it."
  },
  {
    "id": "Prompt S.3",
    "title": "Before/after migration check",
    "text": "Pretend GLADSTONE_DQ_LAB.CUST_NIELS is an operator that has just been migrated from GCP to Azure, and GLADSTONE_DQ_LAB.ADMIN_OPERATOR_TEMPLATE is not visible to me. Using only my schema, design the reconciliation checks I'd run before cut-over: row counts per Bronze table, sum of payment amounts per day, distinct members per status, and max _loaded_at. Write them as data metric functions or SQL I can run against both copies, and explain which differences are acceptable."
  }
],
    'fallbacks': [
  "CREATE OR REPLACE AGENT GLADSTONE_DQ_LAB.CUST_NIELS.NOVA_OPERATOR_AGENT FROM SPECIFICATION $$\n{\"instructions\": {\"response\": \"Answer for this leisure operator only. Always say which metric or verified query you used.\",\n                  \"orchestration\": \"Use the operator_kpis tool for members, revenue and utilisation questions.\"},\n \"tools\": [{\"tool_spec\": {\"type\": \"cortex_analyst_text_to_sql\", \"name\": \"operator_kpis\",\n                          \"description\": \"Active members, revenue, class utilisation for this operator\"}}],\n \"tool_resources\": {\"operator_kpis\": {\"semantic_view\": \"GLADSTONE_DQ_LAB.CUST_NIELS.SV_OPERATOR_KPIS\",\n                    \"execution_environment\": {\"type\": \"warehouse\", \"warehouse\": \"DQ_LAB_WH\"}}}}\n$$;"
],
    'snowsight': [
  {
    "after": "Prompt S.1",
    "steps": [
      "**AI & ML \u00bb Agents** \u00bb **Create agent** in `CUST_NIELS`; add a **Cortex Analyst** tool on `SV_OPERATOR_KPIS`, warehouse `DQ_LAB_WH`.",
      "Use the agent's **Playground** to ask the questions; open the thinking trace to see the verified query being used."
    ],
    "sql": None
  },
  {
    "after": "Prompt S.2",
    "steps": [
      "Create the view and table in a worksheet, then **Transformation \u00bb Tasks \u00bb + Task** with a CRON schedule `0 7 * * * Europe/London`."
    ],
    "sql": None
  }
],
    'checkpoints': [],
    'explanations': [
  {
    "title": "What to look for",
    "body": "\nThe agent answers *\"How many active members?\"* from the **verified query** (paid in the last 35 days) - so it disagrees with the\nstatus-based dashboard number. Neither is a bug: they're two definitions. Fix it in the semantic view (rename the metric, document the definition,\nor align the verified query), then re-test. For ongoing quality, use **Cortex Agent evaluations** and **AI Observability**.\n"
  }
],
    'examples': [
  {
    "title": "Nova agent regression tests",
    "body": "A fixed set of operator questions with known answers runs after every semantic-view change, using agent evaluations."
  },
  {
    "title": "CS morning digest",
    "body": "The daily digest goes to Customer Success, so they know about a broken operator before the operator rings."
  },
  {
    "title": "GCP to Azure cut-over",
    "body": "Reconciliation DMFs give a signed-off, repeatable before/after comparison per operator database."
  }
],
    'what': "Create a Cortex Agent over `SV_OPERATOR_KPIS` (a mini Nova), ask it the operator's questions, and check the answer against the data quality results.",
    'why': "Nova's trust problem is at the agent layer: the agent picks a metric or a verified query. Testing agent answers against known-good numbers is the AI-side half of data quality.",
    'fallback_after': [
  "Prompt S.1"
],
    'refs': {'Quickstarts': [L.QS_AGENTS, L.QS_AGENT_EVAL, L.QS_AI_OBS, L.QS_SV_BP], 'Docs': [L.AGENTS, L.AI_OBS, L.SV_CREATE, L.TASKS]},
  },
  'troubleshooting': {
    'prompts': [],
    'fallbacks': [],
    'snowsight': [],
    'checkpoints': [],
    'explanations': [],
    'examples': [
  {
    "title": "Rollout runbook",
    "body": "These fixes become the runbook when the checks are rolled out to every `CUST_*` database."
  },
  {
    "title": "Least-privilege checks",
    "body": "The isolation errors prove the operator-per-database access model is working - keep them in production."
  }
],
    'refs': {'Docs': [L.DQ_EXPECT, L.DQ_ANOMALY, L.TAG_MASK, L.DT_MONITOR, L.TASK_HISTORY]},
  },
}
