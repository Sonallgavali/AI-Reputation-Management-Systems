
import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Reputation Manager",
    page_icon="⭐",
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
# HERO SECTION
# -----------------------------
st.title("⭐ AI Reputation Management System")

st.markdown(
    """
    ### Monitor Customer Sentiment with AI

    Analyze online reviews, identify operational issues,
    generate AI-powered business insights,
    and automate customer engagement.
    """
)

# -----------------------------
# FEATURE CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        ### 📊 Analytics Dashboard

        Track reviews, ratings,
        sentiment trends,
        and source-wise analytics.
        
        
        """
    )

with col2:
    st.info(
        """
        ### 🤖 AI Insights

        Generate business summaries,
        complaints analysis,
        and recommendations.
        """
    )

with col3:
    st.info(
        """
        ### 💬 AI Reply Assistant

        Generate professional
        customer review responses
        instantly.
        
        
        """
    )

st.markdown("---")

st.success(
    "Use the sidebar to navigate through modules."
)
