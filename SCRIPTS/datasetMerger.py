import pandas as pd

# Load both CSV files
df_reviews = pd.read_csv("sentiment_results.csv")  # First CSV file
df_movies = pd.read_csv("Data - Sheet1.csv")  # Second CSV file

# Merge the two datasets on 'movie_id'
df_combined = df_reviews.merge(df_movies, on="movie_id", how="left")

# Optionally, save the merged dataset to a CSV
df_combined.to_csv("review_dataset.csv", index=False)
print("Merged dataset saved as 'combined_movie_reviews.csv'")
