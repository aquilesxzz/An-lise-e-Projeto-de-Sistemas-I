import streamlit as st
from datetime import datetime, time

# --- MODELO ---
class Sala:
    def __init__(self, nome, lugares):
        self.nome = nome
        self.lugares = lugares

class Funcionario:
    def __init__(self, nome, cargo, ramal):
        self.nome = nome
        self.cargo = cargo
        self.ramal = ramal

class Reserva:
    def __init__(self, sala, funcionario, data, hora, assunto):
        self.sala = sala
        self.funcionario = funcionario
        self.data = data
        self.hora = hora
        self.assunto = assunto

# --- DATABASE EM MEMÓRIA ---
if 'salas' not in st.session_state:
    st.session_state.salas = [Sala("101", 10), Sala("105", 15), Sala("201", 8)]
    st.session_state.reservas = []

# --- INTERFACE ---
st.title("📅 Sistema de Reuniões - Patrícia")

menu = st.tabs(["Nova Reserva", "Visualizar Grade", "Salas Livres"])

with menu[0]:
    st.subheader("Agendar Reunião")
    with st.form("form_reserva"):
        f_nome = st.text_input("Funcionário Responsável")
        assunto = st.text_input("Assunto da Reunião")
        col1, col2, col3 = st.columns(3)
        sala_nome = col1.selectbox("Sala", [s.nome for s in st.session_state.salas])
        data_res = col2.date_input("Data")
        hora_res = col3.time_input("Horário")
        
        if st.form_submit_button("Confirmar Agendamento"):
            # Lógica simples de verificação de conflito
            conflito = any(r.sala == sala_nome and r.data == data_res and r.hora == hora_res 
                           for r in st.session_state.reservas)
            
            if conflito:
                st.error("⚠️ Já existe uma reunião nesta sala e horário!")
            else:
                st.session_state.reservas.append(Reserva(sala_nome, f_nome, data_res, hora_res, assunto))
                st.success("Reserva realizada com sucesso!")

with menu[1]:
    st.subheader("Planilha de Ocupação")
    if st.session_state.reservas:
        for r in st.session_state.reservas:
            st.info(f"**{r.hora.strftime('%H:%M')}** | Sala {r.sala} | {r.funcionario} - {r.assunto} ({r.data})")
    else:
        st.write("Nenhuma reunião agendada.")

with menu[2]:
    st.subheader("Consultar Disponibilidade")
    st.caption("Filtro para os Diretores")
    data_cons = st.date_input("Data da Consulta")
    hora_cons = st.time_input("Faixa de Horário")
    
    # Atributo Derivado: Salas que NÃO possuem reserva no horário
    ocupadas = [r.sala for r in st.session_state.reservas if r.data == data_cons and r.hora == hora_cons]
    livres = [s for s in st.session_state.salas if s.nome not in ocupadas]
    
    if livres:
        for s in livres:
            st.success(f"✅ Sala {s.nome} disponível ({s.lugares} lugares)")
    else:
        st.error("❌ Nenhuma sala disponível neste horário.")
