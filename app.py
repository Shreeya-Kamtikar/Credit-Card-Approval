import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("randomforest.pickle", "rb"))

# Create a Streamlit app
st.title("Credit Card Approval Predictor")

# Create input fields for user input
st.header("Enter your information:")
reports = st.number_input('Number of major derogatory reports',0)
age = st.text_input('Age', 30)
income = st.number_input("Yearly Income")
owner = st.radio('Own house?', ['Yes', 'No'])
selfemp	= st.radio('Self employed?', ['Yes', 'No'])
dependents = st.number_input("Number of people in family(including yourself)", 1)
months = st.number_input("Number of months living at current location: ", 2)
majorcards = st.number_input("Number of major credit cards held: ", 0)
active = st.number_input("Number of active credit accounts: ",1)

# Create a button to submit the input
submit_button = st.button("Submit")

# Define a function to make predictions
def make_prediction(reports,age,income,owner,selfemp,dependents,months,majorcards,active):
    input_data = pd.DataFrame({
        "reports": [reports],
        "age": [age],
        "income": [income],
        "owner": [owner],
        "selfemp": [selfemp],
        "dependents": [dependents],
        "months": [months],
        "majorcards": [majorcards],
        "active": [active]
    })
    input_data["owner"] = input_data["owner"].map(lambda x: 1 if x == "yes" else 0)
    input_data["selfemp"] = input_data["selfemp"].map(lambda x: 1 if x == "yes" else 0)
    prediction = model.predict(input_data)
    return prediction[0]

# Make a prediction when the submit button is clicked
if submit_button:
    prediction = make_prediction(reports,age,income,owner,selfemp,dependents,months,majorcards,active)
    st.header("Prediction:")
    if prediction == 1:
        st.write("You are likely to be approved for a credit card!")
    else:
        st.write("You are unlikely to be approved for a credit card.")