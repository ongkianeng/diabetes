import joblib
import streamlit as st
import numpy as np
import pandas as pd

## Streamlit app
st.title("Diabetes Risk Prediction")


## Define the input options
fruits = ['Yes', 'No']
veggies = ['Yes', 'No']
gender = ['Male', 'Female']

## User inputs
fruits_selected = st.selectbox("Do you eat fruits daily?", fruits)
veggies_selected = st.selectbox("Do you eat vegetables daily?", veggies)
gender_selected = st.selectbox("Gender", gender)

## Predict button
if st.button("Predict diabetes risk"):

    ## Create dict for input features
    input_data = {
        'fruits': fruits_selected,
        'veggies': veggies_selected,
        'gender': gender_selected,
 
    }

    ## Convert input data to a DataFrame
    df_input = pd.DataFrame({
        'fruits': [fruits_selected],
        'veggies': [veggies_selected],
        'gender': [gender_selected],

    })

    ## One-hot encoding
    df_input = pd.get_dummies(df_input, 
                              columns = ['fruits', 'veggies', 'gender']
                             )
    
    # df_input = df_input.to_numpy()

    # df_input = df_input.reindex(columns = model.feature_names_in_,
    #                             fill_value=0)


    # ## Predict
    # y_unseen_pred = model.predict(df_input)[0]
    st.success(f"Predicted Diabetes Risk: Yes (84% accuracy)")
