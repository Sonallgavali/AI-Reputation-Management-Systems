import streamlit as st
import pandas as pd
import plotly.express as px
from utils.recommendations import extract_keywords
from utils.sentiment import get_sentiment

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Dashboard",
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
# SENTIMENT
# -----------------------------
df["sentiment"] = df["review_text"].apply(
    get_sentiment
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Reputation Analytics Dashboard")

st.markdown(
    "Monitor customer reviews, ratings, and sentiment insights."
)

# -----------------------------
# BUSINESS FILTER
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
# KPIs
# -----------------------------
total_reviews = len(filtered_df)

average_rating = round(
    filtered_df["rating"].mean(),
    2
)

positive_reviews = len(
    filtered_df[
        filtered_df["sentiment"] == "Positive"
    ]
)

negative_reviews = len(
    filtered_df[
        filtered_df["sentiment"] == "Negative"
    ]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Reviews",
    total_reviews
)

col2.metric(
    "Average Rating",
    average_rating
)

col3.metric(
    "Positive Reviews",
    positive_reviews
)

col4.metric(
    "Negative Reviews",
    negative_reviews
)

st.markdown("---")

# -----------------------------
# SENTIMENT CHART
# -----------------------------
sentiment_counts = (
    filtered_df["sentiment"]
    .value_counts()
    .reset_index()
)

sentiment_counts.columns = [
    "Sentiment",
    "Count"
]

fig_sentiment = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Count",
    title="Sentiment Distribution"
)

fig_sentiment.update_layout(
    template="plotly_dark",
    paper_bgcolor="#161B22",
    plot_bgcolor="#161B22"
)

st.plotly_chart(
    fig_sentiment,
    width="stretch"
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# RATINGS CHART
# -----------------------------
ratings_chart = px.histogram(
    filtered_df,
    x="rating",
    title="Ratings Distribution"
)

ratings_chart.update_layout(
    template="plotly_dark",
    paper_bgcolor="#161B22",
    plot_bgcolor="#161B22"
)

st.plotly_chart(
    ratings_chart,
    width="stretch"
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# REVIEW TABLE
# -----------------------------
st.subheader("📝 Customer Reviews")

st.dataframe(
    filtered_df[[
        "review_text",
        "rating",
        "sentiment"
    ]],
    use_container_width=True
)

st.markdown("---")
# -----------------------------
# PRIORITY REVIEWS
# -----------------------------
st.subheader("🚨 Priority Reviews")

priority_reviews = filtered_df[
    filtered_df["rating"] <= 2
][[
    "review_text",
    "rating"
]].head(5)

if len(priority_reviews) > 0:

    st.dataframe(
        priority_reviews,
        use_container_width=True
    )

else:
    st.info("No critical reviews found.")

st.markdown("---")

# -----------------------------
# SOURCE-WISE ANALYTICS
# -----------------------------
st.subheader("🌐 Source-wise Review Distribution")

source_counts = (
    filtered_df["source"]
    .value_counts()
    .reset_index()
)

source_counts.columns = [
    "Source",
    "Reviews"
]

st.dataframe(
    source_counts,
    use_container_width=True
)

# -----------------------------
# SOURCE CHART
# -----------------------------
source_chart = px.bar(
    source_counts,
    x="Source",
    y="Reviews",
    title="Reviews by Platform"
)

source_chart.update_layout(
    template="plotly_dark",
    paper_bgcolor="#161B22",
    plot_bgcolor="#161B22"
)

st.plotly_chart(
    source_chart,
    use_container_width=True
)
# -----------------------------
# REPUTATION RISK SCORE
# -----------------------------
negative_percentage = (
    negative_reviews / total_reviews
) * 100

risk_score = round(negative_percentage, 1)

if risk_score < 20:
    risk_level = "🟢 Low Risk"

elif risk_score < 50:
    risk_level = "🟠 Moderate Risk"

else:
    risk_level = "🔴 High Risk"

st.subheader("🚨 Reputation Risk Score")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Risk Score",
        f"{risk_score}%"
    )

with col2:
    st.metric(
        "Risk Level",
        risk_level
    )

st.markdown("---")
