import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('Bank Customer Churn Prediction Dataset.csv')
X = df[['credit_score', 'age', 'tenure', 'balance', 'products_number',
        'credit_card', 'active_member', 'estimated_salary']]
y = df['churn']

nav = st.sidebar.radio("Navigations", ['Home', 'Predictions'])

if nav == "Home":
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
st.table(df.head(5))
    
if nav == 'Predictions':
    with st.sidebar.header('set split parameter'):
        
        split_size = st.sidebar.slider("% of training set", value = 70)
        
        st.slider('set age', value= 16)
        st.slider('tenure', max_value = 10, value= 1)
        st.selectbox('Gender', ['Male', 'Female'], index= 1)
        st.number_input('estimated_salary', min_value = 11.580000, max_value = 199992.480000)  

        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=split_size, random_state=101)

        rfc = RandomForestClassifier(
        n_estimators=300, max_features=2, min_samples_split=10)
        rfc.fit(X_train, y_train)

        ada = AdaBoostClassifier(base_estimator=rfc, n_estimators=100, random_state=42)
        ada.fit(X_train, y_train)
        y_pred = ada.predict(X_test)
    
