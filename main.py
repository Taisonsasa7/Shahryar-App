import streamlit as st
import pandas as pd

def get_all_balances():
    data = {
        "Host": ["Ahmed", "Sara", "Mohamed", "Laila"],
        "Total Sales": [3000, 1500, 5000, 2000],
        "Admin (60%)": [1800, 900, 3000, 1200],
        "Host (35%)": [1050, 525, 1750, 700],
        "Agent (5%)": [150, 75, 250, 100]
    }
    return pd.DataFrame(data)

st.title("لوحة تحكم أرصدة شهريار")

df = get_all_balances()
st.subheader("التقرير المالي الشامل (60/35/5)")

st.dataframe(df.style.format({
    "Total Sales": "${:,.2f}",
    "Admin (60%)": "${:,.2f}",
    "Host (35%)": "${:,.2f}",
    "Agent (5%)": "${:,.2f}"
}))

