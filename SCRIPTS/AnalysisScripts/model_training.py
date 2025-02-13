import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor, plot_importance
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load cleaned data
df = pd.read_csv("DATA/cleaned_movie_data.csv")

# Split features and target
X = df.drop(columns=["Opening_earnings"])
y = df["Opening_earnings"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
joblib.dump(scaler, "OUTPUT/scaler.pkl")  # Save scaler

# Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42)
}

# Train and evaluate models without log transformation
results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    joblib.dump(model, f"OUTPUT/{name.replace(' ', '_')}_No_Log.pkl")  # Save model
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[f"{name} (No Log)"] = {"MAE": mae, "MSE": mse, "R2 Score": r2}

# Apply log transformation
df["Opening_earnings"] = np.log1p(df["Opening_earnings"])
y = df["Opening_earnings"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and evaluate models with log transformation
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    joblib.dump(model, f"OUTPUT/{name.replace(' ', '_')}_Log_Transformed.pkl")  # Save model
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(np.expm1(y_test), np.expm1(y_pred))
    mse = mean_squared_error(np.expm1(y_test), np.expm1(y_pred))
    r2 = r2_score(np.expm1(y_test), np.expm1(y_pred))
    results[f"{name} (Log Transformed)"] = {"MAE": mae, "MSE": mse, "R2 Score": r2}

# Perform Grid Search for XGBoost Hyperparameter Tuning
xgb = XGBRegressor(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}
grid_search = GridSearchCV(xgb, param_grid, cv=3, scoring='r2', n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)

# Best Parameters
best_xgb = grid_search.best_estimator_
joblib.dump(best_xgb, "OUTPUT/Best_XGBoost.pkl")  # Save best model
results["Best XGBoost"] = {
    "MAE": mean_absolute_error(np.expm1(y_test), np.expm1(best_xgb.predict(X_test_scaled))),
    "MSE": mean_squared_error(np.expm1(y_test), np.expm1(best_xgb.predict(X_test_scaled))),
    "R2 Score": r2_score(np.expm1(y_test), np.expm1(best_xgb.predict(X_test_scaled)))
}

# Save results to CSV
results_df = pd.DataFrame(results).T
results_df.to_csv("OUTPUT/model_performance_tracking.csv", index=True)
print("Saved model results to model_performance_tracking.csv")

# Load and use saved models (Example usage)
loaded_model = joblib.load("OUTPUT/Best_XGBoost.pkl")
predictions = np.expm1(loaded_model.predict(X_test_scaled))
print("Sample Predictions:", predictions[:5])