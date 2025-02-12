import pandas as pd

def clean_movie_data(file_path, output_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Clean 'Opening_earnings' column
    df['Opening_earnings'] = df['Opening_earnings'].replace('[\$,]', '', regex=True).astype(float)
    
    # Drop rows with missing target values (Opening_earnings)
    df = df.dropna(subset=['Opening_earnings'])
    
    # Fill missing values in 'Rank' with the median
    df['Rank'] = df['Rank'].fillna(df['Rank'].median())
    
    # Encode categorical variables using one-hot encoding
    df = pd.get_dummies(df, columns=['Release_month', 'Distributor'], drop_first=True)
    
    # Drop unnecessary columns
    df = df.drop(columns=['Movie_id', 'Name'])
    
    # Save the cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_file = "DATA/aggregated_movie_reviews.csv"  # Change to your actual file path
    output_file = "DATA/cleaned_movie_data.csv"  # Output file path
    clean_movie_data(input_file, output_file)