import streamlit as st
import pandas as pd

st.title("🎵 Coleção de CDs")

# Inicializa lista
if "cds" not in st.session_state:
    st.session_state.cds = []

# Entrada
artista = st.text_input("Artista / Banda:")
titulo = st.text_input("Título do CD:")
ano = st.number_input("Ano de lançamento:", min_value=1900, max_value=2100)

# Adicionar CD
if st.button("Adicionar CD"):
    cd = {
        "artista": artista,
        "titulo": titulo,
        "ano": ano
    }
    st.session_state.cds.append(cd)
    st.success("CD adicionado!")

# Exibir coleção
if st.session_state.cds:
    df = pd.DataFrame(st.session_state.cds)

    st.subheader("📀 Lista de CDs")
    st.dataframe(df)

    # Total
    st.write(f"Total de CDs: {len(df)}")

    # Busca por artista
    busca = st.text_input("Buscar por artista:")

    if busca:
        resultado = df[df["artista"].str.contains(busca, case=False)]
        st.subheader("🔍 Resultado da busca")
        st.dataframe(resultado)
