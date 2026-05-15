import os
import requests

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

def generate_review_reply(review):

    prompt = f"""
    You are a restaurant reputation manager.

    Generate a professional and polite
    response to this customer review.

    Review:
    {review}

    Keep the reply:
    - professional
    - concise
    - empathetic
    - customer-friendly
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