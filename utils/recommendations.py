from collections import Counter
import re

# -----------------------------
# CLEAN TEXT
# -----------------------------
def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    return text

# -----------------------------
# EXTRACT KEYWORDS
# -----------------------------
def extract_keywords(reviews):

    stopwords = {
        "the", "and", "was", "were",
        "with", "this", "that",
        "have", "had", "food",
        "place", "very", "good",
        "nice", "great", "best"
    }

    words = []

    for review in reviews:

        cleaned = clean_text(
            str(review)
        )

        split_words = cleaned.split()

        filtered_words = [
            word for word in split_words
            if word not in stopwords
            and len(word) > 3
        ]

        words.extend(filtered_words)

    keyword_counts = Counter(words)

    return keyword_counts.most_common(10)

# -----------------------------
# GENERATE RECOMMENDATIONS
# -----------------------------
def generate_recommendations(
    negative_reviews
):

    recommendations = []

    combined_text = " ".join(
        negative_reviews
    ).lower()

    if "delay" in combined_text:
        recommendations.append(
            "Improve order delivery speed."
        )

    if "service" in combined_text:
        recommendations.append(
            "Provide additional staff training."
        )

    if "price" in combined_text:
        recommendations.append(
            "Review pricing strategy and value offerings."
        )

    if "crowded" in combined_text:
        recommendations.append(
            "Optimize seating and customer flow."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Maintain current service quality and customer satisfaction."
        )

    return recommendations