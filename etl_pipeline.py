import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://clinicaltrials.gov/api/v2/studies"

params = {
    "query.term": "cancer",
    "pageSize": 100
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    studies = data.get("studies", [])

    cleaned_data = []

    for study in studies:
        protocol = study.get("protocolSection", {})

        identification = protocol.get("identificationModule", {})
        status = protocol.get("statusModule", {})
        design = protocol.get("designModule", {})
        sponsor_module = protocol.get("sponsorCollaboratorsModule", {})

        # Phase can sometimes be a list
        phase = design.get("phases")
        if isinstance(phase, list):
            phase = ", ".join(phase)

        record = {
            "nct_id": identification.get("nctId"),
            "title": identification.get("briefTitle"),
            "overall_status": status.get("overallStatus"),
            "phase": phase,
            "start_date": status.get("startDateStruct", {}).get("date"),
            "enrollment": design.get("enrollmentInfo", {}).get("count"),
            "sponsor_name": sponsor_module.get("leadSponsor", {}).get("name")
        }

        cleaned_data.append(record)

    df = pd.DataFrame(cleaned_data)

    # Clean types
    df["enrollment"] = pd.to_numeric(df["enrollment"], errors="coerce")
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")

    df.to_csv("clinical_trials.csv", index=False)
    print("\nCSV file saved successfully!")

    # -----------------------------
# LOAD INTO POSTGRESQL
# -----------------------------

try:
    # Create database connection
    engine = create_engine(
        "postgresql+psycopg2://admin:admin123@localhost:5432/clinical_trials_db"
    )

    # Load DataFrame into database
    df.to_sql(
        "clinical_trials",
        engine,
        if_exists="replace",   # For now we replace table each run
        index=False
    )

    print("\nData successfully loaded into PostgreSQL!")

except Exception as e:
    print("Database error:", e)

    print("\nCleaned Data (Improved):\n")
    print(df.head())

    print("\nData Types:\n")
    print(df.dtypes)

else:
    print("Error:", response.status_code)
