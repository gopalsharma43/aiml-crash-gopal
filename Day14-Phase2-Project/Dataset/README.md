# Order Delay Intelligence - E-Commerce Delivery Delay Prediction

## Project Overview

This project focuses on predicting delivery delays in an e-commerce environment using machine learning techniques.

The objective is to identify orders that are likely to be delayed before delivery, enabling businesses to take proactive actions, improve customer satisfaction, and optimize logistics operations.

The project was completed as part of the AIML Internship Program and covers the complete machine learning workflow from data auditing to model evaluation and business recommendations.

---

## Dataset

The project uses the Brazilian E-Commerce Public Dataset (Olist Dataset).

Datasets used:

- olist_orders_dataset.csv
- olist_customers_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_products_dataset.csv

---

## Project Workflow

### 1. Data Audit

Performed an initial inspection of all datasets:

- Dataset dimensions
- Data types
- Missing values
- Duplicate records

### 2. Data Cleaning

- Converted date columns to datetime format
- Handled missing values
- Verified dataset consistency

### 3. Feature Engineering

Created new features including:

- Delivery Time (Days)
- Delayed Order Flag
- Purchase Month

### 4. Exploratory Data Analysis (EDA)

Analyzed:

- Delayed vs Non-Delayed Orders
- Delivery Time Distribution
- Monthly Order Trends
- Customer State Patterns

### 5. Machine Learning Models

Implemented and evaluated:

- Logistic Regression
- Balanced Logistic Regression
- XGBoost Classifier

### 6. Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC

### 7. Cross Validation

Used Stratified K-Fold Cross Validation to evaluate model stability.

### 8. Hyperparameter Tuning

Applied GridSearchCV to improve XGBoost model performance.

### 9. Feature Importance Analysis

Identified the most influential features affecting delivery delay predictions.

---

## Key Findings

- Most orders are delivered on time.
- A smaller percentage of orders experience delays.
- Customer location plays an important role in delivery performance.
- Seasonal purchasing patterns influence order volumes.
- XGBoost achieved the strongest predictive performance among the tested models.

---

## Business Recommendations

- Monitor high-risk orders proactively.
- Improve logistics planning during peak demand periods.
- Focus on regions with higher delay frequencies.
- Notify customers early when delays are predicted.
- Use predictive analytics to support operational decisions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Jupyter Notebook

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Real-world dataset analysis
- Data cleaning and preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Machine learning model development
- Model evaluation and comparison
- Business-oriented data interpretation

---

## Author

**Gopal Sharma**

AIML Internship Participant

GitHub: https://github.com/gopalsharma43