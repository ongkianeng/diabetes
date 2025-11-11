import streamlit as st
import matplotlib.pyplot as plt

st.title("Diabetes Risk Prediction")

# Initialize session state
if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "predicted" not in st.session_state:
    st.session_state.predicted = False

# Two columns layout
col1, col2 = st.columns([1, 1])  # Equal width

# Left pane: Inputs
with col1:
    st.subheader("Your Lifestyle Info")
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

# Right pane: Prediction or Reveal
with col2:
    st.subheader("Prediction & Reality")

    # Predict button
    if st.button("Predict diabetes risk"):
        st.session_state.predicted = True
        st.session_state.revealed = False  # Reset reveal if clicked again

    # Reveal button
    if st.session_state.predicted and not st.session_state.revealed:
        st.markdown("<h3 style='color: green;'>Your Predicted Diabetes Risk:</h3>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: green;'>No risk of diabetes</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #2196F3;'>Model Accuracy: <b>84%</b> ✅</h4>", unsafe_allow_html=True)

        if st.button("Reveal the truth"):
            st.session_state.revealed = True

    # Show reveal section (replaces prediction)
    if st.session_state.revealed:
        st.markdown("<h3 style='color: red;'>Reality Check</h3>", unsafe_allow_html=True)
        st.write("This model predicts 'No Diabetes' for EVERYONE!")
        st.write("It looks good because 84% of people in the dataset are healthy.")
        st.write("But it misses ALL diabetic patients. Would you trust this model?")

        # Dramatic scenario
        st.markdown("""
        <div style='background-color:#ffe6e6; padding:15px; border-radius:10px;'>
        <h4 style='color:#b30000;'>Imagine this...</h4>
        <p style='font-size:16px;'>
        Mr X went for a health check-up. The model says: <b>'No risk of diabetes'</b>. Mr X felt safe.<br><br>
        Six months later, Mr X collapsed from undiagnosed diabetes complications.<br>
        The model was <b>84% accurate</b>—but for Mr X, it was 0%.
        </p>
        </div>
        """, unsafe_allow_html=True)

        # Pie chart
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
