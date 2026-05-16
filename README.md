# ⭐ AI-Powered Reputation Management System

## Project Overview

The AI-Powered Reputation Management System is a Streamlit-based web application designed for restaurants and hotels to monitor, analyze, and improve their online reputation using Artificial Intelligence.

The platform aggregates customer reviews from multiple platforms, performs sentiment analysis, identifies customer pain points, generates AI-powered business insights, and creates professional AI-generated responses to customer reviews.

This project was developed as a practical MVP for an AI Product Engineering internship assignment focused on product thinking, AI integration, dashboard development, and business intelligence.

---

# 🚀 Key Features

## 📊 Review Analytics Dashboard

* Total Reviews Monitoring
* Average Rating Tracking
* Sentiment Distribution Analysis
* Rating Distribution Charts
* Source-wise Review Monitoring
* Reputation Risk Score

## 🤖 AI-Powered Insights

* AI-generated business summaries
* Complaint analysis
* Compliment analysis
* Operational issue detection
* Actionable recommendations
* Reputation risk assessment

## 💬 AI Reply Assistant

* Automatically generate professional customer responses
* Handle positive and negative reviews
* Improve customer engagement
* AI-assisted reputation management

## 🧠 Smart Business Intelligence

* Top Complaints Detection
* Top Compliments Detection
* Priority Review Monitoring
* Keyword Extraction
* Risk Monitoring

---

# 🏗️ Project Architecture

```text
AI-Reputation-Management-System/
│
├── data/
│   └── demo_reviews.csv
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_AI_Insights.py
│   └── 3_AI_Reply_Assistant.py
│
├── screenshots/
│   ├── home.png
│   ├── dashboard.png
│   ├── complaints.png
│   ├── ai_insights.png
│   └── ai_reply.png
│
├── styles/
│   └── style.css
│
├── utils/
│   ├── ai_insights.py
│   ├── recommendations.py
│   ├── ai_reply.py
│   └── sentiment.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🛠️ Tech Stack

| Category           | Technology                     |
| ------------------ | ------------------------------ |
| Frontend/UI        | Streamlit                      |
| Backend            | Python                         |
| AI Integration     | Google Gemini API / OpenAI API |
| Data Processing    | Pandas                         |
| Visualization      | Plotly                         |
| Sentiment Analysis | VaderSentiment                 |
| Dataset            | CSV                            |
| Styling            | Custom CSS                     |

---

# 📂 Dataset Information

The project uses a restaurant reviews dataset containing:

* Business Name
* Reviewer Name
* Review Text
* Rating
* Review Date
* Review Source

### Dataset Size

* Original Dataset: ~10,000 reviews
* Demo Dataset Used: 1,000 reviews

---

# ⚙️ AI Features

## 1. AI-Generated Business Insights

The system uses Gemini AI to:

* Summarize customer feedback
* Detect operational issues
* Identify customer satisfaction trends
* Generate actionable business recommendations

## 2. AI Review Reply Generation

The system generates:

* Professional customer responses
* Polite engagement replies
* Negative review handling responses
* Customer appreciation responses

---

# 📊 Dashboard Analytics

The analytics dashboard includes:

## KPI Monitoring

* Total Reviews
* Average Rating
* Positive Reviews
* Negative Reviews
* Reputation Risk Score

## Analytics Visualizations

* Sentiment Distribution
* Rating Distribution
* Source-wise Analytics

## Business Intelligence Sections

* Top Complaints
* Top Compliments
* Priority Reviews

---

# 🚨 Reputation Risk Score

The application calculates a dynamic Reputation Risk Score based on negative review percentages.

### Risk Levels

| Score  | Risk Level    |
| ------ | ------------- |
| 0–20%  | Low Risk      |
| 21–50% | Moderate Risk |
| 51%+   | High Risk     |

This helps businesses quickly identify operational or customer experience issues.

---

# 🎯 Product Thinking Behind the MVP

The project was intentionally designed as a practical AI product MVP focusing on:

* Fast implementation
* Clean architecture
* AI integration
* Executive dashboard experience
* Business intelligence
* Real-world usability

Instead of overengineering the system, the focus was placed on:

* User experience
* Practical analytics
* AI-powered automation
* Product presentation

---

# 📸 Screenshots

## 🏠 Home Page

![Home](screenshots/home.png)

## 📊 Analytics Dashboard

![Dashboard](screenshots/dashboard.png)

## ⚠️ Complaints & Compliments

![Complaints](screenshots/complaints.png)

## 🤖 AI Insights

![AI Insights](screenshots/ai_insights.png)

## 💬 AI Reply Assistant

![AI Reply](screenshots/ai_reply.png)

---

# 🎥 Demo Video

[Watch Demo Video](https://github.com/user-attachments/assets/3074c910-b4bb-4352-81c2-2e85a6d3f4f8)

```

---

# ⚡ Installation Guide

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

## 2. Navigate to Project Folder

```bash
cd AI-Reputation-Management-System
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Add API Keys

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

You can use either Gemini API or OpenAI API for AI-powered insights and response generation.

## 7. Run Application

```bash
streamlit run app.py
```
```

# 🔒 Environment Variables

The project uses environ!ment variables for secure API key management.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# 🔮 Future Improvements

Potential future enhancements include:

* Real-time review scraping
* Database integration
* User authentication
* Multi-business management
* Review trend forecasting
* Email alerts for negative reviews
* Cloud deployment
* Advanced NLP models
* Role-based dashboards

---

# 💡 Learning Outcomes

Through this project, the following concepts were implemented:

* AI API Integration
* Prompt Engineering
* Dashboard Development
* Sentiment Analysis
* Business Intelligence
* Product-Oriented MVP Development
* Streamlit Multi-page Architecture
* Data Visualization
* Reputation Monitoring Workflows

---

# 👨‍💻 Author

Sonal Gavali

B.E Computer Engineering

AI & Data Analytics Enthusiast

---

# 📄 License

This project is intended for educational and internship evaluation purposes.
