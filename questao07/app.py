import streamlit as st
import pandas as pd

# --- MODELO ---
class ItemCompra:
    def __init__(self, nome, unidade, qtd_prev, qtd_efet, preco):
        self.nome = nome
        self.unidade = unidade
        self.qtd_prev = qtd_prev
        self.qtd_efet = qtd_efet
        self.preco = preco

    @property
    def subtotal(self):
        return self.qtd_efet * self.preco

class PlanilhaCarolina:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item):
        self.itens.append(item)
    
    @property
    def total_geral(self):
        return sum(item.subtotal for item in self.itens)

# --- INTERFACE ---
st.set_page_config(page_title="Lista de Compras Carolina", page_icon="🛒")
st.title("🛒 Planejamento de Compras - Carolina")

if 'planilha_carol' not in st.session_state:
    st.session_state.planilha_carol = PlanilhaCarolina()

# Cadastro
with st.expander("➕ Adicionar Produto à Lista", expanded=True):
    c1, c2, c3 = st.columns([2, 1, 1])
    nome = c1.text_input("Produto", placeholder="Ex: Arroz")
    unid = c2.text_input("Unidade", placeholder="Ex: Kg")
    p_est = c3.number_input("Preço Estimado (R$)", min_value=0.0, step=0.10)
    
    c4, c5 = st.columns(2)
    q_pre = c4.number_input("Qtd. Prevista (Mês)", min_value=0.0, step=1.0)
    q_efe = q_pre # Sugere a prevista como inicial para a efetiva
    q_efe = c5.number_input("Qtd. Efetiva de Compra", min_value=0.0, value=q_efe, step=0.5)
    
    if st.button("Inserir na Planilha"):
        if nome:
            novo = ItemCompra(nome, unid, q_pre, q_efe, p_est)
            st.session_state.planilha_carol.adicionar(novo)
            st.success(f"{nome} adicionado!")
        else:
            st.error("O nome do produto é obrigatório.")

# Exibição
if st.session_state.planilha_carol.itens:
    st.divider()
    
    # Criando dados para a tabela
    dados = []
    for i in st.session_state.planilha_carol.itens:
        dados.append({
            "Produto": i.nome,
            "Unid.": i.unidade,
            "Qtd. Mês": i.qtd_prev,
            "Qtd. Compra": i.qtd_efet,
            "Preço Est.": f"R$ {i.preco:.2f}",
            "Subtotal": f"R$ {i.subtotal:.2f}"
        })
    
    df = pd.DataFrame(dados)
    st.table(df)
    
    st.subheader(f"💰 Total Estimado da Compra: R$ {st.session_state.planilha_carol.total_geral:.2f}")
    
    if st.button("Limpar Lista"):
        st.session_state.planilha_carol = PlanilhaCarolina()
        st.rerun()
else:
    st.info("A planilha está vazia. Comece cadastrando os itens acima.")
