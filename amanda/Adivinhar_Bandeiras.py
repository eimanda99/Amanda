import streamlit as st
import random

Brasil = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/2560px-Flag_of_Brazil.svg.png"
Estados_Unidos = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/1920px-Flag_of_the_United_States.svg.png"
Franca = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1920px-Flag_of_France.svg.png"
Japao = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/2560px-Flag_of_Japan.svg.png"
Alemanha = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png"

bandeiras = [Brasil, Estados_Unidos, Franca, Japao, Alemanha]

st.title("Jogo de Adivinhação de Bandeiras")
st.write("Tente adivinhar a bandeira do país!")

tentativas = 5
pontuacao = 0

for bandeira_atual in bandeiras:
   bandeira_atual = random.choice(bandeiras)
   if st.button ("Iniciar Jogo"):
    st.image(bandeira_atual)
    palpite = st.text_input("Digite o nome do país:")
    if palpite == bandeira_atual:
      st.success("Correto!")
      pontuacao += 1
else:
    print(f"Resposta errada! A resposta certa era {bandeira_atual}")
    tentativas -= 1

if tentativas == 0:
    st.write("Fim de jogo")

print(f"Pontuação: {pontuacao}")
print(f"Tentativas Restantes: {tentativas}")


print(f"Jogo encerrado. Sua pontuação final: {pontuacao}")
