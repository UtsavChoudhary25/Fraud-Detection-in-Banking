import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("🏦 Banking Fraud Detection Dashboard")

st.write("""
This dashboard presents an overview of the credit card fraud detection dataset.
""")

# Load Dataset
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "dataset" / "creditcard.csv"

df = pd.read_csv(DATA_PATH)

# Basic Statistics
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", len(df))
col2.metric("Fraud Cases", int(df["Class"].sum()))
col3.metric("Genuine Cases", int((df["Class"] == 0).sum()))

st.divider()

st.header("Transaction Class Distribution")

fig, ax = plt.subplots(figsize=(6,4))

df["Class"].value_counts().plot(kind="bar", ax=ax)

ax.set_xticklabels(["Genuine", "Fraud"])

st.pyplot(fig)

st.divider()

st.header("Transaction Amount Distribution")

fig2, ax2 = plt.subplots(figsize=(8,4))

ax2.hist(df["Amount"], bins=50)

ax2.set_xlabel("Amount")
ax2.set_ylabel("Frequency")

st.pyplot(fig2)

st.divider()

st.header("Dataset Preview")

st.dataframe(df.head())