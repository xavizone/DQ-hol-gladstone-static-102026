"""Results captured from a real run of the Gladstone DQ lab on a Snowflake demo account (16 Oct 2026).
Account and user identifiers are replaced with placeholders. Data is synthetic. Generated - do not hand-edit."""

A_ROSTER = [
 {
  "OPERATOR_NAME": "NIELS",
  "SCHEMA_NAME": "CUST_NIELS",
  "ROLE_NAME": "DQ_LAB_NIELS",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "AMY",
  "SCHEMA_NAME": "CUST_AMY",
  "ROLE_NAME": "DQ_LAB_AMY",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "RAJ",
  "SCHEMA_NAME": "CUST_RAJ",
  "ROLE_NAME": "DQ_LAB_RAJ",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "SARA",
  "SCHEMA_NAME": "CUST_SARA",
  "ROLE_NAME": "DQ_LAB_SARA",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "TOM",
  "SCHEMA_NAME": "CUST_TOM",
  "ROLE_NAME": "DQ_LAB_TOM",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "LENA",
  "SCHEMA_NAME": "CUST_LENA",
  "ROLE_NAME": "DQ_LAB_LENA",
  "USER_NAME": None,
  "STATUS": "NO USER BOUND"
 },
 {
  "OPERATOR_NAME": "SPARE01",
  "SCHEMA_NAME": "CUST_SPARE01",
  "ROLE_NAME": "DQ_LAB_SPARE01",
  "USER_NAME": None,
  "STATUS": "SPARE - free"
 },
 {
  "OPERATOR_NAME": "SPARE02",
  "SCHEMA_NAME": "CUST_SPARE02",
  "ROLE_NAME": "DQ_LAB_SPARE02",
  "USER_NAME": None,
  "STATUS": "SPARE - free"
 }
]

B1_DT_COST = [
 {
  "NAME": "REPORTING__ACTIVE_MEMBERS",
  "REFRESHES": 21,
  "REFRESH_SECONDS": 9
 },
 {
  "NAME": "REPORTING__CLASS_UTILISATION",
  "REFRESHES": 25,
  "REFRESH_SECONDS": 63
 },
 {
  "NAME": "REPORTING__DAILY_REVENUE",
  "REFRESHES": 21,
  "REFRESH_SECONDS": 22
 }
]

B1_LIMIT = [
 {
  "GET_SPENDING_LIMIT": 5
 }
]

B1_LINKED = [
 {
  "RESOURCE_ID": 2942,
  "NAME": "CUST_NIELS",
  "DOMAIN": "SCHEMA",
  "SCHEMA_NAME": None,
  "DATABASE_NAME": "GLADSTONE_DQ_LAB"
 }
]

B1_MONITORS = [
 {
  "name": "DQ_LAB_RM",
  "credit_quota": "20.00",
  "used_credits": "0.92",
  "remaining_credits": "19.08",
  "frequency": "MONTHLY",
  "notify_at": "75%",
  "suspend_at": "100%"
 },
 {
  "name": "DQ_LAB_RM_DEMO",
  "credit_quota": "2.00",
  "used_credits": "0.00",
  "remaining_credits": "2.00",
  "frequency": "DAILY",
  "notify_at": "50%,90%",
  "suspend_at": "100%"
 }
]

B1_TAGS = [
 {
  "TAG_NAME": "COST_CENTRE",
  "TAG_VALUE": "nova",
  "LEVEL": "SCHEMA",
  "OBJECT_NAME": "CUST_NIELS"
 },
 {
  "TAG_NAME": "OPERATOR_ID",
  "TAG_VALUE": "CUST_NIELS",
  "LEVEL": "SCHEMA",
  "OBJECT_NAME": "CUST_NIELS"
 }
]

B1_THRESHOLD = [
 {
  "GET_NOTIFICATION_THRESHOLD": 80
 }
]

B1_WH = [
 {
  "name": "DQ_LAB_WH",
  "size": "X-Small",
  "min_cluster_count": 1,
  "max_cluster_count": 3,
  "auto_suspend": 60,
  "resource_monitor": "DQ_LAB_RM"
 }
]

B2_CLASSIFY = [
 {
  "SYSTEM$CLASSIFY": "{\n  \"classification_result\": {\n    \"DATE_OF_BIRTH\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"QUASI_IDENTIFIER\",\n        \"semantic_category\": \"DATE_OF_BIRTH\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"DATE_OF_BIRTH\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"QUASI_IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"EMAIL\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"EMAIL\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"EMAIL\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"FIRST_NAME\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"NAME\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"NAME\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"HEALTH_NOTES\": {\n      \"alternates\": []\n    },\n    \"HOME_SITE_ID\": {\n      \"alternates\": []\n    },\n    \"JOINED_ON\": {\n      \"alternates\": []\n    },\n    \"LAST_ACTIVITY_AT\": {\n      \"alternates\": []\n    },\n    \"LAST_NAME\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"HIGH\",\n        \"coverage\": 1,\n        \"details\": [],\n        \"privacy_category\": \"IDENTIFIER\",\n        \"semantic_category\": \"NAME\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"NAME\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"LEFT_ON\": {\n      \"alternates\": []\n    },\n    \"MARKETING_CONSENT\": {\n      \"alternates\": []\n    },\n    \"MEMBER_ID\": {\n      \"alternates\": []\n    },\n    \"OPERATOR_ID\": {\n      \"alternates\": []\n    },\n    \"PHONE\": {\n      \"alternates\": []\n    },\n    \"POSTCODE\": {\n      \"alternates\": [],\n      \"recommendation\": {\n        \"confidence\": \"LOW\",\n        \"coverage\": 0.4645,\n        \"details\": [\n          {\n            \"coverage\": 0.4645,\n            \"semantic_category\": \"UK_POSTAL_CODE\"\n          }\n        ],\n        \"privacy_category\": \"QUASI_IDENTIFIER\",\n        \"semantic_category\": \"POSTAL_CODE\",\n        \"tags\": [\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.semantic_category\",\n            \"tag_value\": \"POSTAL_CODE\"\n          },\n          {\n            \"tag_applied\": False,\n            \"tag_name\": \"snowflake.core.privacy_category\",\n            \"tag_value\": \"QUASI_IDENTIFIER\"\n          }\n        ]\n      },\n      \"valid_value_ratio\": 1\n    },\n    \"STATUS\": {\n      \"alternates\": []\n    },\n    \"_BATCH_ID\": {\n      \"alternates\": []\n    },\n    \"_LOADED_AT\": {\n      \"alternates\": []\n    }\n  }\n}"
 }
]

B2_CLEAR_READER = [
 {
  "MEMBER_ID": "M-01030",
  "FIRST_NAME": "Amelia",
  "EMAIL": "member1030@example.co.uk",
  "DATE_OF_BIRTH": "1972-08-30",
  "HEALTH_NOTES": "Asthma - inhaler on poolside"
 },
 {
  "MEMBER_ID": "M-01043",
  "FIRST_NAME": "Amelia",
  "EMAIL": "member1043@example.co.uk",
  "DATE_OF_BIRTH": "1967-03-10",
  "HEALTH_NOTES": "Asthma - inhaler on poolside"
 },
 {
  "MEMBER_ID": "M-01048",
  "FIRST_NAME": "Isla",
  "EMAIL": "member1048@example.co.uk",
  "DATE_OF_BIRTH": "1986-12-13",
  "HEALTH_NOTES": "Recent knee surgery - low impact only"
 }
]

B2_CROSS_REGION = [
 {
  "key": "CORTEX_ENABLED_CROSS_REGION",
  "value": "ANY_REGION",
  "default": "DISABLED",
  "level": "ACCOUNT"
 }
]

B2_ERASE = [
 {
  "ERASE_MEMBER": "{\n  \"attendance_deleted\": 6,\n  \"bookings_deleted\": 8,\n  \"member_rows\": 1,\n  \"payments_pseudonymised\": 3\n}"
 }
]

B2_ERASURE_EVAL = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ERASED_MEMBERS_STILL_PRESENT",
  "EXPECTATION_NAME": "ERASURE_COMPLETE",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

B2_GDPR_TAGS = [
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "contact"
 },
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "EMAIL",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "special_category"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "explicit_consent"
 },
 {
  "COLUMN_NAME": "HEALTH_NOTES",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "30"
 },
 {
  "COLUMN_NAME": "MARKETING_CONSENT",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "behavioural"
 },
 {
  "COLUMN_NAME": "MARKETING_CONSENT",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "consent"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "identifier"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "MEMBER_ID",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "GDPR_CATEGORY",
  "TAG_VALUE": "contact"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "LAWFUL_BASIS",
  "TAG_VALUE": "contract"
 },
 {
  "COLUMN_NAME": "PHONE",
  "TAG_NAME": "RETENTION_DAYS",
  "TAG_VALUE": "730"
 }
]

B2_MASKED_OWNER = [
 {
  "MEMBER_ID": "M-01000",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1970-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01001",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1982-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 },
 {
  "MEMBER_ID": "M-01002",
  "FIRST_NAME": "*** MASKED ***",
  "EMAIL": "*****@example.co.uk",
  "DATE_OF_BIRTH": "1997-01-01",
  "HEALTH_NOTES": "*** MASKED ***"
 }
]

B2_REQUESTS = [
 {
  "OPERATOR_ID": "CUST_NIELS",
  "MEMBER_ID": "M-01042",
  "REQUEST_TYPE": "ERASURE",
  "COMPLETED": True,
  "EVIDENCE": "{\n  \"attendance_deleted\": 6,\n  \"bookings_deleted\": 8,\n  \"member_rows\": 1,\n  \"payments_pseudonymised\": 3,\n  \"token\": \"ERASED-96235932dc8ea9c1\"\n}"
 },
 {
  "OPERATOR_ID": "CUST_NIELS",
  "MEMBER_ID": "M-01043",
  "REQUEST_TYPE": "SAR",
  "COMPLETED": True,
  "EVIDENCE": "[\n  \"MEMBERS__MEMBER\",\n  \"MEMBERS__MEMBERSHIP\",\n  \"SYSTEM__ATTENDANCE\",\n  \"SYSTEM__BOOKING\",\n  \"SYSTEM__PAYMENT\"\n]"
 }
]

B2_RETENTION = [
 {
  "name": "MEMBERS__MEMBER",
  "retention_time": "1",
  "change_tracking": "ON"
 }
]

B2_SAR = [
 {
  "SAR_EXPORT": "{\n  \"data\": {\n    \"MEMBERS__MEMBER\": [\n      {\n        \"DATE_OF_BIRTH\": \"1967-03-10\",\n        \"EMAIL\": \"member1043@example.co.uk\",\n        \"FIRST_NAME\": \"Amelia\",\n        \"HEALTH_NOTES\": \"Asthma - inhaler on poolside\",\n        \"HOME_SITE_ID\": \"S01\",\n        \"JOINED_ON\": \"2023-06-04\",\n        \"LAST_ACTIVITY_AT\": \"2026-10-11 06:35:31.298 -0700\",\n        \"LAST_NAME\": \"Smith\",\n        \"MARKETING_CONSENT\": False,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"PHONE\": \"07700 938200\",\n        \"POSTCODE\": \"OX1 4AB\",\n        \"STATUS\": \"ACTIVE\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:31.298 -0700\"\n      }\n    ],\n    \"MEMBERS__MEMBERSHIP\": [\n      {\n        \"LAST_PAID_ON\": \"2026-10-05\",\n        \"MEMBERSHIP_ID\": \"MS-01043\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"MONTHLY_FEE\": 49.99,\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"PLAN_NAME\": \"Premium Plus\",\n        \"START_DATE\": \"2023-06-04\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:32.048 -0700\"\n      }\n    ],\n    \"SYSTEM__ATTENDANCE\": [\n      {\n        \"ATTENDANCE_ID\": \"AT-000206\",\n        \"BOOKING_ID\": \"BK-000206\",\n        \"CHECKED_IN_AT\": \"2026-10-12 16:55:32.758 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:33.348 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-003371\",\n        \"BOOKING_ID\": \"BK-003371\",\n        \"CHECKED_IN_AT\": \"2026-09-21 12:34:32.758 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:33.348 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-006995\",\n        \"BOOKING_ID\": \"BK-006995\",\n        \"CHECKED_IN_AT\": \"2026-10-06 01:01:32.758 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:33.348 -0700\"\n      },\n      {\n        \"ATTENDANCE_ID\": \"AT-008122\",\n        \"BOOKING_ID\": \"BK-008122\",\n        \"CHECKED_IN_AT\": \"2026-10-11 07:14:32.758 -0700\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:33.348 -0700\"\n      }\n    ],\n    \"SYSTEM__BOOKING\": [\n      {\n        \"ACTIVITY_ID\": \"A00465\",\n        \"BOOKED_AT\": \"2026-10-12 16:50:32.758 -0700\",\n        \"BOOKING_ID\": \"BK-000206\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:32.758 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00246\",\n        \"BOOKED_AT\": \"2026-09-21 12:29:32.758 -0700\",\n        \"BOOKING_ID\": \"BK-003371\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:32.758 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00459\",\n        \"BOOKED_AT\": \"2026-10-06 00:56:32.758 -0700\",\n        \"BOOKING_ID\": \"BK-006995\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:32.758 -0700\"\n      },\n      {\n        \"ACTIVITY_ID\": \"A00566\",\n        \"BOOKED_AT\": \"2026-10-11 07:09:32.758 -0700\",\n        \"BOOKING_ID\": \"BK-008122\",\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:32.758 -0700\"\n      }\n    ],\n    \"SYSTEM__PAYMENT\": [\n      {\n        \"AMOUNT\": 49.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"PAYMENT_DATE\": \"2026-10-05\",\n        \"PAYMENT_ID\": \"PY-0001691\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:34.037 -0700\"\n      },\n      {\n        \"AMOUNT\": 24.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"PAYMENT_DATE\": \"2026-10-07\",\n        \"PAYMENT_ID\": \"PY-0001885\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:34.037 -0700\"\n      },\n      {\n        \"AMOUNT\": 24.99,\n        \"MEMBER_ID\": \"M-01043\",\n        \"OPERATOR_ID\": \"CUST_NIELS\",\n        \"PAYMENT_DATE\": \"2026-09-23\",\n        \"PAYMENT_ID\": \"PY-0003635\",\n        \"PAYMENT_TYPE\": \"PAYMENT\",\n        \"_BATCH_ID\": \"B-SEED\",\n        \"_LOADED_AT\": \"2026-10-16 06:35:34.037 -0700\"\n      }\n    ]\n  },\n  \"generated_at\": \"2026-10-16 06:58:06.892 -0700\",\n  \"member_id\": \"M-01043\",\n  \"note\": \"REPORTING dynamic tables hold aggregates only (no member_id)\",\n  \"operator\": \"CUST_NIELS\"\n}"
 }
]

B2_SV_DESCRIBE = [
 {
  "object_kind": None,
  "object_name": None,
  "property": "COMMENT",
  "property_value": "Nova Gold layer for operator CUST_NIELS"
 },
 {
  "object_kind": "CUSTOM_INSTRUCTION",
  "object_name": None,
  "property": "AI_SQL_GENERATION",
  "property_value": "Unless the user says otherwise, \"active members\" means the active_members metric (source status)."
 },
 {
  "object_kind": "AI_VERIFIED_QUERY",
  "object_name": "VQ_ACTIVE_MEMBERS",
  "property": "QUESTION",
  "property_value": "How many active members do we have?"
 },
 {
  "object_kind": "AI_VERIFIED_QUERY",
  "object_name": "VQ_ACTIVE_MEMBERS",
  "property": "SQL",
  "property_value": "SELECT COUNT_IF(last_paid_on >= DATEADD(day, -35, CURRENT_DATE())) AS active_members FROM GLADSTONE_DQ_LAB.CUST_NIELS.MEMBERS__MEMBERSHIP"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LAB"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "CUST_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__ACTIVE_MEMBERS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "AM",
  "property": "PRIMARY_KEY",
  "property_value": "[\"SITE_ID\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "TABLE",
  "property_value": "AM"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "EXPRESSION",
  "property_value": "SUM(am.active_members)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(25,0)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "SYNONYMS",
  "property_value": "[\"members\",\"active members\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "COMMENT",
  "property_value": "Members whose source status is ACTIVE"
 },
 {
  "object_kind": "METRIC",
  "object_name": "ACTIVE_MEMBERS",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "TABLE",
  "property_value": "AM"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "EXPRESSION",
  "property_value": "am.site_id"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "COMMENT",
  "property_value": "Site"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "SITE_ID",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LAB"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "CUST_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "BASE_TABLE_NAME",
  "property_value": "MEMBERS__MEMBERSHIP"
 },
 {
  "object_kind": "TABLE",
  "object_name": "MS",
  "property": "PRIMARY_KEY",
  "property_value": "[\"MEMBERSHIP_ID\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "TABLE",
  "property_value": "MS"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "EXPRESSION",
  "property_value": "COUNT_IF(ms.last_paid_on >= DATEADD(day, -35, CURRENT_DATE()))"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(13,0)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "COMMENT",
  "property_value": "Members who paid in the last 35 days (finance definition of active)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "PAID_MEMBERS_35D",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "TABLE",
  "property_value": "MS"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "EXPRESSION",
  "property_value": "ms.plan_name"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "COMMENT",
  "property_value": "Membership plan"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PLAN_NAME",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LAB"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "CUST_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__DAILY_REVENUE"
 },
 {
  "object_kind": "TABLE",
  "object_name": "REV",
  "property": "PRIMARY_KEY",
  "property_value": "[\"PAYMENT_DATE\"]"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "TABLE",
  "property_value": "REV"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "EXPRESSION",
  "property_value": "SUM(rev.net_revenue)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(34,2)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "COMMENT",
  "property_value": "Payments minus refunds, GBP"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NET_REVENUE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "TABLE",
  "property_value": "REV"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "EXPRESSION",
  "property_value": "rev.payment_date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "DATA_TYPE",
  "property_value": "DATE"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "COMMENT",
  "property_value": "Payment date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "PAYMENT_DATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_DATABASE_NAME",
  "property_value": "GLADSTONE_DQ_LAB"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_SCHEMA_NAME",
  "property_value": "CUST_NIELS"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "BASE_TABLE_NAME",
  "property_value": "REPORTING__CLASS_UTILISATION"
 },
 {
  "object_kind": "TABLE",
  "object_name": "UTIL",
  "property": "PRIMARY_KEY",
  "property_value": "[\"ACTIVITY_ID\"]"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "EXPRESSION",
  "property_value": "util.class_date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "DATA_TYPE",
  "property_value": "DATE"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "COMMENT",
  "property_value": "Class date"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_DATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "EXPRESSION",
  "property_value": "util.class_name"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "COMMENT",
  "property_value": "Class type"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_NAME",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "EXPRESSION",
  "property_value": "util.site_id"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "DATA_TYPE",
  "property_value": "VARCHAR(16777216)"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "COMMENT",
  "property_value": "Site of the class"
 },
 {
  "object_kind": "DIMENSION",
  "object_name": "CLASS_SITE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "EXPRESSION",
  "property_value": "DIV0(SUM(util.bookings) - SUM(util.attended), SUM(util.bookings)) * 100"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(38,6)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "COMMENT",
  "property_value": "Booked but did not attend, percent"
 },
 {
  "object_kind": "METRIC",
  "object_name": "NO_SHOW_RATE",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "TABLE",
  "property_value": "UTIL"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "EXPRESSION",
  "property_value": "DIV0(SUM(util.attended), SUM(util.capacity)) * 100"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "DATA_TYPE",
  "property_value": "NUMBER(38,6)"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "COMMENT",
  "property_value": "Attended places as a percentage of capacity"
 },
 {
  "object_kind": "METRIC",
  "object_name": "UTILISATION_PCT",
  "property": "ACCESS_MODIFIER",
  "property_value": "PUBLIC"
 }
]

B2_TIMETRAVEL = [
 {
  "STILL_IN_TIME_TRAVEL": 1
 }
]

B2_TOM_AFTER = [
 {
  "OPERATOR_ID": "CUST_TOM",
  "N": 2000
 }
]

B2_TOM_BEFORE = [
 {
  "OPERATOR_ID": "CUST_TOM",
  "N": 2000
 },
 {
  "OPERATOR_ID": "CUST_NEIGHBOUR",
  "N": 50
 }
]

B2_VIEWER_ROWS = [
 {
  "ROWS_VISIBLE": 2000,
  "FOREIGN_ROWS_VISIBLE": 0
 }
]

D_AMY_FRESH = [
 {
  "LAST_PAYMENT_LOADED": "2026-10-16 06:40:18",
  "SECONDS_SINCE": 329
 }
]

D_AMY_TASK = [
 {
  "name": "TSK_BIFROST_MERGE",
  "schedule": "1 MINUTE",
  "state": "suspended"
 }
]

D_AMY_TASKHIST = [
 {
  "NAME": "TSK_BIFROST_MERGE",
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 06:40:16",
  "COMPLETED_TIME": "2026-10-16 06:40:21",
  "ERROR_MESSAGE": None
 },
 {
  "NAME": "TSK_BIFROST_MERGE",
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 06:39:16",
  "COMPLETED_TIME": "2026-10-16 06:39:20",
  "ERROR_MESSAGE": None
 },
 {
  "NAME": "TSK_BIFROST_MERGE",
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 06:38:16",
  "COMPLETED_TIME": "2026-10-16 06:38:19",
  "ERROR_MESSAGE": None
 }
]

D_LENA_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1890,
  "PAID_MEMBERS_35D": 1520
 }
]

D_LENA_ROWS = [
 {
  "MEMBER_ID": "M-01001",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-07-04",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01004",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-10-03",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01020",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-06-20",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01021",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-10-10",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01022",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-07-11",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01036",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-08-18",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01039",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-09-30",
  "_BATCH_ID": "B-STATUS-01"
 },
 {
  "MEMBER_ID": "M-01042",
  "STATUS": "ACTIVE",
  "LEFT_ON": "2026-09-13",
  "_BATCH_ID": "B-STATUS-01"
 }
]

D_NIELS_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1748,
  "PAID_MEMBERS_35D": 1520
 }
]

D_NIELS_BATCH = [
 {
  "BATCH_ID": "B-REPLAY-01",
  "TABLE_NAME": "MEMBERS__MEMBER",
  "TIMES_APPLIED": 2,
  "FIRST_LOADED": "2026-10-16 06:40:57",
  "LAST_LOADED": "2026-10-16 06:40:57"
 }
]

D_NIELS_SCAN = [
 {
  "MEMBER_ID": "M-01000",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Harry",
  "LAST_NAME": "Evans",
  "EMAIL": "member1000@example.co.uk",
  "PHONE": "07700 982865",
  "DATE_OF_BIRTH": "1970-02-27",
  "POSTCODE": "OX14 6AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-05-04",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-08-24 13:35:31",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 06:40:56"
 },
 {
  "MEMBER_ID": "M-01000",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Harry",
  "LAST_NAME": "Evans",
  "EMAIL": "member1000@example.co.uk",
  "PHONE": "07700 982865",
  "DATE_OF_BIRTH": "1970-02-27",
  "POSTCODE": "OX14 6AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-05-04",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-08-24 13:35:31",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 06:35:31"
 },
 {
  "MEMBER_ID": "M-01002",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S01",
  "FIRST_NAME": "Amelia",
  "LAST_NAME": "Evans",
  "EMAIL": "member1002@example.co.uk",
  "PHONE": "07700 948460",
  "DATE_OF_BIRTH": "1997-12-17",
  "POSTCODE": "OX1 7AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-07-18",
  "LEFT_ON": None,
  "MARKETING_CONSENT": False,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-13 18:35:31",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 06:40:56"
 },
 {
  "MEMBER_ID": "M-01002",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S01",
  "FIRST_NAME": "Amelia",
  "LAST_NAME": "Evans",
  "EMAIL": "member1002@example.co.uk",
  "PHONE": "07700 948460",
  "DATE_OF_BIRTH": "1997-12-17",
  "POSTCODE": "OX1 7AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-07-18",
  "LEFT_ON": None,
  "MARKETING_CONSENT": False,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-13 18:35:31",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 06:35:31"
 },
 {
  "MEMBER_ID": "M-01003",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S02",
  "FIRST_NAME": "Jack",
  "LAST_NAME": "Evans",
  "EMAIL": "member1003@example.co.uk",
  "PHONE": "07700 906969",
  "DATE_OF_BIRTH": "1960-04-16",
  "POSTCODE": "OX14 8AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-01-21",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-09 05:35:31",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 06:40:56"
 },
 {
  "MEMBER_ID": "M-01003",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S02",
  "FIRST_NAME": "Jack",
  "LAST_NAME": "Evans",
  "EMAIL": "member1003@example.co.uk",
  "PHONE": "07700 906969",
  "DATE_OF_BIRTH": "1960-04-16",
  "POSTCODE": "OX14 8AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-01-21",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-09 05:35:31",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 06:35:31"
 },
 {
  "MEMBER_ID": "M-01005",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Mia",
  "LAST_NAME": "Thomas",
  "EMAIL": "member1005@example.co.uk",
  "PHONE": "07700 914176",
  "DATE_OF_BIRTH": "1961-10-11",
  "POSTCODE": "OX1 3AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2023-06-28",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-28 22:35:31",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 06:35:31"
 },
 {
  "MEMBER_ID": "M-01005",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Mia",
  "LAST_NAME": "Thomas",
  "EMAIL": "member1005@example.co.uk",
  "PHONE": "07700 914176",
  "DATE_OF_BIRTH": "1961-10-11",
  "POSTCODE": "OX1 3AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2023-06-28",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-09-28 22:35:31",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 06:40:56"
 },
 {
  "MEMBER_ID": "M-01006",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Ava",
  "LAST_NAME": "Brown",
  "EMAIL": "member1006@example.co.uk",
  "PHONE": "07700 956634",
  "DATE_OF_BIRTH": "1995-06-07",
  "POSTCODE": "OX16 9AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-01-25",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-10-03 04:35:31",
  "_BATCH_ID": "B-SEED",
  "_LOADED_AT": "2026-10-16 06:35:31"
 },
 {
  "MEMBER_ID": "M-01006",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "FIRST_NAME": "Ava",
  "LAST_NAME": "Brown",
  "EMAIL": "member1006@example.co.uk",
  "PHONE": "07700 956634",
  "DATE_OF_BIRTH": "1995-06-07",
  "POSTCODE": "OX16 9AB",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-01-25",
  "LEFT_ON": None,
  "MARKETING_CONSENT": True,
  "HEALTH_NOTES": None,
  "LAST_ACTIVITY_AT": "2026-10-03 04:35:31",
  "_BATCH_ID": "B-REPLAY-01",
  "_LOADED_AT": "2026-10-16 06:40:56"
 }
]

D_RAJ_BATCH = [
 {
  "_BATCH_ID": "B-SIGNBUG-01",
  "N": 40,
  "TOTAL": "-10000.00"
 }
]

D_RAJ_REVENUE = [
 {
  "PAYMENT_DATE": "2026-10-16",
  "NET_REVENUE": "1971.66",
  "REFUNDS": 8,
  "TRANSACTIONS": 390
 },
 {
  "PAYMENT_DATE": "2026-10-15",
  "NET_REVENUE": "7283.07",
  "REFUNDS": 11,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-14",
  "NET_REVENUE": "7168.03",
  "REFUNDS": 9,
  "TRANSACTIONS": 215
 }
]

D_RAJ_SCAN = [
 {
  "PAYMENT_ID": "PY-NEG-0",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01000",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-1",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01001",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-2",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01002",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-3",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01003",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-4",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01004",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-5",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01005",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-6",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01006",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 },
 {
  "PAYMENT_ID": "PY-NEG-7",
  "OPERATOR_ID": "CUST_RAJ",
  "MEMBER_ID": "M-01007",
  "PAYMENT_DATE": "2026-10-16",
  "AMOUNT": "-250.00",
  "PAYMENT_TYPE": "PAYMENT",
  "_BATCH_ID": "B-SIGNBUG-01",
  "_LOADED_AT": "2026-10-16 06:40:58"
 }
]

D_SARA_ORPHANS = [
 {
  "ATTENDANCE_ID": "AT-GHOST-0",
  "BOOKING_ID": "BK-GHOST-0",
  "MEMBER_ID": "M-01000",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-1",
  "BOOKING_ID": "BK-GHOST-1",
  "MEMBER_ID": "M-01001",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-10",
  "BOOKING_ID": "BK-GHOST-10",
  "MEMBER_ID": "M-01010",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-11",
  "BOOKING_ID": "BK-GHOST-11",
  "MEMBER_ID": "M-01011",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-12",
  "BOOKING_ID": "BK-GHOST-12",
  "MEMBER_ID": "M-01012",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-13",
  "BOOKING_ID": "BK-GHOST-13",
  "MEMBER_ID": "M-01013",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-14",
  "BOOKING_ID": "BK-GHOST-14",
  "MEMBER_ID": "M-01014",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 },
 {
  "ATTENDANCE_ID": "AT-GHOST-15",
  "BOOKING_ID": "BK-GHOST-15",
  "MEMBER_ID": "M-01015",
  "CHECKED_IN_AT": "2026-10-16 06:40:59"
 }
]

D_TOM_OPERATORS = [
 {
  "OPERATOR_ID": "CUST_TOM",
  "N": 2000,
  "BATCH": "B-SEED"
 },
 {
  "OPERATOR_ID": "CUST_NEIGHBOUR",
  "N": 50,
  "BATCH": "B-MISROUTE-01"
 }
]

E_AMY_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_AMY_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_AMY_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 346,
  "EXPECTATION_VIOLATED": True
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_LENA_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 292,
  "EXPECTATION_VIOLATED": True
 }
]

E_LENA_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_LENA_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 7,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_NIELS_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 150,
  "EXPECTATION_VIOLATED": True
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_NIELS_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_NIELS_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 53,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_RAJ_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_RAJ_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_RAJ_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 36,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 40,
  "EXPECTATION_VIOLATED": True
 }
]

E_SARA_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_SARA_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 60,
  "EXPECTATION_VIOLATED": True
 }
]

E_SARA_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 24,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_TOM_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 50,
  "EXPECTATION_VIOLATED": True
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_TOM_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

E_TOM_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 17,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

F_ANSWER_KEY = [
 {
  "SHORT_NAME": "NIELS",
  "SCHEMA_NAME": "CUST_NIELS",
  "FAULT_CODE": "BIFROST_REPLAY",
  "DESCRIPTION": "Merge batch B-REPLAY-01 applied twice: 150 duplicate member rows; active members inflated",
  "EXPECTED_DETECTION": "DUPLICATE_COUNT(member_id) > 0 on MEMBERS__MEMBER; batch_id appears twice in _SYNC_META__MERGE_BATCH"
 },
 {
  "SHORT_NAME": "AMY",
  "SCHEMA_NAME": "CUST_AMY",
  "FAULT_CODE": "MERGE_TASK_STALLED",
  "DESCRIPTION": "Bifrost merge task suspended: no new payments or bookings; REPORTING goes stale",
  "EXPECTED_DETECTION": "FRESHNESS on SYSTEM__PAYMENT breaches expectation; TASK_HISTORY shows no runs; no new _SYNC_META batches"
 },
 {
  "SHORT_NAME": "RAJ",
  "SCHEMA_NAME": "CUST_RAJ",
  "FAULT_CODE": "REFUND_SIGN_FLIP",
  "DESCRIPTION": "Refunds arrived as negative PAYMENT rows (batch B-SIGNBUG-01); today's net revenue collapses",
  "EXPECTED_DETECTION": "NEGATIVE_COUNT(amount) > 0 on SYSTEM__PAYMENT; net_revenue drop on REPORTING__DAILY_REVENUE"
 },
 {
  "SHORT_NAME": "SARA",
  "SCHEMA_NAME": "CUST_SARA",
  "FAULT_CODE": "ORPHAN_ATTENDANCE",
  "DESCRIPTION": "60 turnstile check-ins with no matching booking (booking sync partially failed)",
  "EXPECTED_DETECTION": "REFERENTIAL_INTEGRITY_COUNT(booking_id -> SYSTEM__BOOKING) > 0 on SYSTEM__ATTENDANCE"
 },
 {
  "SHORT_NAME": "TOM",
  "SCHEMA_NAME": "CUST_TOM",
  "FAULT_CODE": "TENANT_LEAK",
  "DESCRIPTION": "50 member rows from another operator (CUST_NEIGHBOUR) routed into this operator",
  "EXPECTED_DETECTION": "DQ_COMMON.FOREIGN_OPERATOR_ROWS(operator_id) > 0 on MEMBERS__MEMBER"
 },
 {
  "SHORT_NAME": "LENA",
  "SCHEMA_NAME": "CUST_LENA",
  "FAULT_CODE": "STATUS_DRIFT",
  "DESCRIPTION": "Cancelled members re-sent as ACTIVE; Nova's active members disagrees with the verified (paid in 35 days) query",
  "EXPECTED_DETECTION": "Gold check: active_members metric vs vq_active_members gap jumps from ~6% to ~25%; ACCEPTED_VALUES / left_on not null with ACTIVE"
 }
]

S1_COUNTS = [
 {
  "T": "MEMBERS__MEMBER",
  "N": 2000
 },
 {
  "T": "MEMBERS__MEMBERSHIP",
  "N": 2000
 },
 {
  "T": "SHARED__SITE",
  "N": 3
 },
 {
  "T": "SHARED__ACTIVITY",
  "N": 600
 },
 {
  "T": "SYSTEM__BOOKING",
  "N": 9010
 },
 {
  "T": "SYSTEM__ATTENDANCE",
  "N": 7401
 },
 {
  "T": "SYSTEM__PAYMENT",
  "N": 6015
 },
 {
  "T": "_SYNC_META__MERGE_BATCH",
  "N": 5
 }
]

S1_DTS = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 3
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 600
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "target_lag": "1 minute",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE",
  "rows": 28
 }
]

S1_MEMBERS_SAMPLE = [
 {
  "MEMBER_ID": "M-01000",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-05-04",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01001",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "STATUS": "CANCELLED",
  "JOINED_ON": "2026-03-16",
  "LEFT_ON": "2026-07-04",
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01002",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S01",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-07-18",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01003",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S02",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2024-01-21",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01004",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S02",
  "STATUS": "CANCELLED",
  "JOINED_ON": "2024-04-06",
  "LEFT_ON": "2026-10-03",
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01005",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2023-06-28",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01006",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S03",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-01-25",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 },
 {
  "MEMBER_ID": "M-01007",
  "OPERATOR_ID": "CUST_NIELS",
  "HOME_SITE_ID": "S01",
  "STATUS": "ACTIVE",
  "JOINED_ON": "2026-07-16",
  "LEFT_ON": None,
  "_BATCH_ID": "B-SEED"
 }
]

S1_OBJECTS = [
 {
  "name": "MEMBERS__MEMBER",
  "kind": "TABLE",
  "comment": "Bronze MEMBERS: member master (synthetic personal data)"
 },
 {
  "name": "MEMBERS__MEMBERSHIP",
  "kind": "TABLE",
  "comment": "Bronze MEMBERS: membership contracts"
 },
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "kind": "TABLE",
  "comment": "Silver REPORTING: active members by site (status-based definition)"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "kind": "TABLE",
  "comment": "Silver REPORTING: class bookings, attendance and capacity"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "kind": "TABLE",
  "comment": "Silver REPORTING: net revenue per day"
 },
 {
  "name": "SHARED__ACTIVITY",
  "kind": "TABLE",
  "comment": "Bronze SHARED: scheduled classes"
 },
 {
  "name": "SHARED__SITE",
  "kind": "TABLE",
  "comment": "Bronze SHARED: operator sites"
 },
 {
  "name": "SV_OPERATOR_KPIS",
  "kind": "VIEW",
  "comment": "Nova Gold layer for operator CUST_NIELS"
 },
 {
  "name": "SYSTEM__ATTENDANCE",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: turnstile / class check-ins"
 },
 {
  "name": "SYSTEM__BOOKING",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: class bookings"
 },
 {
  "name": "SYSTEM__PAYMENT",
  "kind": "TABLE",
  "comment": "Bronze SYSTEM: payments and refunds"
 },
 {
  "name": "_SYNC_META__MERGE_BATCH",
  "kind": "TABLE",
  "comment": "Sync metadata: one row per merge batch"
 }
]

S1_REVENUE = [
 {
  "PAYMENT_DATE": "2026-10-16",
  "NET_REVENUE": "7772.86",
  "REFUNDS": 8,
  "TRANSACTIONS": 230
 },
 {
  "PAYMENT_DATE": "2026-10-15",
  "NET_REVENUE": "7283.07",
  "REFUNDS": 11,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-14",
  "NET_REVENUE": "7168.03",
  "REFUNDS": 9,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-13",
  "NET_REVENUE": "7202.99",
  "REFUNDS": 7,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-12",
  "NET_REVENUE": "7657.93",
  "REFUNDS": 4,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-11",
  "NET_REVENUE": "7767.89",
  "REFUNDS": 2,
  "TRANSACTIONS": 215
 },
 {
  "PAYMENT_DATE": "2026-10-10",
  "NET_REVENUE": "7602.89",
  "REFUNDS": 2,
  "TRANSACTIONS": 215
 }
]

S1_TASKS = [
 {
  "name": "TSK_BIFROST_MERGE",
  "schedule": "1 MINUTE",
  "state": "started",
  "definition": "CALL GLADSTONE_DQ_LAB.ADMIN.BIFROST_MERGE('CUST_NIELS')"
 }
]

S1_TWO_ACTIVE = [
 {
  "ACTIVE_MEMBERS": 1598,
  "PAID_MEMBERS_35D": 1520
 }
]

S1_UTIL = [
 {
  "CLASS_NAME": "Aqua Fit",
  "UTILISATION_PCT": "57.206400",
  "NO_SHOW_RATE": "18.089200"
 },
 {
  "CLASS_NAME": "HIIT",
  "UTILISATION_PCT": "57.363800",
  "NO_SHOW_RATE": "17.740200"
 },
 {
  "CLASS_NAME": "Pilates",
  "UTILISATION_PCT": "52.741000",
  "NO_SHOW_RATE": "17.210700"
 },
 {
  "CLASS_NAME": "Spin",
  "UTILISATION_PCT": "52.292000",
  "NO_SHOW_RATE": "17.976000"
 },
 {
  "CLASS_NAME": "Swim Lessons",
  "UTILISATION_PCT": "56.311300",
  "NO_SHOW_RATE": "17.689200"
 },
 {
  "CLASS_NAME": "Yoga",
  "UTILISATION_PCT": "60.782000",
  "NO_SHOW_RATE": "19.339600"
 }
]

S2_ATTACHED = [
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2287655\",\"name\":\"STATUS\"},{\"domain\":\"COLUMN\",\"id\":\"2287649\",\"name\":\"LEFT_ON\"}]",
  "SCHEDULE": "*/5 * * * * UTC",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2287652\",\"name\":\"OPERATOR_ID\"}]",
  "SCHEDULE": "*/5 * * * * UTC",
  "SCHEDULE_STATUS": "STARTED"
 },
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "REF_ARGUMENTS": "[{\"domain\":\"COLUMN\",\"id\":\"2287651\",\"name\":\"MEMBER_ID\"}]",
  "SCHEDULE": "*/5 * * * * UTC",
  "SCHEDULE_STATUS": "STARTED"
 }
]

S2_CLEAN_MEMBERS__MEMBER = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S2_CLEAN_SYSTEM__ATTENDANCE = [
 {
  "METRIC_NAME": "REFERENTIAL_INTEGRITY_COUNT",
  "EXPECTATION_NAME": "NO_ORPHAN_CHECKINS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S2_CLEAN_SYSTEM__PAYMENT = [
 {
  "METRIC_NAME": "FRESHNESS",
  "EXPECTATION_NAME": "PAYMENTS_FRESH_3MIN",
  "EXPECTATION_EXPRESSION": "VALUE < 180",
  "VALUE": 19,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "NEGATIVE_COUNT",
  "EXPECTATION_NAME": "NO_NEGATIVE_AMOUNTS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S3_DT_HISTORY = [
 {
  "NAME": "REPORTING__CLASS_UTILISATION",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "INCREMENTAL",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:47:08",
  "STATE_MESSAGE": None
 },
 {
  "NAME": "REPORTING__DAILY_REVENUE",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "INCREMENTAL",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:47:08",
  "STATE_MESSAGE": None
 },
 {
  "NAME": "REPORTING__ACTIVE_MEMBERS",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "NO_DATA",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:47:08",
  "STATE_MESSAGE": None
 },
 {
  "NAME": "REPORTING__ACTIVE_MEMBERS",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "NO_DATA",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:46:20",
  "STATE_MESSAGE": None
 },
 {
  "NAME": "REPORTING__DAILY_REVENUE",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "INCREMENTAL",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:46:20",
  "STATE_MESSAGE": None
 },
 {
  "NAME": "REPORTING__CLASS_UTILISATION",
  "STATE": "SUCCEEDED",
  "REFRESH_ACTION": "INCREMENTAL",
  "REFRESH_TRIGGER": "SCHEDULED",
  "DATA_TIMESTAMP": "2026-10-16 06:46:20",
  "STATE_MESSAGE": None
 }
]

S3_FAILING = [
 {
  "TABLE_NAME": "MEMBERS__MEMBER",
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "VALUE": "150",
  "MEASUREMENT_TIME": "2026-10-16 06:45:09"
 }
]

S4_AFTER_FIX_EVAL = [
 {
  "METRIC_NAME": "DUPLICATE_COUNT",
  "EXPECTATION_NAME": "NO_DUPLICATE_MEMBERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "FOREIGN_OPERATOR_ROWS",
  "EXPECTATION_NAME": "NO_OTHER_OPERATOR_ROWS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 },
 {
  "METRIC_NAME": "ACTIVE_BUT_LEFT",
  "EXPECTATION_NAME": "NO_ACTIVE_LEAVERS",
  "EXPECTATION_EXPRESSION": "VALUE = 0",
  "VALUE": 0,
  "EXPECTATION_VIOLATED": False
 }
]

S4_CB_CLOSED = [
 {
  "NAME": "TSK_DQ_CIRCUIT_BREAKER",
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 06:51:02",
  "RETURN_VALUE": "CLOSED: Bronze clean"
 },
 {
  "NAME": "TSK_DQ_CIRCUIT_BREAKER",
  "STATE": "FAILED",
  "SCHEDULED_TIME": "2026-10-16 06:47:54",
  "RETURN_VALUE": None
 }
]

S4_CB_OPEN = [
 {
  "NAME": "TSK_DQ_CIRCUIT_BREAKER",
  "STATE": "SUCCEEDED",
  "SCHEDULED_TIME": "2026-10-16 06:54:18",
  "RETURN_VALUE": "OPEN: 1 failing Bronze check(s) - REPORTING frozen at last good state"
 }
]

S4_DTS_CLOSED = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 }
]

S4_DTS_OPEN = [
 {
  "name": "REPORTING__ACTIVE_MEMBERS",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "SUSPENDED"
 },
 {
  "name": "REPORTING__CLASS_UTILISATION",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "ACTIVE"
 },
 {
  "name": "REPORTING__DAILY_REVENUE",
  "refresh_mode": "INCREMENTAL",
  "scheduling_state": "SUSPENDED"
 }
]

S4_FIX_COUNT = [
 {
  "ROWS_REMOVED": 150
 }
]

S5_FLEET = [
 {
  "OPERATOR": "CUST_AMY",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.FRESHNESS()\"\n]",
  "LAST_MEASURED": "2026-10-16 06:45:47"
 },
 {
  "OPERATOR": "CUST_LENA",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.ACTIVE_BUT_LEFT(STATUS,LEFT_ON)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:45:16"
 },
 {
  "OPERATOR": "CUST_NIELS",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.DUPLICATE_COUNT(MEMBER_ID)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:45:47"
 },
 {
  "OPERATOR": "CUST_RAJ",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.NEGATIVE_COUNT(AMOUNT)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:46:00"
 },
 {
  "OPERATOR": "CUST_SARA",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__ATTENDANCE.REFERENTIAL_INTEGRITY_COUNT(BOOKING_ID)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:45:52"
 },
 {
  "OPERATOR": "CUST_TEST1_DCM",
  "CHECKS": 5,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.DUPLICATE_COUNT(MEMBER_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:43"
 },
 {
  "OPERATOR": "CUST_TEST2",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.FRESHNESS()\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:51"
 },
 {
  "OPERATOR": "CUST_TEST3",
  "CHECKS": 9,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.NEGATIVE_COUNT(AMOUNT)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:59"
 },
 {
  "OPERATOR": "CUST_TEST4",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__ATTENDANCE.REFERENTIAL_INTEGRITY_COUNT(BOOKING_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:54"
 },
 {
  "OPERATOR": "CUST_TEST5",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.FOREIGN_OPERATOR_ROWS(OPERATOR_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:47"
 },
 {
  "OPERATOR": "CUST_TEST6",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.ACTIVE_BUT_LEFT(STATUS,LEFT_ON)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:43"
 },
 {
  "OPERATOR": "CUST_TOM",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.FOREIGN_OPERATOR_ROWS(OPERATOR_ID)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:45:32"
 },
 {
  "OPERATOR": "CUST_TEST1",
  "CHECKS": 7,
  "FAILING_CHECKS": 0,
  "FAILING": "[]",
  "LAST_MEASURED": "2026-10-15 22:20:59"
 }
]

S5_FLEET_AFTER = [
 {
  "OPERATOR": "CUST_AMY",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.FRESHNESS()\"\n]",
  "LAST_MEASURED": "2026-10-16 06:50:49"
 },
 {
  "OPERATOR": "CUST_LENA",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.ACTIVE_BUT_LEFT(STATUS,LEFT_ON)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:50:57"
 },
 {
  "OPERATOR": "CUST_RAJ",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.NEGATIVE_COUNT(AMOUNT)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:50:57"
 },
 {
  "OPERATOR": "CUST_SARA",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__ATTENDANCE.REFERENTIAL_INTEGRITY_COUNT(BOOKING_ID)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:50:47"
 },
 {
  "OPERATOR": "CUST_TEST1_DCM",
  "CHECKS": 5,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.DUPLICATE_COUNT(MEMBER_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:43"
 },
 {
  "OPERATOR": "CUST_TEST2",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.FRESHNESS()\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:51"
 },
 {
  "OPERATOR": "CUST_TEST3",
  "CHECKS": 9,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__PAYMENT.NEGATIVE_COUNT(AMOUNT)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:59"
 },
 {
  "OPERATOR": "CUST_TEST4",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"SYSTEM__ATTENDANCE.REFERENTIAL_INTEGRITY_COUNT(BOOKING_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:54"
 },
 {
  "OPERATOR": "CUST_TEST5",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.FOREIGN_OPERATOR_ROWS(OPERATOR_ID)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:47"
 },
 {
  "OPERATOR": "CUST_TEST6",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.ACTIVE_BUT_LEFT(STATUS,LEFT_ON)\"\n]",
  "LAST_MEASURED": "2026-10-15 22:20:43"
 },
 {
  "OPERATOR": "CUST_TOM",
  "CHECKS": 7,
  "FAILING_CHECKS": 1,
  "FAILING": "[\n  \"MEMBERS__MEMBER.FOREIGN_OPERATOR_ROWS(OPERATOR_ID)\"\n]",
  "LAST_MEASURED": "2026-10-16 06:50:51"
 },
 {
  "OPERATOR": "CUST_NIELS",
  "CHECKS": 7,
  "FAILING_CHECKS": 0,
  "FAILING": "[]",
  "LAST_MEASURED": "2026-10-16 06:50:37"
 },
 {
  "OPERATOR": "CUST_TEST1",
  "CHECKS": 7,
  "FAILING_CHECKS": 0,
  "FAILING": "[]",
  "LAST_MEASURED": "2026-10-15 22:20:59"
 }
]

B2_CLASSIFY_JSON = {
 "classification_result": {
  "DATE_OF_BIRTH": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "QUASI_IDENTIFIER",
    "semantic_category": "DATE_OF_BIRTH",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "DATE_OF_BIRTH"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "QUASI_IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "EMAIL": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "EMAIL",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "EMAIL"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "FIRST_NAME": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "NAME",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "NAME"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "HEALTH_NOTES": {
   "alternates": []
  },
  "HOME_SITE_ID": {
   "alternates": []
  },
  "JOINED_ON": {
   "alternates": []
  },
  "LAST_ACTIVITY_AT": {
   "alternates": []
  },
  "LAST_NAME": {
   "alternates": [],
   "recommendation": {
    "confidence": "HIGH",
    "coverage": 1,
    "details": [],
    "privacy_category": "IDENTIFIER",
    "semantic_category": "NAME",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "NAME"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "LEFT_ON": {
   "alternates": []
  },
  "MARKETING_CONSENT": {
   "alternates": []
  },
  "MEMBER_ID": {
   "alternates": []
  },
  "OPERATOR_ID": {
   "alternates": []
  },
  "PHONE": {
   "alternates": []
  },
  "POSTCODE": {
   "alternates": [],
   "recommendation": {
    "confidence": "LOW",
    "coverage": 0.4645,
    "details": [
     {
      "coverage": 0.4645,
      "semantic_category": "UK_POSTAL_CODE"
     }
    ],
    "privacy_category": "QUASI_IDENTIFIER",
    "semantic_category": "POSTAL_CODE",
    "tags": [
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.semantic_category",
      "tag_value": "POSTAL_CODE"
     },
     {
      "tag_applied": False,
      "tag_name": "snowflake.core.privacy_category",
      "tag_value": "QUASI_IDENTIFIER"
     }
    ]
   },
   "valid_value_ratio": 1
  },
  "STATUS": {
   "alternates": []
  },
  "_BATCH_ID": {
   "alternates": []
  },
  "_LOADED_AT": {
   "alternates": []
  }
 }
}

B2_SAR_JSON = {
 "data": {
  "MEMBERS__MEMBER": [
   {
    "DATE_OF_BIRTH": "1967-03-10",
    "EMAIL": "member1043@example.co.uk",
    "FIRST_NAME": "Amelia",
    "HEALTH_NOTES": "Asthma - inhaler on poolside",
    "HOME_SITE_ID": "S01",
    "JOINED_ON": "2023-06-04",
    "LAST_ACTIVITY_AT": "2026-10-11 06:35:31.298 -0700",
    "LAST_NAME": "Smith",
    "MARKETING_CONSENT": False,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "PHONE": "07700 938200",
    "POSTCODE": "OX1 4AB",
    "STATUS": "ACTIVE",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 06:35:31.298 -0700"
   }
  ],
  "MEMBERS__MEMBERSHIP": [
   {
    "LAST_PAID_ON": "2026-10-05",
    "MEMBERSHIP_ID": "MS-01043",
    "MEMBER_ID": "M-01043",
    "MONTHLY_FEE": 49.99,
    "OPERATOR_ID": "CUST_NIELS",
    "PLAN_NAME": "Premium Plus",
    "START_DATE": "2023-06-04",
    "_LOADED_AT": "2026-10-16 06:35:32.048 -0700"
   }
  ],
  "SYSTEM__ATTENDANCE": [
   {
    "ATTENDANCE_ID": "AT-000206",
    "BOOKING_ID": "BK-000206",
    "CHECKED_IN_AT": "2026-10-12 16:55:32.758 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:33.348 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-003371",
    "BOOKING_ID": "BK-003371",
    "CHECKED_IN_AT": "2026-09-21 12:34:32.758 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:33.348 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-006995",
    "BOOKING_ID": "BK-006995",
    "CHECKED_IN_AT": "2026-10-06 01:01:32.758 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:33.348 -0700"
   },
   {
    "ATTENDANCE_ID": "AT-008122",
    "BOOKING_ID": "BK-008122",
    "CHECKED_IN_AT": "2026-10-11 07:14:32.758 -0700",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:33.348 -0700"
   }
  ],
  "SYSTEM__BOOKING": [
   {
    "ACTIVITY_ID": "A00465",
    "BOOKED_AT": "2026-10-12 16:50:32.758 -0700",
    "BOOKING_ID": "BK-000206",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:32.758 -0700"
   },
   {
    "ACTIVITY_ID": "A00246",
    "BOOKED_AT": "2026-09-21 12:29:32.758 -0700",
    "BOOKING_ID": "BK-003371",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:32.758 -0700"
   },
   {
    "ACTIVITY_ID": "A00459",
    "BOOKED_AT": "2026-10-06 00:56:32.758 -0700",
    "BOOKING_ID": "BK-006995",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:32.758 -0700"
   },
   {
    "ACTIVITY_ID": "A00566",
    "BOOKED_AT": "2026-10-11 07:09:32.758 -0700",
    "BOOKING_ID": "BK-008122",
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "_LOADED_AT": "2026-10-16 06:35:32.758 -0700"
   }
  ],
  "SYSTEM__PAYMENT": [
   {
    "AMOUNT": 49.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "PAYMENT_DATE": "2026-10-05",
    "PAYMENT_ID": "PY-0001691",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 06:35:34.037 -0700"
   },
   {
    "AMOUNT": 24.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "PAYMENT_DATE": "2026-10-07",
    "PAYMENT_ID": "PY-0001885",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 06:35:34.037 -0700"
   },
   {
    "AMOUNT": 24.99,
    "MEMBER_ID": "M-01043",
    "OPERATOR_ID": "CUST_NIELS",
    "PAYMENT_DATE": "2026-09-23",
    "PAYMENT_ID": "PY-0003635",
    "PAYMENT_TYPE": "PAYMENT",
    "_BATCH_ID": "B-SEED",
    "_LOADED_AT": "2026-10-16 06:35:34.037 -0700"
   }
  ]
 },
 "generated_at": "2026-10-16 06:58:06.892 -0700",
 "member_id": "M-01043",
 "note": "REPORTING dynamic tables hold aggregates only (no member_id)",
 "operator": "CUST_NIELS"
}

B2_ERASE_JSON = {
 "attendance_deleted": 6,
 "bookings_deleted": 8,
 "member_rows": 1,
 "payments_pseudonymised": 3
}

AGENT_QUESTION = 'How many active members do we have?'
AGENT_ANSWER = "You currently have **1,520 active members**.\n\nThis uses the active members measure (members whose last payment was within the past 35 days)."
AGENT_USED_VERIFIED_QUERY = True

B3_CREATE_OUT = "Creating DCM Project 'GLADSTONE_DQ_LAB.CUST_NIELS_DCM.OPERATOR_PIPELINE'\nDCM Project 'GLADSTONE_DQ_LAB.CUST_NIELS_DCM.OPERATOR_PIPELINE' successfully created."
B3_PLAN_OUT = "Uploading definition files\n  Creating temporary stage GLADSTONE_DQ_LAB.CUST_NIELS_DCM.DCM_OPERATOR_PIPELINE_1792159156_TMP_STAGE.\n  Local changes to be deployed:\n    added:    manifest.yml -> manifest.yml\n    added:    sources/definitions/bronze.sql -> sources/definitions/bronze.sql\n    added:    sources/definitions/expectations.sql -> sources/definitions/expectations.sql\n    added:    sources/definitions/reporting.sql -> sources/definitions/reporting.sql\n  Uploading files from local ./dcm_project/output/bundle directory to temporary stage.\n\nArtifacts saved to: ./dcm_project/out\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__ACTIVE_MEMBERS\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__DAILY_REVENUE\nCREATE   TABLE                GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER\nCREATE   TABLE                GLADSTONE_DQ_LAB.CUST_NIELS_DCM.SYSTEM__PAYMENT\nALTER    ROLE                 DQ_LAB_NIELS\n\nPlanned 5 entities (4 to create, 1 to alter, 0 to drop)."
B3_DEPLOY_OUT = "Uploading definition files\n  Creating temporary stage GLADSTONE_DQ_LAB.CUST_NIELS_DCM.DCM_OPERATOR_PIPELINE_1792159178_TMP_STAGE.\n  Local changes to be deployed:\n    added:    manifest.yml -> manifest.yml\n    added:    sources/definitions/bronze.sql -> sources/definitions/bronze.sql\n    added:    sources/definitions/expectations.sql -> sources/definitions/expectations.sql\n    added:    sources/definitions/reporting.sql -> sources/definitions/reporting.sql\n  Uploading files from local ./dcm_project/output/bundle directory to temporary stage.\n\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__ACTIVE_MEMBERS\nCREATE   DYNAMIC_TABLE        GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__DAILY_REVENUE\nCREATE   TABLE                GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER\nCREATE   TABLE                GLADSTONE_DQ_LAB.CUST_NIELS_DCM.SYSTEM__PAYMENT\nALTER    ROLE                 DQ_LAB_NIELS\n\nDeployed 5 entities (4 created, 1 altered, 0 dropped)."
B3_TEST_OUT = "\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_ACTIVE_LEAVERS)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_DUPLICATE_MEMBERS)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_OTHER_OPERATOR_ROWS)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__DAILY_REVENUE (REVENUE_ALWAYS_COMPUTED)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.SYSTEM__PAYMENT (NO_NEGATIVE_AMOUNTS)\n\n5 passed, 0 failed out of 5 total."
B3_TEST_FAIL_OUT = "\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_ACTIVE_LEAVERS)\n\u2717 FAIL      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_DUPLICATE_MEMBERS)\n  \u2514\u2500 Expected: value = 0, Got: 1 (Metric: DUPLICATE_COUNT)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.MEMBERS__MEMBER (NO_OTHER_OPERATOR_ROWS)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.REPORTING__DAILY_REVENUE (REVENUE_ALWAYS_COMPUTED)\n\u2713 PASS      GLADSTONE_DQ_LAB.CUST_NIELS_DCM.SYSTEM__PAYMENT (NO_NEGATIVE_AMOUNTS)\n\u256d\u2500 Error \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256e\n\u2502 4 passed, 1 failed out of 5 total.                                           \u2502\n\u2570\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u256f"
B3_TEST_FAIL_EXIT = 1
