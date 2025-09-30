# Healthcare Financial Analytics for Risk Management

This project demonstrates how to use PySpark, SQL, and Streamlit to build an ETL pipeline and financial risk analytics system for healthcare data.

## Features
- Spark ETL pipeline integrating **pharmacy, lab, and eligibility** datasets
- SQL-based risk scoring (HCC-like logic) for chronic condition tagging
- **Interactive Streamlit dashboard** for PMPM cost transparency

## Run Instructions
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run ETL pipeline
python src/etl_pipeline.py

# 3. Launch dashboard
streamlit run src/dashboard_app.py
