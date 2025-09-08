import streamlit as st
import joblib as jl

model = jl.load("regression.joblib")

size = st.number_input("size", value=50)
nb_rooms = st.number_input("nb_rooms", value=2)
garden = st.checkbox("garden", value=False)

prediction = model.predict([[size, nb_rooms, garden]])

st.write(f"predicted price: {prediction[0]}")