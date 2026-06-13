# Linear Regression Project Report

## Introduction

This project was completed as part of the AI/ML Internship Program. The objective was to understand the practical implementation of Linear Regression and learn how regression models are evaluated using different performance metrics.

As a beginner in the AI/ML domain, this project helped me gain hands-on experience with data preprocessing, model training, prediction, evaluation, and result interpretation.

---

## Dataset Description

The California Housing Dataset was used for this project.

The dataset contains information related to housing characteristics such as:

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Latitude
* Longitude

The target variable is:

* Median House Value (MedHouseVal)

---

## Work Performed

### Task 1

A baseline Linear Regression model was trained using all available features. Predictions were generated and evaluated using standard regression metrics.

### Task 2

Two Linear Regression models were compared:

* One-feature model
* Multi-feature model

The comparison showed that the multi-feature model performed better because it had access to more information.

### Task 3

The same model was tested using different train-test splits:

* 80/20
* 70/30
* 60/40

The objective was to study how dataset splitting affects model performance and stability.

### Task 4

Evaluation metrics were calculated manually and compared with sklearn outputs. An additional metric, Median Absolute Error, was also explored.

An artificial error experiment was conducted to understand how large prediction errors affect MSE, RMSE, and MAE.

---

## Key Findings

* Linear Regression can capture important relationships in housing data.
* Multiple features generally improve prediction accuracy.
* Different train-test splits can slightly affect model performance.
* MSE and RMSE are highly sensitive to large prediction errors.
* MAE is less affected by extreme outliers.

---

## Challenges Faced

During this project, I faced challenges in:

* Understanding regression evaluation metrics
* Selecting appropriate input features
* Comparing multiple models fairly
* Interpreting the meaning of different error values

These challenges helped me improve my understanding of machine learning fundamentals.

---

## Conclusion

This project provided practical exposure to Linear Regression and model evaluation techniques. It helped me understand the complete workflow from dataset preparation to model assessment.

As one of my early machine learning projects, it strengthened my confidence in working with real datasets and applying theoretical concepts in practice.
