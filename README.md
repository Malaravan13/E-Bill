⚡ Electricity Bill Prediction – End-to-End ML Project

📌 Project Overview
This is an End-to-End Machine Learning application that predicts electricity bill amount based on the number of units consumed.
It demonstrates the complete ML lifecycle including data preprocessing, model training, model persistence, and a Streamlit-powered frontend for interactive predictions.

🚀 Features

📊 Predict electricity bill amount (₹) based on units consumed

⚡ Real-time prediction through a Streamlit web app

🛠️ Model trained using Linear Regression

🔍 Model evaluation with R² score and error metrics

💾 Model persistence using Pickle for reusability

🖥️ Clean and user-friendly UI for input and output

🛠️ Tech Stack

Python 🐍

Scikit-learn (ML model)

Streamlit (Frontend UI)

NumPy / Pandas (Data handling & preprocessing)

Matplotlib / Seaborn (Data visualization)

📂 Project Structure
E2E_ElectricityBill/
├── bill_prediction.ipynb     # Jupyter notebook for model training & testing
├── trained_model.sav         # Saved ML model (Pickle)
├── app.py                    # Streamlit web app
├── requirements.txt          # Required dependencies
├── README.md                 # Project documentation

⚙️ Installation & Setup

Clone this repository

git clone https://github.com/Mlaravan13/E-Bill.git
cd E-Bill


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

🖥️ Usage

Enter the number of units consumed

Click Predict Bill

✅ The model outputs the estimated electricity bill (₹)

📊 Model Performance

Algorithm: Linear Regression

Evaluation Metrics:

R² Score: ~ 0.002456222817075693

Mean Absolute Error (MAE): High

Mean Squared Error (MSE): High

Here’s how the Electricity Bill Predictor app looks:

![alt text](<Screenshot (344).png>)