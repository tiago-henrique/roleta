import random
import time
import streamlit as st

st.set_page_config(page_title="Roleta de Prêmios", page_icon="🎯", layout="centered")

st.title("🎯 Roleta de Sorteio de Prêmios")
st.write("Gire a roleta para descobrir qual prêmio você ganhou!")

# Lista padrão de prêmios
premios_padrao = "Smartphone, Voucher R$ 50, Fone de Ouvido, Camiseta, Caneca, Tente de Novo, Livro Python, Vale-Brinde"

# Área para configurar os prêmios na barra lateral ou na tela
st.sidebar.header("Configurações")
input_premios = st.sidebar.text_area(
    "Digite os prêmios separados por vírgula:", premios_padrao
)

# Converte o texto em uma lista de prêmios
lista_premios = [p.strip() for p in input_premios.split(",") if p.strip()]

st.subheader("Prêmios disponíveis na roleta:")
st.write(", ".join(lista_premios))

# Botão para girar a roleta
if st.button("Girar a Roleta! 🎲", type="primary"):
  if not lista_premios:
    st.warning("Adicione pelo menos um prêmio para girar!")
  else:
  # Elemento visual para simular o giro
    placeholder = st.empty()

    # Efeito de animação girando rapidamente
    for _ in range(15):
      sorteio_temporario = random.choice(lista_premios)
      placeholder.markdown(
          f"### 🔄 Girando... **{sorteio_temporario}**"
      )
      time.sleep(0.1)

    # Resultado final
    vencedor = random.choice(lista_premios)
    placeholder.success(f"🎉 Parabéns! O prêmio sorteado foi: **{vencedor}** 🎁")
    st.balloons()
