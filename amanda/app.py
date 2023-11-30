import streamlit as st

st.title("Hello")

num1 = st.number_input("Digite o primeiro número: ")
num2 = st.number_input("Digite o segundo número: ")

st.text("Calculadora")

if st.button("Calcular Soma"):
    resultado = num1 + num2
    st.text("Resultado:")
    st.title(resultado)

if st.button("Calcular Multiplicação"):
    result1 = num1 * num2
    st.text("Resultado:")
    st.title(result1)

if st.button("Calcular Subtração"):
    result2 = num1 - num2
    st.text("Resultado:")
    st.title(result2)

if st.button("Calcular Divisão"):
    result3 = num1/num2
    st.text("Resultado:")
    st.title(result3)




