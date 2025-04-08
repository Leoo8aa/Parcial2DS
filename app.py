# app.py (Streamlit)
import streamlit as st
import joblib
import numpy as np
import pickle


with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Título de la app
st.title("Clasificador de Arroz")

# Entrada de datos
st.write("Ingrese los valores de las características:")
feature_values = []
for i in range(X_train.shape[1]):
    value = st.number_input(f"Característica {i+1}", value=0.0)
    feature_values.append(value)

# Predecir
if st.button("Predecir"):
    prediction = model.predict([feature_values])
    st.write(f"Clase predicha: {prediction[0]}")