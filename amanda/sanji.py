import streamlit as st

st.title("Converter Graus pra Fahrenheit ")

num = st.number_input("Digite uma temperatura em Graus: ")
if st.button("Converter para Fahrenheit"):
    resultado = num * 1.8 + 32
    st.text("Resultado:")
    st.title(resultado)

st.title("Converter Fahrenheit para Graus")

num = st.number_input("Digite uma temperatura em Fahrenheit: ")
if st.button("Converter para Graus"):
    result1= (num - 32) / 1.8
    st.text("Resultado:")
    st.title(result1)