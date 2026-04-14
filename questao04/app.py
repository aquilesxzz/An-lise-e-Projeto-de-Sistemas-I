import streamlit as st
from datetime import datetime, timedelta

st.title("💊 Controle de Horário de Remédios")

# Entrada de dados
nome_usuario = st.text_input("Nome do paciente:")
nome_remedio = st.text_input("Nome do remédio:")
dosagem = st.text_input("Dosagem (ex: 500mg):")
data_inicio = st.date_input("Data de início:")
dias = st.number_input("Quantidade de dias:", min_value=1)
vezes_dia = st.number_input("Vezes ao dia:", min_value=1)

# Gerar horários
if st.button("Gerar horários"):
    intervalo = 24 // vezes_dia
    horarios = []

    for i in range(vezes_dia):
        hora = (8 + i * intervalo) % 24  # começa às 08h
        horarios.append(f"{hora:02d}:00")

    st.subheader("⏰ Horários sugeridos:")
    for h in horarios:
        st.write(h)

    data_fim = data_inicio + timedelta(days=dias)

    st.success(f"Tratamento até: {data_fim.strftime('%d/%m/%Y')}")

    # Simulação de planilha
    st.subheader("📅 Planilha do dia:")
    for h in horarios:
        status = st.checkbox(f"{h} - Tomado?")
        
        if not status:
            st.warning(f"Atraso detectado no horário {h}!")
