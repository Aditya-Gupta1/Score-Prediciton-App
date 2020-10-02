import joblib
import streamlit as st
from sklearn.linear_model import LinearRegression
import sklearn

st.write('''
# Scores Prediction App

The app provides an estimate of the exam score that a student can expect based on the number of hours of study.
It uses **Linear Regression** to predict the scores.
''')

st.header('Input hours studied')

hours = st.slider('hours', 1.0, 9.0, 5.0)

model = joblib.load('linear_regression_model.sav')

score = model.predict([[hours]])

st.header("Predicted Score")

st.write(f'{score[0]}')
