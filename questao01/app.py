import streamlit as st
import pandas as pd

# Classe conforme Diagrama UML
class ContaLuz:
    def __init__(self, data_leitura, num_leitura, kw_gasto, valor_pagar, data_pagamento, media_consumo):
        self.data_leitura = data_leitura
        self.num_leitura = num_leitura
        self.kw_gasto = float(kw_gasto)
        self.valor_pagar = float(valor_pagar)
        self.data_pagamento = data_pagamento
        self.media_consumo = float(media_consumo)

st.set_page_config(page_title="Questão 01 - Conta de Luz", layout="wide")
st.title("💡 Acompanhamento de Gasto de Luz")

if 'contas' not in st.session_state:
    st.session_state.contas = []

# Sidebar para Cadastro
with st.sidebar:
    st.header("Novo Registro")
    with st.form("add_conta"):
        d_lei = st.text_input("Data Leitura", placeholder="DD/MM/AAAA")
        n_lei = st.number_input("Nº Leitura", step=1)
        kw = st.number_input("KW Gasto", step=0.1)
        val = st.number_input("Valor a Pagar", step=0.01)
        d_pag = st.text_input("Data Pagamento")
        med = st.number_input("Média Consumo", step=0.01)
        if st.form_submit_button("Salvar na Planilha"):
            st.session_state.contas.append(ContaLuz(d_lei, n_lei, kw, val, d_pag, med))

# Exibição e Lógica
if st.session_state.contas:
    df = pd.DataFrame([vars(c) for c in st.session_state.contas])
    df.columns = ["Data Leitura", "Nº Leitura", "KW Gasto", "Valor a Pagar", "Data Pagamento", "Média Consumo"]
    st.table(df)

    # Teste de Lógica: Menor/Maior Consumo
    menor = min(st.session_state.contas, key=lambda x: x.kw_gasto)
    maior = max(st.session_state.contas, key=lambda x: x.kw_gasto)
    
    col1, col2 = st.columns(2)
    col1.metric("Menor Consumo", f"{menor.kw_gasto} KW", f"Mês: {menor.data_leitura}")
    col2.metric("Maior Consumo", f"{maior.kw_gasto} KW", f"Mês: {maior.data_leitura}")
else:
    st.warning("Aguardando dados para análise...")
