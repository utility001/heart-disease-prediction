import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Title of the app
st.title('Heart Disease Prediction app Demo')

# Load the model
heart_disease_model = pickle.load(open('final_log_reg_model.pkl', 'rb'))

# Function to get user input
def user_input_features():
    age = st.slider("Patient's Age", 29, 77, 30, 1)
    sex = st.selectbox("Patient's sex", ('Female', 'Male'))
    cp = st.selectbox(
        "Chest Pain Type",
        ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
    trestbps = st.slider(
        "Patient's Resting Blood Pressure (mm Hg) on admission into the hospital",
        94.0, 200.0, 100.0, 0.01)
    chol = st.slider(
        "Patient's Serum Cholestoral level in (mg/dl)", 
        126, 409, 200, 1)
    fbs = st.slider(
        "Patient's Fasting Blood Sugar in mg/dl",
        100, 200, 150, 1)
    restecg = st.selectbox(
        "Patient's Resting Electrocardiographic Results",
        ('Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'))
    slope = st.selectbox(
        'Slope of the Peak Exercise ST Segment',
        ('Upsloping', 'Flat', 'Downsloping'))
    thalach = st.slider(
        'Maximum Heart Rate Achieved by patient',
        80, 300, 90, 1)
    exang = st.selectbox(
        'Does the patient have Exercise Induced Angina',
        ('No', 'Yes'))
    oldpeak = st.slider(
        'ST Depression Induced by Exercise Relative to Rest', 
        0.0, 6.0, 2.0, 0.1)
    ca = st.slider(
        'Number of Major Vessels Colored by Flourosopy',
        0, 5, 3, 1)
    thal = st.selectbox(
        'Thalassemia',
        ('Normal', 'Fixed Defect', 'Reversible Defect'))
    
    data = {
        'age': age,
        'sex': 1 if sex == 'Male' else 0,
        'cp': ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(cp),
        'trestbps': trestbps,
        'chol': chol,
        'fbs': 1 if fbs > 120 else 0,
        'restecg': ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'].index(restecg),
        'thalach': thalach,
        'exang': 1 if exang == 'Yes' else 0,
        'oldpeak': oldpeak,
        'slope': ['Upsloping', 'Flat', 'Downsloping'].index(slope),
        'ca': ca,
        'thal': ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal)
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

option = st.sidebar.radio('Select an Option', ('About Heart Disease', 'Live Demo'))

if option == 'About Heart Disease':
    st.header("What is heart disease")
    st.markdown("""
Heart disease refers to various conditions that affect the heart's ability to function properly.  

The most common type is coronary artery disease (CAD), which can lead to heart attacks. Other types include heart failure, arrhythmias, and heart valve problems.    
    
This app predicts the likelihood of having heart disease based on input features such as age, sex, blood pressure, cholesterol levels, and other health indicators.  
    
Once heart disease is detected, further test will be carried out by healthcare professionals to determine the specific type of heart disease and the appropriate treatment.

Click on 'Live Demo' on the side bar to use the live demo of the app.
    """)

elif option == 'Live Demo':
    st.header('Input user Features')

    df = user_input_features()

    # # Main panel
    # st.subheader('User Input features')
    # st.write(df)

    prediction = heart_disease_model.predict(df)

    if st.button("Make Prediction"):
        if prediction[0] == 1:
            st.success("⚠⚠⚠⚠Warning⚠⚠⚠⚠: The model predicts that **the patient has heart disease**.")
        else:
            st.success("The model predicts that **the patient DOES NOT have heart disease.**")