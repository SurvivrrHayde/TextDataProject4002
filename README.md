<!-- README for TextDataProject4002 -->

# TextDataProject4002

<!-- Project Overview -->
## 📌 Project Overview

**TextDataProject4002** is a **sentiment analysis and box office prediction** project.  
It leverages **pre-released critic reviews** to predict a movie’s **opening weekend revenue**.  
The project involves **data collection, sentiment analysis, machine learning modeling, and evaluation**.  

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



<!-- Section 3: Instructions for Reproducing Results -->
## Section 3: Instructions for Reproducing Results
Follow these steps to reproduce our results:

1. **Set Up the Environment**  
   Ensure you have Python 3.x installed and run:
   ```bash
   pip install -r requirements.txt
   ```
2. **Collect & Prepare Data**
   - Scrape IMDb reviews: Run the web_scraper.py script.
   - Merge datasets: Use the datasetMerger.py script.
   - Aggregate sentiment scores: Execute aggregation_function.py.
   - Clean the dataset: Run prepare_dataset.py.
4. **Train Models & Evaluate Performance**
   - Execute the model_training.py script to train models and evaluate their performance.
5. **View Results**
   - Check the OUTPUT folder for performance tracking results and saved models.



