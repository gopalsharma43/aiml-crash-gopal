# Project Report: Order Delay Intelligence

## Introduction

As part of the AIML Internship Program, I worked on a machine learning project focused on predicting delivery delays in an e-commerce environment. The goal was to analyze historical order data and build predictive models that can identify orders that are likely to be delayed.

This project provided hands-on experience with data analysis, feature engineering, machine learning model development, model evaluation, and business-oriented interpretation of results.

---

## Project Objectives

The main objectives of this project were:

* Analyze e-commerce order data.
* Identify factors associated with delivery delays.
* Build machine learning models to predict delayed orders.
* Compare multiple models using evaluation metrics.
* Generate business insights and recommendations.

---

## Dataset Description

The project used multiple datasets from the Olist E-Commerce Dataset, including information about orders, customers, products, payments, and order items.

The datasets were merged and analyzed to understand customer purchasing behavior and delivery performance.

Key datasets used:

* Orders Dataset
* Customers Dataset
* Products Dataset
* Order Items Dataset
* Payments Dataset

---

## Data Audit and Cleaning

The first stage involved auditing the datasets to understand their structure and quality.

Activities performed:

* Checked dataset dimensions.
* Examined data types.
* Identified missing values.
* Checked duplicate records.
* Converted date columns into datetime format.

Several missing values were found in delivery-related columns, which is expected because some orders were not completed or delivered at the time of data collection.

---

## Feature Engineering

To improve the predictive capability of the models, new features were created.

### Delivery Time

A new feature called delivery_time_days was created by calculating the difference between the purchase date and the actual delivery date.

### Delayed Order Flag

A binary target variable called is_delayed was created:

* 1 = Delayed Order
* 0 = On-Time Order

### Purchase Month

The purchase month was extracted from the order timestamp to capture possible seasonal patterns.

---

## Exploratory Data Analysis

Several visualizations and analyses were performed.

### Delayed vs Non-Delayed Orders

The analysis showed that most orders were delivered on time, while a smaller percentage experienced delays.

### Delivery Time Distribution

Most deliveries were completed within a relatively short period. However, a small number of orders experienced significantly longer delivery times.

### Monthly Trends

Order volume varied across different months, indicating seasonal purchasing behavior.

### Customer Location Analysis

Customer state information appeared to have a strong influence on delivery performance, suggesting regional differences in logistics efficiency.

---

## Machine Learning Models

Three machine learning approaches were evaluated.

### Logistic Regression

A baseline Logistic Regression model was developed to establish initial performance.

Results:

* Accuracy ≈ 92%
* ROC AUC ≈ 0.53

Although accuracy was high, the model struggled to identify delayed orders.

### Balanced Logistic Regression

To address class imbalance, Logistic Regression with class balancing was implemented.

Results:

* Improved Recall
* Better identification of delayed orders
* Lower overall accuracy

This demonstrated the impact of class imbalance on model performance.

### XGBoost

XGBoost was used as an advanced ensemble learning algorithm.

Results:

* Accuracy ≈ 92%
* ROC AUC ≈ 0.70

XGBoost achieved the strongest overall performance and was able to capture more complex relationships within the data.

---

## Cross Validation

Stratified K-Fold Cross Validation was performed to evaluate model stability.

Results:

* Mean ROC AUC ≈ 0.709
* Standard Deviation ≈ 0.005

The low standard deviation indicates consistent performance across multiple folds and suggests that the model generalizes reasonably well.

---

## Hyperparameter Tuning

GridSearchCV was used to search for improved model configurations.

The tuning process helped identify better parameter combinations and ensured that the model was evaluated systematically.

---

## Feature Importance Analysis

Feature importance analysis revealed that customer location and purchase timing were among the most influential variables.

Important features included:

* Customer State
* Purchase Month
* Regional customer information

These findings suggest that logistics performance varies across different locations and time periods.

---

## Business Recommendations

Based on the analysis, the following recommendations were identified:

1. Monitor orders with high delay risk.
2. Improve logistics planning during peak demand periods.
3. Focus operational improvements on regions with frequent delays.
4. Use predictive analytics to proactively manage customer expectations.
5. Strengthen coordination with shipping partners.

---

## Learning Outcomes

This project helped me gain practical experience in:

* Data cleaning and preprocessing
* Exploratory Data Analysis
* Feature engineering
* Machine learning model development
* Model evaluation
* Cross validation
* Hyperparameter tuning
* Business-focused interpretation of data

As this was one of my first end-to-end machine learning projects, it significantly improved my understanding of how data science workflows are applied to real-world business problems.

---

## Conclusion

This project successfully demonstrated an end-to-end machine learning workflow for predicting e-commerce delivery delays.

Among all tested models, XGBoost achieved the best performance and provided the strongest predictive capability. The project highlighted the importance of data preparation, feature engineering, model evaluation, and business interpretation in solving practical analytics problems.

Overall, this project was a valuable learning experience and provided hands-on exposure to real-world machine learning techniques and business analytics.
