import streamlit as st
import pandas as pd

from utils.ai_reply import generate_review_reply

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Reply Assistant",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("⭐ AI Reputation")

st.sidebar.markdown(
    """
    AI-powered reputation monitoring
    for restaurants & hotels.
    """
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/demo_reviews.csv")

df = load_data()

# -----------------------------
# TITLE
# -----------------------------
st.title("💬 AI Review Reply Assistant")

st.markdown(
    "Generate AI-powered professional responses to customer reviews."
)

# -----------------------------
# SELECT BUSINESS
# -----------------------------
businesses = sorted(df["business_name"].unique())

selected_business = st.selectbox(
    "Select Business",
    businesses
)

filtered_df = df[
    df["business_name"] == selected_business
]

# -----------------------------
# SELECT REVIEW
# -----------------------------
selected_review = st.selectbox(
    "Select Customer Review",
    filtered_df["review_text"].head(20)
)

st.subheader("📝 Customer Review")

st.info(selected_review)

# -----------------------------
# GENERATE REPLY
# -----------------------------
if st.button("Generate AI Reply"):

    with st.spinner("Generating AI reply..."):

        ai_reply = generate_review_reply(
            selected_review
        )

        st.subheader("🤖 AI-Generated Reply")

        st.success(ai_reply)