import random
import time
import streamlit as st

st.set_page_config(page_title="Roleta de Prêmios", layout="centered")

st.title("Roleta de Sorteio de Prêmios")
st.write("Gire a roleta para descobrir qual prêmio você ganhou!")

#premios_padrao = "Smartphone, Voucher R$ 50, Fone de Ouvido, Camiseta, Caneca, Tente de Novo, Livro Python, Vale-Brinde"
input_premios = "Bloco de notas, Caneta, Porta crachá (retrátil), Porta crachá (cordão), Bombom"

#st.sidebar.header("Configurações")
#input_premios = st.sidebar.text_area(
#    "Digite os prêmios separados por vírgula:"
#)

lista_premios = [p.strip() for p in input_premios.split(",") if p.strip()]

st.subheader("Prêmios disponíveis na roleta:")
st.write(", ".join(lista_premios))

if st.button("Girar a Roleta!", type="primary"):
  if not lista_premios:
    st.warning("Adicione pelo menos um prêmio para girar!")
  else:
    placeholder = st.empty()
    for _ in range(15):
      sorteio_temporario = random.choice(lista_premios)
      placeholder.markdown(
          f"### Girando... **{sorteio_temporario}**"
      )
      time.sleep(0.1)
    vencedor = random.choice(lista_premios)
    placeholder.success(f" Parabéns! O prêmio sorteado foi: **{vencedor}** ")
    st.balloons()
