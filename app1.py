import streamlit as st  # Import Streamlit (for the web app)
import pickle  # Import pickle (to load your model)
import pandas as pd  # Import pandas (to handle data)

# Load the saved Titanic model
with open("titanic_best_rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# App Title
st.title("Titanic Survival Prediction 🚢")

# User Inputs
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])  # Dropdown to select class
age = st.number_input("Age", min_value=1, max_value=100)  # Box to enter age
fare = st.number_input("Fare", min_value=0.0, max_value=600.0)  # Box to enter ticket fare
sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=8)  # Family aboard
parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=6)  # Parents/Kids aboard
sex = st.selectbox("Sex", ["Male", "Female"])  # Dropdown for gender
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"]) 

# Convert categorical inputs to numerical
sex = 1 if sex == "Male" else 0

# One-hot encoding for 'Embarked'
Embarked_Q = 1 if embarked == "Q" else 0
Embarked_S = 1 if embarked == "S" else 0

# Calculate FamilySize
family_size = sibsp + parch + 1
st.write(f"📌 Family Size: {family_size}")  # Display FamilySize

#create table for user input
input_data = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, Embarked_Q, Embarked_S, family_size]], 
                          columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S', 'FamilySize'])

# Prediction Button
if st.button("Predict Survival"):  # When user clicks "Predict"
    prediction = model.predict(input_data)  # Use the model to predict survival
    
    # Show results
    if prediction[0] == 1:
        st.success("The passenger **survived**! 🎉")  # Green success message
    else:
        st.error("The passenger **did not survive**. 😔")  # Red error message
