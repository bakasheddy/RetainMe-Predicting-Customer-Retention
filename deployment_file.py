import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import pickle

df = pd.read_csv('Bank Customer Churn Prediction Dataset.csv')

nav = st.sidebar.radio("Navigations", ['Home', 'Predictions'])

if nav == "Home":
    st.write(
    """
    # RetainMe: Predicting-Customer-Retention
    """)

    st.image('churn.JPG')

    st.write("""### About dataset

Every bank wants to hold there customers for sustaining their business so the ABC Multinational bank.
Bank ABC (incorporated as Arab Banking Corporation B.S.C) is an international bank headquartered in Manama, Kingdom of Bahrain. Our network spreads across five continents, covering countries in the Middle East, North Africa, Europe, the Americas and Asia. 

Bank ABC, founded in 1980, is listed on the Bahrain Bourse and our major shareholders are the Central Bank of Libya and Kuwait Investment Authority. 

Bank ABC is a leading provider of Trade Finance, Treasury, Project & Structured Finance, Syndications, Corporate & Institutional Banking as well as Islamic Banking services. We are also expanding our retail banking network in the MENA region.

Bank ABC is licensed as a conventional wholesale bank by the Central Bank of Bahrain.
The dataset used for this model training is for ABC Multistate bank, the dataset has 10000 entries with no duplicates or missing values, it has 10000 rows and 12 columns with following column names:

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

    """
         )
    st.dataframe(df)
    st.write("""
        by Shedrack David
        connect with me on [linkedin](https://www.linkedin.com/in/shedrack-david-1a116b235/)
        
        click [here](https://github.com/bakasheddy/RetainMe-Predicting-Customer-Retention.git) to view project on github, and check out my [Portfolio](akasheddy.github.io/Portfolio/)
        """)
    
elif nav == 'Predictions':
    st.image('./images/churn.JPG')
    st.sidebar.subheader('set parameters for predictions')
    def user_input_features():
        
        credit_score = st.sidebar.number_input('credit_score', min_value = df['credit_score'].min(), max_value = df['credit_score'].max())
        gender = st.sidebar.selectbox('Gender', ['male', 'female'], index= 1)
        gender = 1 if gender.lower() == 'male' else 0
        
        age = st.sidebar.slider('set age', value= 16)
        tenure = st.sidebar.slider('tenure', max_value = 10, value= 1)
        balance = st.sidebar.number_input('balance', max_value = df['balance'].max())
        products_number = st.sidebar.number_input('products_number', min_value = df['products_number'].min(), max_value = df['products_number'].max())
        
        credit_card = st.sidebar.selectbox('has credit card?', ['yes', 'no'], index= 1)
        credit_card = 1 if credit_card.lower() == 'yes' else 0 #encoding
        
        active_member = st.sidebar.selectbox('Active member?', ['yes', 'no'], index= 1) 
        active_member = 1 if active_member.lower() == 'yes' else 0 #encoding
        
        estimated_salary = st.sidebar.number_input('estimated_salary', min_value = df['estimated_salary'].min(), max_value = df['estimated_salary'].max())
        
        data = {
            'credit_score': credit_score,            
            'gender': gender,
            'age': age,
            'tenure': tenure,
            'balance': balance,
            'products_number': products_number,
            'credit_card': credit_card,
            'active_member': active_member,
            'estimated_salary': estimated_salary
        }
        feautres = pd.DataFrame(data, index=[0])
        return feautres
    dff = user_input_features()
    st.header('Specified Parameters')
    st.write(dff)
    st.write('---')
    file_name = './RetainMe_Model.pkl'
    loaded_model = pickle.load(open(file_name, 'rb'))
    predictions = loaded_model.predict(dff)
    
    st.write('Churn probability')
    prob = loaded_model.predict_proba(dff)
    st.write(prob)
    
    st.write('Will this person churn?')
    st.write(predictions)
    st.write('---')
    
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(loaded_model.feature_importances_, index= dff.columns)
    feat_importances.nlargest(10).plot(kind='barh')
    plt.title('Most important features for prediction')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.style.use('ggplot')
    plt.grid(visible=False)
    st.pyplot()

    
       
