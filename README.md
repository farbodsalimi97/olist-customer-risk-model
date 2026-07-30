# Olist Customer Experience Risk Modeling

End-to-end data analysis + machine learning case study on the Olist E-Commerce dataset, focused on predicting high-risk orders (low review scores) and improving customer experience.

## Problem
Identify orders that are likely to receive low ratings (review score <= 2) early enough to take proactive action.

## Key Insight
Exploratory analysis suggests customer dissatisfaction is driven mainly by logistics, not price:
- Delivery delay
- Actual transit time

## Model
- Algorithm: Random Forest Classifier
- Metric: ROC-AUC ≈ 0.75

## Business Recommendation
Implement an **Early Warning System** to flag high-risk orders and enable proactive operational intervention (instead of broad discounting).


## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
