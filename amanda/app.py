import streamlit as st
import random

palavras = ["python", "programacao", "streamlit", "jogo", "forca", "aleatorio"]

palavra_escolhida = random.choice(palavras)

letras_erradas = []

letras_corretas = ["_"] * len(palavra_escolhida)

max_tentativas = 6

while max_tentativas > 0:
    st.text("Palavra: " + " ".join(letras_corretas))
    st.text("Letras erradas: " + " ".join(letras_erradas))
    letra = st.text_input("Digite uma letra:")
    if letra in palavra_escolhida: 
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_corretas[i] = letra
    else:
        letras_erradas.append(letra)
        max_tentativas -= 1
    if "_" not in letras_corretas:
        st.text("Parabéns! Você venceu!")
        break
    if max_tentativas == 0:
        st.text(f"Você perdeu! A palavra era: {palavra_escolhida}")
        break

