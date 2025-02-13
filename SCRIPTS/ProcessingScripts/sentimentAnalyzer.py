import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon if not already available
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Load CSV file
file_path = "DATA/imdb_reviews.csv"  # Update with the actual file path
df = pd.read_csv(file_path)

# Apply VADER sentiment analysis
df[['neg', 'neu', 'pos', 'compound']] = df['review_text'].apply(lambda x: pd.Series(sia.polarity_scores(str(x))))

output_file = "DATA/sentiment_results.csv"
df.to_csv(output_file, index=False)
print(f"Sentiment analysis saved to {output_file}")
