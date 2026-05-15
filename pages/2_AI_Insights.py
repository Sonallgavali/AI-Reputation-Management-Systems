import streamlit as st
import pandas as pd

from utils.ai_insights import generate_ai_insights
from utils.recommendations import (
    extract_keywords,
    generate_recommendations
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Insights",
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
st.title("🤖 AI Reputation Insights")

st.markdown(
    "Generate AI-powered business insights and recommendations."
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
# GENERATE INSIGHTS
# -----------------------------
if st.button("Generate AI Insights"):

    with st.spinner("Analyzing reviews..."):

        reviews = (
            filtered_df["review_text"]
            .astype(str)
            .tolist()
        )[:30]

        insights = generate_ai_insights(reviews)

        summary_tab, keyword_tab, recommendation_tab = st.tabs([
            "AI Summary",
            "Keywords",
            "Recommendations"
        ])

        with summary_tab:

            st.subheader("📌 AI Summary")
            st.markdown(insights)

        with keyword_tab:

            st.subheader("📊 Common Keywords")

            keywords = extract_keywords(
                filtered_df["review_text"]
            )

            keyword_df = pd.DataFrame(
                keywords,
                columns=["Keyword", "Frequency"]
            )

            st.dataframe(
                keyword_df,
                use_container_width=True
            )

        with recommendation_tab:

            st.subheader("🚀 Recommendations")

            negative_reviews = filtered_df[
                filtered_df["rating"] <= 2
            ]["review_text"].tolist()

            recommendations = generate_recommendations(
                negative_reviews
            )

            for recommendation in recommendations:
                st.success(recommendation)