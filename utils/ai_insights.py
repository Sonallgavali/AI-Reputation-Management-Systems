import os
import requests

from dotenv import load_dotenv

# Load env variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

def generate_ai_insights(reviews):

    reviews_text = "\n".join(reviews)

    prompt = f"""
    You are an AI reputation management assistant.

    Analyze these customer reviews.

    Provide:

    1. Overall customer sentiment
    2. Top compliments
    3. Common complaints
    4. Operational/service issues
    5. Actionable recommendations
    6. Reputation risk summary

    Reviews:
    {reviews_text}

    Keep response concise,
    professional, and business-focused.
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },

        json={
            "model": "openai/gpt-3.5-turbo",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]