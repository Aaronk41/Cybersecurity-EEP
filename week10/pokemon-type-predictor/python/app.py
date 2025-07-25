# python/app.py

import streamlit as st
import joblib
import numpy as np

# Load the model
model_data = joblib.load('model/pokemon_type_predictor.pkl')
clf = model_data['model']
scaler = model_data['scaler']
le = model_data['le']

st.set_page_config(page_title="Pokémon Type Predictor", page_icon="🧠")

st.title("🧬 Pokémon Type Predictor")
st.markdown("Enter the base stats of a Pokémon and we'll predict its **Type 1**!")

# Input sliders
hp = st.slider('HP', 1, 255, value=70)
attack = st.slider('Attack', 1, 190, value=70)
defense = st.slider('Defense', 1, 250, value=70)
sp_atk = st.slider('Sp. Atk', 1, 200, value=70)
sp_def = st.slider('Sp. Def', 1, 250, value=70)
speed = st.slider('Speed', 1, 200, value=70)
total = hp + attack + defense + sp_atk + sp_def + speed

# Predict
if st.button("Predict Type"):
    input_data = np.array([[hp, attack, defense, sp_atk, sp_def, speed, total]])
    input_scaled = scaler.transform(input_data)
    pred = clf.predict(input_scaled)
    pred_type = le.inverse_transform(pred)[0]
    st.success(f"Predicted Pokémon Type 1: **{pred_type}**")
