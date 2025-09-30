import streamlit as st
import pandas as pd

# Load sample processed data
data = pd.read_parquet("output/healthcare_data.parquet")

# Sidebar filters
patient_id = st.sidebar.selectbox("Select Patient", data["patient_id"].unique())

# Show details
patient_data = data[data["patient_id"] == patient_id]

st.title("Healthcare Financial Analytics Dashboard")
st.subheader(f"Patient ID: {patient_id}")

st.write("### Pharmacy Costs")
st.bar_chart(patient_data[["drug_cost"]])

st.write("### Lab Results")
st.table(patient_data[["lab_test", "result_flag"]])

st.write("### Eligibility & Risk Score")
st.json({
    "Eligibility_Status": str(patient_data["eligibility_status"].iloc[0]),
    "Mock_Risk_Score": round(patient_data["drug_cost"].sum() / 1000, 2)
})
