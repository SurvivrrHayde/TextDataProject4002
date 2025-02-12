import pandas as pd

# Save the merged dataset
df_combined = pd.read_csv("review_dataset.csv")

# Aggregate sentiment scores by movie_id (taking the mean)
df_aggregated = df_combined.groupby("movie_id").agg({
    "neg": "mean",
    "neu": "mean",
    "pos": "mean",
    "compound": "mean",
    "Rank": "first",         # Keeping the first occurrence
    "Name": "first",
    "Opening": "first",
    "Month": "first",
    "Distributor": "first"
}).reset_index()

# Save the aggregated dataset
df_aggregated.to_csv("aggregated_movie_reviews.csv", index=False)
print("Aggregated dataset saved as 'aggregated_movie_reviews.csv'")
