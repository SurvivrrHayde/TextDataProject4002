<!-- README for TextDataProject4002 -->

# TextDataProject4002

<!-- Project Overview -->
## 📌 Project Overview

This is a **sentiment analysis and box office prediction** project. It leverages **pre-released critic reviews** to predict a movie’s **opening weekend revenue**. The project involves **data collection, sentiment analysis, machine learning modeling, and evaluation**.  

### Key Features:
- **Web Scraping** IMDb reviews
- **Sentiment Analysis** using NLP techniques
- **Feature Engineering** for predictive modeling
- **Machine Learning** (XGBoost, Random Forest, etc.)
- **Performance Evaluation** with RMSE, MAE, and R²

<!-- Section 1: Software & Platform -->
## Section 1: Software & Platform

This project was developed using the following software and tools:

- **Programming Language:** Python 3.x  
- **Development Environment:** VS Code  
- **Libraries & Packages:**
  - **pandas** (data manipulation)
  - **matplotlib**, **seaborn** (data visualization)
  - **scikit-learn** (machine learning models)
  - **xgboost** (gradient boosting regression)
  - **joblib** (model saving/loading)
  - **beautifulsoup4**, **requests** (web scraping IMDb reviews)
- **Platform:** Developed and tested on Windows 10 and macOS

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```
<!-- Section 2: Project Folder Structure -->
## Section 2: Software & Platform

├── DATA
│   ├── AnalysisData
│   ├── InputData
│   ├── IntermediateData
│
├── OUTPUT
│   ├── AnalysisGraphics
│   ├── DatasetGraphics
│   ├── Results
│   ├── models
│
├── SCRIPTS
│   ├── AnalysisScripts
│   ├── DataCollectionScripts
│   ├── ProcessingScripts
│
├── LICENSE
├── README.md
├── requirements.txt

<!-- Section 3: Instructions for Reproducing Results -->
## Section 3: Instructions for Reproducing Results
Follow these steps to reproduce our results:

1. **Set Up the Environment**  
   Ensure you have Python 3.x installed as well as the requirements.txt file installed from the SCRIPTS folder. Then run:
   ```bash
   pip install -r requirements.txt
   ```
2. **Collect & Prepare Data**
   - Select Movie Data: Go into Box Office Mojo and hand select which movies you want to train the dataset on.
   - Copy Movie Data into CSV: We used the Domestic Box Office For 2024 movies. Here you should take the Rank, Release, Opening, Open, and Distibutor by copy and paste.
   - Get IMDb ids: You should then search up each movie's name into IMDb to get the movie id and place it into movie_ids.txt.
   - Scrape IMDb reviews: From here use the web_scraper.py script using the movie_ids.txt to webscrape the movie reviews from IMDb.
   - Prepare to combine datasets: Make sure the hand_picked_movie_data obtained from Box Office Mojo is a csv file in the same directory as imdb_reviews.csv.
   - Merge datasets: Use the datasetMerger.py script.
   - Aggregate sentiment scores: Execute aggregation_function.py so that each movie has average sentimennt analysis results and not 25 for each review.
   - Clean the dataset: Run prepare_dataset.py to transform categorical data, fill empty values with median, as well as scale numerical data.
4. **Train Models & Evaluate Performance**
   - Execute the model_training.py script to train models and evaluate their performance.
5. **View Results**
   - Check the OUTPUT folder for performance tracking results and saved models.



