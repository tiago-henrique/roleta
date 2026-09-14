import random
import time
import streamlit as st

st.set_page_config(page_title="Roleta de Prêmios", layout="centered")

st.title("Roleta de Sorteio de Prêmios")
st.write("Gire a roleta para descobrir qual prêmio você ganhou!")

premios_padrao = {
    "Bloco de notas": 200,
    "Caneta": 100,
    "Porta crachá (retrátil)": 200,
    "Porta crachá (cordão)": 500,
    "Bombom": 50,
    "Prêmio surpresas": 1,
}

if "quantidades" not in st.session_state:
    st.session_state.quantidades = premios_padrao.copy()

for premio in list(st.session_state.quantidades.keys()):
    col1, col2 = st.sidebar.columns([3, 1])
    with col1:
        nova_quantidade = st.number_input(
            premio,
            min_value=0,
            value=st.session_state.quantidades[premio],
            step=1,
            key=f"qtd_{premio}",
        )
        st.session_state.quantidades[premio] = nova_quantidade
    with col2:
        if st.button("🗑️", key=f"del_{premio}"):
            del st.session_state.quantidades[premio]
            st.rerun()

if st.sidebar.button("Resetar quantidades para o padrão"):
    st.session_state.quantidades = premios_padrao.copy()
    st.rerun()

lista_premios_disponiveis = [
    premio for premio, qtd in st.session_state.quantidades.items() if qtd > 0
]

st.subheader("Prêmios disponíveis na roleta:")
#if lista_premios_disponiveis:
#    resumo = ", ".join(
#        f"{p} ({st.session_state.quantidades[p]})" for p in lista_premios_disponiveis
#    )
#    st.write(resumo)
#else:
#    st.write("Nenhum prêmio disponível no momento.")

if st.button("Girar a Roleta!", type="primary"):
    if not lista_premios_disponiveis:
        st.warning("Não há mais prêmios disponíveis para sortear!")
    else:
        placeholder = st.empty()
        for _ in range(15):
            sorteio_temporario = random.choice(lista_premios_disponiveis)
            placeholder.markdown(f"### Girando... **{sorteio_temporario}**")
            time.sleep(0.1)

        vencedor = random.choice(lista_premios_disponiveis)
        st.session_state.quantidades[vencedor] -= 1

        placeholder.success(f" Parabéns! O prêmio sorteado foi: **{vencedor}** ")
        st.balloons()

        st.info(
            f"Restam **{st.session_state.quantidades[vencedor]}** unidade(s) de **{vencedor}**."
        )
