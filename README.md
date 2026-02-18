Clinical Trials ETL Pipeline + Power BI Dashboard

End-to-end data engineering pipeline that extracts clinical trial data from the ClinicalTrials.gov REST API, transforms nested JSON into a clean relational format, loads it into PostgreSQL (Docker), and visualizes insights in Power BI.

🚀 Architecture

ClinicalTrials.gov API

→ Python (Extract + Transform)

→ PostgreSQL (Docker container)

→ SQL Views

→ Power BI Dashboard


🛠 Tech Stack

Python (requests, pandas, SQLAlchemy)

PostgreSQL 15 (Docker)

Power BI Desktop

Git & GitHub

📊 Features

API data extraction with parameterized queries

Nested JSON flattening into structured schema

Data type cleaning and transformation

Containerized PostgreSQL database

Analytical SQL views for reporting

Interactive Power BI dashboard with slicers and KPI cards

📈 Dashboard Visuals

Trials by Status (Donut Chart)

Trials by Phase (Bar Chart)

Total Trials KPI

Interactive Status Filter

💡 Future Improvements

Implement pagination for 1000+ records

Add incremental loading logic

Schedule pipeline execution

Deploy to cloud environment (AWS/GCP/Azure)
