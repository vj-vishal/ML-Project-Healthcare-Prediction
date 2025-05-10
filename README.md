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
                                                                              'Diabetes & High blood pressure', 'Thyroid', 
                                                                               'Heart disease'
                                                                              'High blood pressure & Heart disease', 
                                                                              'Diabetes & Thyroid',
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
The model is segmented into two age-based groups(18-25 and 26-100) to reduce prediction error, as the project aims to maintain a margin of error below 10%. However, initial results showed that approximately 30% of customers exceeded this threshold, with some errors surpassing 80%.
## Results
**For age group(18-25)** :  
  
1. Feature Importance : 

<img width="649" alt="Image" src="https://github.com/user-attachments/assets/b018b552-35f5-4fc8-ac4c-be672e3ac8ef" /><b>

2. Best Performing model : Linear Regression  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R2 Score = 98%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RSME = 292.80

**For age group(26-100)** :  

1. Feature Importance :

<img width="632" alt="Image" src="https://github.com/user-attachments/assets/44fefd7c-299d-4ee9-a278-45cb1c1da3a4" /><b>

2. Best Performing model : XGBoost Regressor  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;R2 Score = 99.7%  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RSME = 353.73

## Future Improvements
- Experimenting with orher advanced models.
- Deploying the core model as an API using frameworks like FastAPI or Flask.

## Conclusion  
This project provides valueable insights into healthcare insurance prediction, helping insurance company to predict premium healthcare insurance productivily by leveraging machine learning models.

## Streamlit 
https://ml-project-healthcare-prediction.streamlit.app/

## Contact
Linkedln: https://www.linkedin.com/in/vishaljaiswalvj/  
Email: vishaljaiswal529@gmail.com







