# ML-Project-Healthcare-Prediction
## Project Overview
This Project focusses on developing a predictive model for an Insurance Company to estimate health insurance 
premiums based on factors like age, smoking habits, BMI, and medical history and Deploying application on streamlit.
## Dataset Information 
- **Age** : Age of the individual in years
- **Gender** : Gender of the policyholder('Male', 'Female')
- **Region** : Geographic location or region of residence('Northwest', 'Southeast', 'Northeast', 'Southwest')
- **Marital Status** : Marital status of the individual('Unmarried', 'Married')
- **Number of Dependants** : Number of people financially dependent on the individual
- **BMI Category** : Body Mass Index category of the individual('Normal', 'Obesity', 'Overweight', 'Underweight')
- **Smoking Status** : Indicates if the individual currently smokes or has smoked in the past('No Smoking', 'Regular', 'Occasional')
- **Employment Status** : ('Salaried', 'Self-Employed', 'Freelancer')
- **Income level** : General income classification('<10L','10L - 25L','> 40L','25L - 40L')
- **Income lakhs** : Exact annual income in lakhs of rupees
- **Medical History** : Summarized medical history or pre-existing conditions('Diabetes', 'High blood pressure', 'No Disease',
                                                                              'Diabetes & High blood pressure', 'Thyroid', 'Heart disease'
                                                                              'High blood pressure & Heart disease', 'Diabetes & Thyroid',
                                                                              'Diabetes & Heart disease')
- **Insurance Plan** : Type of insurance plan selected by the user('Bronze', 'Silver', 'Gold')
- **Genetical Risk** : Indicates the individual's inherited predisposition to certain diseases or health conditions based on family history or genetic testing
- **Annual Premium Amount** : The target variable – the total yearly premium to be paid for the health insurance plan
## Objectives 
- Develop a high-accuracy (>97%) predictive model. The percentage difference between the predicted and actual value on a minimum of 95% of the errors should be less than 
10%. 
- Deploy the model in the cloud so that an insurance underwriter can run it from anywhere. 
- Create an interactive Streamlit application that an underwriter can use for predictions.
## Scope of Work
### 1. Data Collection and Preprocessing  
  - Collect and clean labeled datasets.  
  - Perform exploratory data analysis (EDA).
  - Perform Featuring Engineering
### 2. Model Development  
  - Train and evaluate multiple models.  
  - Optimize the best model for accuracy. 
### 3. Model Deployment  
  - Deploy the model on a cloud platform.  
  - Ensure security and scalability. 
### 4. Streamlit Application Development  
  - Build an interactive app for inputting factors and displaying predictions. 
### 5. Testing and Validation  
  - Rigorous testing and validation with real-world data. 
### 6. Documentation and Training  
  - Provide documentation and training for underwriters.
## Insights  
The model is segmented into two age-based groups to reduce prediction error, as the project aims to maintain a margin of error below 10%. However, initial results showed that approximately 30% of customers exceeded this threshold, with some errors surpassing 80%. 



