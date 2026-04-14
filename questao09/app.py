import streamlit as st

# --- MODELO ---
class Musico:
    def __init__(self, nome):
        self.nome = nome

class Musica:
    def __init__(self, titulo, duracao, musico):
        self.titulo = titulo
        self.duracao = duracao
        self.musico = musico # Relacionamento

class CD:
    def __init__(self, titulo, eh_duplo, eh_coletanea):
        self.titulo = titulo
        self.eh_duplo = eh_duplo
        self.eh_coletanea = eh_coletanea
        self.faixas = []

    def adicionar_faixa(self, musica):
        self.faixas.append(musica)

# --- ENGINE DE DADOS (Simulando Banco de Dados) ---
if 'db' not in st.session_state:
    st.session_state.db = {"musicos": [], "cds": []}

st.title("📀 Gerenciador de Coletâneas Pro")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Músico", "Cadastrar CD", "Relatórios"])

if menu == "Cadastrar Músico":
    nome = st.text_input("Nome do Músico")
    if st.button("Salvar Músico"):
        st.session_state.db["musicos"].append(Musico(nome))
        st.success("Músico cadastrado!")

elif menu == "Cadastrar CD":
    tt = st.text_input("Título do CD")
    c1, c2 = st.columns(2)
    duplo = c1.checkbox("CD Duplo")
    col = c2.checkbox("Coletânea")
    
    if st.button("Criar CD"):
        st.session_state.db["cds"].append(CD(tt, duplo, col))
        st.success("CD criado! Agora adicione faixas nos relatórios.")

elif menu == "Relatórios":
    st.header("🔍 Consultas")
    
    tab1, tab2 = st.tabs(["Por Músico", "Por Música"])
    
    with tab1:
        if st.session_state.db["musicos"]:
            m_sel = st.selectbox("Selecione o Músico", [m.nome for m in st.session_state.db["musicos"]])
            # Lógica de atributo derivado: busca CDs onde o músico aparece
            st.write(f"CDs com participação de: {m_sel}")
            # (Aqui entraria a lógica de filtro nos objetos)
        else:
            st.warning("Cadastre músicos primeiro.")
            
    with tab2:
        st.info("Funcionalidade de rastreio de faixa em CDs (Atributo Derivado)")
