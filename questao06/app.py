import streamlit as st

# --- MODELO ---
class ItemComanda:
    def __init__(self, nome, valor, qtd):
        self.nome = nome
        self.valor = valor
        self.qtd = qtd
    
    @property
    def subtotal(self):
        return self.valor * self.qtd

class Comanda:
    def __init__(self, numero):
        self.numero = numero
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    @property
    def valor_total(self):
        return sum(item.subtotal for item in self.itens)

# --- INTERFACE ---
st.set_page_config(page_title="Padaria Doce Sabor", page_icon="🥖")
st.title("🥖 Padaria Doce Sabor - PDV")

if 'comanda' not in st.session_state:
    st.session_state.comanda = None

# Iniciar Comanda
if st.session_state.comanda is None:
    with st.form("abrir_comanda"):
        num = st.number_input("Número da Comanda", min_value=1, step=1)
        if st.form_submit_button("Abrir Comanda"):
            st.session_state.comanda = Comanda(num)
            st.rerun()
else:
    st.subheader(f"🛒 Comanda Nº: {st.session_state.comanda.numero}")
    
    # Registro de Produtos
    with st.expander("➕ Lançar Produto", expanded=True):
        c1, c2, c3 = st.columns([2, 1, 1])
        prod = c1.text_input("Produto")
        preco = c2.number_input("Preço Unit. (R$)", min_value=0.0, step=0.10)
        qtd = c3.number_input("Qtd", min_value=1, step=1)
        
        if st.button("Adicionar à Comanda"):
            if prod:
                novo_item = ItemComanda(prod, preco, qtd)
                st.session_state.comanda.adicionar_item(novo_item)
                st.success(f"{prod} adicionado!")
            else:
                st.error("Informe o nome do produto.")

    # Exibição dos Itens
    if st.session_state.comanda.itens:
        st.write("---")
        for item in st.session_state.comanda.itens:
            st.text(f"{item.qtd}x {item.nome} (R$ {item.valor:.2f}) = R$ {item.subtotal:.2f}")
        
        st.divider()
        st.subheader(f"Total a Pagar: R$ {st.session_state.comanda.valor_total:.2f}")
        
        if st.button("Finalizar e Fechar Comanda", type="primary"):
            st.balloons()
            st.success("Compra finalizada com sucesso!")
            st.session_state.comanda = None # Reseta para a próxima
            if st.button("Nova Venda"):
                st.rerun()
