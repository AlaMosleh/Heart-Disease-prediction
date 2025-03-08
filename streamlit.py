import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.header("Heart disease prediction")

# Getting the input data from USER
# age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
age = st.number_input("Age")
sex=str(st.selectbox('Gender : Male: 1 ,Female: 0',[1,0]))
cp = int(st.selectbox("Chest Pain Type", [0, 1, 2, 3]))
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs=int(st.selectbox('Fasting Blood sugar : Fasting :1 ,Not fasting: 0',[1,0]))

restecg = int(st.selectbox("Resting ECG",[0, 1, 2]))
thalach = st.number_input("Max Heart Rate")
exang=int(st.selectbox('Exercise Induced Angina',[True,False]))
oldpeak = st.number_input("ST Depression")
slope =int(st.selectbox("Slope",[0, 1, 2]))

ca =int(st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4]))
thal =int(st.selectbox("Thal", [0, 1, 2, 3]))


# Code for prediction
heartDisease_diagnosis = ''

# Prediction
if st.button("Get Results"):
    # Create a NumPy array from the inputs
    input_data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
    # Apply the scaler transformation
    input_data_scaled = scaler.transform(input_data)
    
    # Make the prediction
    hd_pred = model.predict(input_data_scaled)

    # Display the result    
    if hd_pred[0] == 0:
        heartDisease_diagnosis = "The person does not have a heart disease."
        st.success(heartDisease_diagnosis)
    else:
        heartDisease_diagnosis = "The person has heart disease."
        st.error(heartDisease_diagnosis)