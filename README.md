# Fraud Detection in Banking Using Machine Learning

## Overview

This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The objective is to build a classification model capable of distinguishing fraudulent transactions from genuine ones while handling a highly imbalanced dataset.

The project covers the complete data science workflow, including data preprocessing, exploratory data analysis, visualization, model training, evaluation, and deployment through a Streamlit dashboard.

---

## Dataset

The project uses the **Credit Card Fraud Detection** dataset containing anonymized transaction records.

**Dataset Summary**

| Attribute | Value |
|-----------|-------:|
| Total Transactions | 284,807 |
| Genuine Transactions | 284,315 |
| Fraudulent Transactions | 492 |
| Features | 30 |

The dataset is highly imbalanced, making fraud detection a challenging binary classification problem.
## Dataset

The dataset used in this project is too large to be stored on GitHub.

You can download it from Kaggle:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

After downloading, place the `creditcard.csv` file inside the `dataset` folder.
---

## Project Workflow

The following steps were carried out during the project:

- Data loading and preprocessing
- Missing value analysis
- Exploratory Data Analysis (EDA)
- Transaction visualization
- Correlation analysis
- Machine learning model development
- Model evaluation
- Dashboard development

---

## Machine Learning Models

Three supervised learning algorithms were implemented and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Performance Summary

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|---------:|----------:|--------:|----------:|
| Logistic Regression | 99.93% | 0.87 | 0.72 | 0.79 |
| Decision Tree | 99.91% | 0.75 | 0.74 | 0.75 |
| Random Forest | **99.96%** | **0.94** | **0.82** | **0.87** |

Based on the evaluation metrics, the Random Forest model produced the best overall performance and was selected as the final model.

---

## Project Structure

```
Fraud-Detection-in-Banking/
│
├── dashboard/
│   └── app.py
│
├── dataset/
│   └── creditcard.csv
│
├── images/
│
├── models/
│   └── random_forest_model.pkl
│
├── notebooks/
│   └── Fraud_Detection.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dashboard

A Streamlit dashboard was developed to provide an interactive overview of the dataset and project results. The dashboard includes:

- Dataset summary
- Fraud vs Genuine transaction statistics
- Transaction distribution visualizations
- Dataset preview

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## Future Improvements

Potential enhancements for this project include:

- Hyperparameter optimization
- Implementation of XGBoost and LightGBM
- Handling class imbalance using SMOTE
- Real-time fraud prediction
- Interactive analytical dashboard

---
## Running the Project

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

## Author

**Utsav Choudhary**

Data Science Internship Project