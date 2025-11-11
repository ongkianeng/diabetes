import streamlit as st
import matplotlib.pyplot as plt

# Title with big font
st.markdown("<h3 style='text-align: center; color: #FF5722;'>Diabetes Risk Prediction</h3>", unsafe_allow_html=True)

# Inputs
fruits = ['Yes', 'No']
veggies = ['Yes', 'No']
fried_food = ['Yes', 'No']
bubbletea = ['Yes', 'No']
gender = ['Male', 'Female']

fruits_selected = st.selectbox("Do you eat fruits daily?", fruits)
veggies_selected = st.selectbox("Do you eat vegetables daily?", veggies)
fried_food_selected = st.selectbox("Do you eat fried food daily?", fried_food)
bubbletea_selected = st.selectbox("Do you drink bubble tea more than 3X a week?", bubbletea)
gender_selected = st.selectbox("Gender", gender)

if st.button("Predict diabetes risk"):
    # Fake prediction output
    st.markdown("<h3 style='color: green;'>You're safe. No risk of diabetes</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #2196F3;'>Model Accuracy: <b>84%</b> ✅</h3>", unsafe_allow_html=True)

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
