import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu

# Load models from relative paths
base_path = os.path.dirname(file) if 'file' in locals() else "."
diabetes_model = pickle.load(open(os.path.join(base_path, 'diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(base_path, 'heart_disease_model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(base_path, 'parkinsons_model.sav'), 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

# ------------- Diabetes Prediction Page -------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            input_data = [float(i) for i in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            prediction = diabetes_model.predict([input_data])
            diab_diagnosis = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numerical values.'
        st.success(diab_diagnosis)

# ------------- Heart Disease Prediction Page -------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex')
    with col3: cp = st.text_input('Chest Pain')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1: restecg = st.text_input('Resting ECG')
    with col2: thalach = st.text_input('Max Heart Rate')
    with col3: exang = st.text_input('Exercise Induced Angina')
    with col1: oldpeak = st.text_input('ST depression')
    with col2: slope = st.text_input('Slope of ST segment')
    with col3: ca = st.text_input('Major vessels colored')
    with col1: thal = st.text_input('Thal (0=normal, 1=fixed defect, 2=reversable)')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [float(i) for i in [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                             exang, oldpeak, slope, ca, thal]]
            prediction = heart_disease_model.predict([input_data])
            heart_diagnosis = 'The person has heart disease' if prediction[0] == 1 else 'The person does not have heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numerical values.'
        st.success(heart_diagnosis)

# ------------- Parkinson's Prediction Page -------------
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    fields = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    inputs = []
    for i in range(0, len(fields), 5):
        cols = st.columns(5)
        for j, field in enumerate(fields[i:i+5]):
            with cols[j]:
                val = st.text_input(field)
                inputs.append(val)

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [float(i) for i in inputs]
            prediction = parkinsons_model.predict([input_data])
            parkinsons_diagnosis = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numerical values.'
        st.success(parkinsons_diagnosis)