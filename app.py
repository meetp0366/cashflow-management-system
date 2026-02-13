import streamlit as st

st.set_page_config(page_title="Cash Flow Management System", layout="wide")

st.title("💰 Cash Flow Management System")

st.markdown("### 📊 Financial Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Income", "₹ 0")
col2.metric("Total Expense", "₹ 0")
col3.metric("Net Profit", "₹ 0")

st.markdown("---")

