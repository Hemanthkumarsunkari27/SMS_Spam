import streamlit as st
import pickle

# Load your model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("SMS Spam Detection System")

# Input from user
user_input = st.text_input("Enter your message:")
if st.button("Predict"):
    data = vectorizer.transform([user_input])
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.error("This message is Spam!")
    else:
        st.success("This message is Not Spam.")


       
 

