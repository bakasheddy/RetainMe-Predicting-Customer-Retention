import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


st.write(
    """
    # RetainMe: Predicting-Customer-Retention
    """)

st.image('./images/churn.JPG')

st.write("""### About dataset

This dataset is for ABC Multistate bank, the dataset has 10000 entries with no duplicates or missing values, it has 10000 rows and 12 columns with following column names:

- customer_id, unused variable.
- credit_score, used as input.
- country, used as input.
- gender, used as input.
- age, used as input.
- tenure, used as input.
- balance, used as input.
- products_number, used as input.
- credit_card, used as input.
- active_member, used as input.
- estimated_salary, used as input.
- churn, used as the target. 1 if the client has left the bank during some period or 0 if he/she has not.

Every bank wants to hold there customers for sustaining their business so the ABC Multinational bank.

Below is the customer data of account holders at ABC Multinational Bank and the aim of the data will be predicting the Customer Churn.

    """
         )

df = pd.read_csv('Bank Customer Churn Prediction Dataset.csv')
st.table(df.head(5))
