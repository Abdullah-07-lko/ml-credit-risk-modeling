import streamlit as st
from prediction_helper import predict  

# Set the page configuration and title
st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊")
st.title("Credit Risk Modelling")

# Short explanation
st.markdown("""
This app helps you **estimate the risk of loan default**, generate a **credit score**, and assign a **risk rating**  
based on a customer’s financial and credit behavior.

👉 Enter the details below and click **Calculate Risk** to see the results.
""")

st.divider()

# Creating rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# -------- Row 1 --------
with row1[0]:
    age = st.number_input('Age', min_value=18, max_value=70, step=1, value=18)

with row1[1]:
    income = st.number_input('Annual Income', min_value=100_000, max_value=100_000_000, value=400_000)

with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=100_000, max_value=50_000_000, value=100_000)

# -------- Loan to Income Ratio --------
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")

# -------- Row 2 --------
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=1, max_value=480, step=1, value=1)

with row2[2]:
    avg_dpd_per_delinquency = st.number_input(
        'Average DPD (Delay in Payments)',
        min_value=0, max_value=365, value=0
    )

# -------- Row 3 --------
with row3[0]:
    delinquency_ratio = st.number_input(
        'Missed Payment Ratio (%)',
        min_value=0, max_value=100, step=1, value=0
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        'Credit Usage Ratio (%)',
        min_value=0, max_value=100, step=1, value=0
    )

with row3[2]:
    num_open_accounts = st.number_input(
        'Active Loan Accounts',
        min_value=0, max_value=20, step=1, value=0
    )

# -------- Row 4 --------
with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])

with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

with row4[2]:
    loan_type = st.selectbox('Loan Type', ['secured', 'Unsecured'])

# -------- Button --------
if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Display the results
    st.write(f"Default Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")


st.markdown("### 📊 Prediction Results")
st.caption("Lower default probability and higher credit score mean lower risk.")
