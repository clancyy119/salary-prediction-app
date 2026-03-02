import streamlit as st
import pickle
import numpy as np
import os

def load_model():
    model = None
    try:
        with open(os.path.join(os.path.dirname(__file__), 'saved_steps.pkl'), 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        st.error('Model file not found!')
    return model

def show_predict_page():
    st.title('Salary Prediction')
    country = st.selectbox('Select your country:', ['USA', 'Canada', 'UK'])
    education = st.selectbox('Select your education level:', ['High School', 'Bachelors', 'Masters'])
    experience = st.slider('Years of Experience:', 0, 20, 1)
    if st.button('Predict Salary'):
        model = load_model()
        if model:
            # Assume model has a predict method
            salary_prediction = model.predict([[country, education, experience]])
            st.success(f'Predicted Salary: ${salary_prediction[0]}')
