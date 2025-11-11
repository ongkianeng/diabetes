import streamlit as st
import matplotlib.pyplot as plt

st.title("Diabetes Risk Prediction")

# Define input options
fruits = ['Yes', 'No']
veggies = ['Yes', 'No']
fried_food = ['Yes', 'No']
bubbletea = ['Yes', 'No']
gender = ['Male', 'Female']

# User inputs
fruits_selected = st.selectbox("Do you eat fruits daily?", fruits)
veggies_selected = st.selectbox("Do you eat vegetables daily?", veggies)
fried_food_selected = st.selectbox("Do you eat fried food daily?", fried_food)
bubbletea_selected = st.selectbox("Do you drink bubble tea more than 3X a week?", bubbletea)
gender_selected = st.selectbox("Gender", gender)

# Initialize session state
if "show_reveal" not in st.session_state:
    st.session_state.show_reveal = False

# Predict button
if st.button("Predict diabetes risk"):
    st.markdown("<h2 style='color: green;'>Your Predicted Diabetes Risk: No risk of diabetes</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #2196F3;'>Model Accuracy: <b>84%</b> ✅</h3>", unsafe_allow_html=True)

    # Show reveal button
    if st.button("Reveal the truth"):
        st.session_state.show_reveal = True

# Reveal section (persistent)
if st.session_state.show_reveal:
    st.markdown("<h2 style='color: red;'>This model predicts 'No Diabetes' for EVERYONE!</h2>", unsafe_allow_html=True)
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
