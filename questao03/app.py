import streamlit as st

# --- MODELO (CLASSE) ---
class Boneco:
    def __init__(self, nome):
        self.nome = nome
        self.pos_x = 50  # Posição inicial centralizada (0-100)
        self.pos_y = 50
        self.direcao = "Direita"

    def mover(self):
        passo = 5
        if self.direcao == "Cima":
            self.pos_y = max(0, self.pos_y - passo)
        elif self.direcao == "Baixo":
            self.pos_y = min(100, self.pos_y + passo)
        elif self.direcao == "Esquerda":
            self.pos_x = max(0, self.pos_x - passo)
        elif self.direcao == "Direita":
            self.pos_x = min(100, self.pos_x + passo)

# --- INTERFACE ---
st.title("🏃 Boneco em Movimento")

if 'boneco' not in st.session_state:
    st.session_state.boneco = Boneco("Robot")

# Controles
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Controles")
    nome_input = st.text_input("Nome do Boneco", value=st.session_state.boneco.nome)
    st.session_state.boneco.nome = nome_input
    
    st.write(f"**Direção Atual:** {st.session_state.boneco.direcao}")
    
    # Botões de movimento
    st.button("⬆️ Cima", on_click=lambda: setattr(st.session_state.boneco, 'direcao', 'Cima'))
    c1, c2 = st.columns(2)
    c1.button("⬅️ Esquerda", on_click=lambda: setattr(st.session_state.boneco, 'direcao', 'Esquerda'))
    c2.button("➡️ Direita", on_click=lambda: setattr(st.session_state.boneco, 'direcao', 'Direita'))
    st.button("⬇️ Baixo", on_click=lambda: setattr(st.session_state.boneco, 'direcao', 'Baixo'))
    
    if st.button("EXECUTAR MOVIMENTO 🚀", type="primary"):
        st.session_state.boneco.mover()

with col2:
    st.subheader("Campo de Movimento")
    
    # Criando o boneco visualmente usando CSS inline
    x = st.session_state.boneco.pos_x
    y = st.session_state.boneco.pos_y
    
    campo_html = f"""
    <div style="position: relative; width: 100%; height: 300px; background-color: #f0f2f6; border: 2px solid #ccc; border-radius: 10px;">
        <div style="position: absolute; left: {x}%; top: {y}%; transform: translate(-50%, -50%); transition: all 0.3s ease;">
            <div style="text-align: center;">
                <span style="font-size: 30px;">🧍</span><br>
                <span style="background: black; color: white; padding: 2px 5px; border-radius: 5px; font-size: 10px;">{st.session_state.boneco.nome}</span>
            </div>
        </div>
    </div>
    """
    st.markdown(campo_html, unsafe_allow_html=True)
    st.info(f"Coordenadas: X={x} | Y={y}")

st.markdown("---")
