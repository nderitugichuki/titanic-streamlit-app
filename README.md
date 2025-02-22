# Titanic Survival Prediction - Streamlit App  

This project is a **machine learning-powered web app** built using **Streamlit**. It predicts whether a Titanic passenger would have survived based on features such as **passenger class, age, fare, family size, and embarkation point**. The app utilizes a **trained Random Forest model** and provides an interactive UI for users to enter their details and get a prediction.  

---

## Features  

- **User-friendly Interface:** Built with **Streamlit**, making it intuitive and interactive  
- **Machine Learning Model:** Uses a pre-trained **Random Forest Classifier**  
- **Real-time Predictions:** Users input their details and receive instant survival predictions  
- **Multiple Input Features:** Supports **Pclass, Age, Fare, SibSp, Parch, Sex, Embarked, and FamilySize**  
- **Deployed on Streamlit Cloud** (Guide provided below)  

---

## Setup & Installation  

To run this project on your local machine, follow these steps:  

### 1. Clone the Repository  
First, download the project files from GitHub:  
```bash
git clone https://github.com/nderitugichuki/titanic-streamlit-app.git
cd titanic-streamlit-app
```

### 2. Create a Virtual Environment (Optional but Recommended)  
It’s best practice to use a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies  
Ensure all required Python libraries are installed:  
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App  
Launch the app locally with:  
```bash
streamlit run app.py
```
This will open the app in your browser.

---

## Deployment Guide (Streamlit Cloud)  

### 1. Push Your Code to GitHub  
Ensure your latest code is pushed to GitHub:  
```bash
git add .
git commit -m "Updated Streamlit app"
git push origin main
```

### 2. Deploy on Streamlit Cloud  
1. Go to [Streamlit Cloud](https://share.streamlit.io/)  
2. Click **"New app"** and connect your GitHub repository  
3. Select your repository (`nderitugichuki/titanic-streamlit-app`)  
4. Set `app.py` as the **entry point**  
5. Click **"Deploy"**  
6. Wait for the app to build, then share your deployment link  

---

## Project Structure  

```
📦 titanic-streamlit-app
 ┣ 📜 app.py               # Main Streamlit application script
 ┣ 📜 titanic_best_rf_model.pkl  # Trained Random Forest model (saved with Pickle)
 ┣ 📜 requirements.txt     # List of dependencies for the project
 ┣ 📜 README.md            # Project documentation
 ┣ 📜 .gitignore           # Files to exclude from Git tracking
 ┗ 📂 images/              # (Optional) Images for documentation/screenshots
```

---

## How It Works  

1. **User Inputs**  
   - **Pclass (1st, 2nd, 3rd Class)**  
   - **Age** (Passenger’s age)  
   - **Fare** (Ticket price paid)  
   - **SibSp** (Siblings/Spouses aboard)  
   - **Parch** (Parents/Children aboard)  
   - **Sex** (Male/Female)  
   - **Embarked** (Port of boarding - Q, S, or C)  
   - **FamilySize** (Number of family members aboard)  

2. **Model Prediction**  
   - The trained **Random Forest model** takes these inputs  
   - It predicts **Survival (1) or Not Survived (0)**  

3. **Output Display**  
   - If `1`, the app displays **"The passenger survived!"**  
   - If `0`, the app displays **"The passenger did not survive."**  

---

## Technical Details  

- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Machine Learning Model:** Random Forest Classifier  
- **Data Preprocessing:** Handled using Pandas & Scikit-learn  
- **Deployment:** Streamlit Cloud  

---

## License  

This project is open-source under the **MIT License**. You are free to use, modify, and distribute it.  

---

