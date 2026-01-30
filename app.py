import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

st.title("Heart Disease Predictor")
tab1 = st.tabs(['Predict'])[0]

with tab1:
    age = st.number_input("Age (years)", min_value=0, max_value=150)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    resting_bp = st. number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300)
    cholesterol = st.number_input("Serum Cholesterol (mm/dl)", min_value=0)
    fasting_bs = st.selectbox("Fasting Blood Sugar", ["<= 120 mg/dl", "> 120 mg/dl"])
    resting_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=202)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=10.0)
    st_slope = st.selectbox("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])


    # Convert categorical inputs to numeric

    sex = 0 if sex == "Male" else 1
    chest_pain = ["Atypical Angina", "Non-Anginal Pain", "Asymptomatic", "Typical Angina"].index(chest_pain)
    fasting_bs = 1 if fasting_bs == "> 120 mg/dl" else 0
    resting_ecg = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index (resting_ecg)
    exercise_angina = 1 if exercise_angina == "Yes" else 0
    st_slope = ["Upsloping", "Flat", "Downsloping"].index (st_slope)

    # Create a DataFrame with user inputs

    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ChestPainType': [chest_pain],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'RestingECG': [resting_ecg],
        'MaxHR': [max_hr],
        'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope]
    })

    algonames = ['Logistic Regression (Accuracy: 85.86%)']
    modelnames = ['LogisticRegression.pkl']

    predictions = []
    def predict_heart_disease(data):
        for modelname in modelnames:
            model = pickle.load(open(modelname,'rb'))
            prediction = model.predict(data)
            predictions.append(prediction)
        return predictions
    
    # Create a submit button to make predictions

    if st.button("Submit"):
        st.subheader('Results....')
        st.markdown('----------------------------')
                    
        result = predict_heart_disease(input_data)

        for i in range(len(predictions)):
            st.subheader (algonames[i])
            if result[i][0] == 0:
                st.write("No heart disease detected.")
            else:
                st.write("Heart disease detected.")
            st.markdown('----------------------------')


