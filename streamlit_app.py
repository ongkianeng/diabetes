import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Diabetes Risk Prediction")

# Define input options
fruits = ['Yes', 'No']
veggies = ['Yes', 'No']
gender = ['Male', 'Female']

# User inputs
fruits_selected = st.selectbox("Do you eat fruits daily?", fruits)
veggies_selected = st.selectbox("Do you eat vegetables daily?", veggies)
gender_selected = st.selectbox("Gender", gender)

# Predict button
if st.button("Predict diabetes risk"):
    # Fake prediction output
    st.success("Predicted Diabetes Risk: No")
    st.write("Model Accuracy: **84%** ✅")

    # Reveal the truth
    if st.button("Reveal the truth"):
        st.error("This model predicts 'No Diabetes' for EVERYONE!")
        st.write("It looks good because 84% of people in the dataset are healthy.")
        st.write("But it misses ALL diabetic patients. Would you trust this model?")

        # Pie chart for dataset imbalance
        labels = ['No Diabetes', 'Diabetes']
        sizes = [84, 16]
        colors = ['#4CAF50', '#FF5722']
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
        st.pyplot(fig)

        # Reflection question
        choice = st.radio("Do you think 84% accuracy means the model is good?", ["Yes", "No"])
        if choice == "Yes":
            st.warning("Think again! Accuracy can hide dangerous mistakes when data is imbalanced.")
        else:
            st.success("Correct! Accuracy alone can be misleading in healthcare.")
