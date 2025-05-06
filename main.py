
import streamlit as st
from prediction_helper import predict

st.markdown(
    """
    <style>
    .stApp {
    background: linear-gradient(to bottom right, rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.7));
    position: relative;
    overflow: hidden;
}

.stApp::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-repeat: repeat;
    background-size: 100px 100px;
    z-index: 0;
    opacity: 0.3;
}

/* Content layer */
.stApp > div {
    position: relative;
    z-index: 1;
}   
    body {
        color: white !important;
    }
    .stNumberInput label, .stSelectbox label, .stTextInput label {
        color: white !important;
    }
    /* Selectbox styling */
     div[data-baseweb="select"] {
        background-color: white !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] div {
        color: black !important;
    }

    ul[role="listbox"] {
        background-color: #1e1e1e !important;
        color: white !important;
    }

    li[role="option"]:hover {
        background-color: white !important;
        border: 2px solid black !important;
        border-radius: 4px !important;
    }
    /* Number/Text input styling */
    .stNumberInput input, .stTextInput input {
        background-color: #FFFFFF !important;
        color: black !important;
        border-color: white;
    }
    .st-bb {
        background-color: transparent;
    }
    div[data-testid="stAlert-success"] {
    color: black !important;  /* Or any color you want */
    background-color: rgba(200, 200, 200, 0.6) !important;  /* Optional: grey background */
    border: 2px solid white !important;
    border-radius: 6px;
    }
    .css-1aumxhk {
        background-image: none;
    }
    .stButton>button {
        color: red !important;
        border: 1px solid white;
    }
    .stTitle {
        color: white !important;
    }
    .block-container h1 {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Health Insurance Cost Predictor')


categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')
