import streamlit as st
from datetime import date
import pandas as pd

st.title("💰 Controle de Gastos Diários")

# Inicializa lista
if "gastos" not in st.session_state:
    st.session_state.gastos = []

# Entrada
tipo = st.text_input("Tipo do gasto:")
data = st.date_input("Data:")
valor = st.number_input("Valor:", min_value=0.0)
forma = st.selectbox("Forma de pagamento:", 
                     ["Dinheiro", "Crédito", "Débito", "Ticket Alimentação", "Refeição"])

# Adicionar gasto
if st.button("Adicionar Gasto"):
    gasto = {
        "tipo": tipo,
        "data": data,
        "valor": valor,
        "forma": forma
    }
    st.session_state.gastos.append(gasto)
    st.success("Gasto adicionado!")

# Mostrar dados
if st.session_state.gastos:
    df = pd.DataFrame(st.session_state.gastos)

    st.subheader("📋 Gastos registrados")
    st.dataframe(df)

    # Total mensal
    total = df["valor"].sum()
    st.subheader(f"💵 Total mensal: R$ {total:.2f}")

    # Agrupado por tipo
    st.subheader("📊 Por tipo")
    st.write(df.groupby("tipo")["valor"].sum())

    # Agrupado por forma de pagamento
    st.subheader("💳 Por forma de pagamento")
    st.write(df.groupby("forma")["valor"].sum())
