import pandas as pd
import random

# Load raw dataset
df = pd.read_csv("data/raw_reviews.csv")

# Rename columns
df = df.rename(columns={
    "Restaurant": "business_name",
    "Reviewer": "reviewer_name",
    "Review": "review_text",
    "Rating": "rating",
    "Time": "review_date"
})

# Keep only required columns
df = df[
    [
        "business_name",
        "reviewer_name",
        "review_text",
        "rating",
        "review_date"
    ]
]

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Convert rating to numeric
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Remove invalid ratings
df = df[df["rating"].between(1, 5)]

# Add source column
sources = ["Google", "Yelp", "TripAdvisor"]

df["source"] = [
    random.choice(sources)
    for _ in range(len(df))
]

# Keep top 10 businesses only for demo
top_businesses = (
    df["business_name"]
    .value_counts()
    .head(10)
    .index
)

demo_df = df[
    df["business_name"].isin(top_businesses)
]

# Limit rows for faster app performance
demo_df = demo_df.head(2000)

# Save cleaned datasets
df.to_csv(
    "data/sample_reviews.csv",
    index=False
)

demo_df.to_csv(
    "data/demo_reviews.csv",
    index=False
)

print("Datasets created successfully!")
print(f"Full dataset rows: {len(df)}")
print(f"Demo dataset rows: {len(demo_df)}")

print("\nTop Businesses:")
print(demo_df["business_name"].value_counts())