import streamlit as st
from app.validator import validate_jwt

st.title("JWT Token Validator")

jwt_token = st.text_area("Paste your JWT token here")
secret = st.text_input("Enter the secret key", type="password")
algorithms = st.multiselect("Select algorithm(s)", ["HS256", "HS384", "HS512"], default=["HS256"])

if st.button("Validate Token"):
    if jwt_token and secret:
        valid, result = validate_jwt(jwt_token.strip(), secret.strip(), algorithms)
        if valid:
            st.success("Token is valid!")
            st.json(result)
        else:
            st.error(result)
    else:
        st.warning("Please provide both the JWT token and secret key.")
