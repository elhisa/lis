import streamlit as st

st.title("Hello")

num1 = st.number_input("Digite o primeiro número:")
num2 = st.number_input("Digite o segundo número:")


if st.button("Calcular"):
    resultado = num1 + num2
    st.text("Resultado:")
    st.title(resultado)