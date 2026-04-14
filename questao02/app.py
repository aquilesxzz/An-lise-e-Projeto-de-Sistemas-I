import streamlit as st

class TextoSaida:
    def __init__(self, texto, tamanho, cor_f, cor_b, tipo):
        self.texto = texto
        self.tamanho = tamanho
        self.cor_f = cor_f
        self.cor_b = cor_b
        self.tipo = tipo

    def render(self):
        # Mapeamento de cores para CSS
        cores_map = {"preto": "black", "branco": "white", "azul": "blue", "amarelo": "yellow", "cinza": "gray"}
        f_color = cores_map[self.cor_f]
        b_color = cores_map[self.cor_b]
        
        estilo = f"font-size:{self.tamanho}px; color:{f_color}; background-color:{b_color}; border:1px solid #000; padding:5px;"
        
        if self.tipo == "Label":
            return f"<p style='{estilo}'>{self.texto}</p>"
        elif self.tipo == "Edit":
            return f"<input type='text' value='{self.texto}' style='{estilo} width:100%;'>"
        else: # Memo
            return f"<textarea style='{estilo} width:100%; height:100px;'>{self.texto}</textarea>"

st.title("🔠 Configuração de Componente de Saída")

with st.expander("Configurar Atributos da Classe", expanded=True):
    t = st.text_input("Texto", "Olá Mundo")
    tam = st.slider("Tamanho da Letra", 10, 50, 20)
    c1, c2, c3 = st.columns(3)
    cf = c1.selectbox("Cor da Fonte", ["preto", "branco", "azul", "amarelo", "cinza"])
    cb = c2.selectbox("Cor do Fundo", ["branco", "preto", "azul", "amarelo", "cinza"])
    tp = c3.radio("Tipo de Componente", ["Label", "Edit", "Memo"])

# Instanciação da Classe e Chamada do Método
obj = TextoSaida(t, tam, cf, cb, tp)

st.subheader("Resultado do Objeto:")
st.markdown(obj.render(), unsafe_allow_html=True)
