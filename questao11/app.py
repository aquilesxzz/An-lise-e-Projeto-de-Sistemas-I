import streamlit as st
from datetime import date

# SUPERCLASSE
class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def obter_idade(self):
        hoje = date.today()
        return hoje.year - self.nascimento.year

# SUBCLASSE FUNCIONARIO
class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, salario):
        super().__init__(nome, nascimento)
        self.salario = salario

    def reajustar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

# SUBCLASSE CLIENTE
class Cliente(Pessoa):
    def __init__(self, nome, nascimento, profissao):
        super().__init__(nome, nascimento)
        self.profissao = profissao

# INTERFACE
st.title("Sistema de Pessoas")

tipo = st.selectbox("Tipo:", ["Funcionario", "Cliente"])

nome = st.text_input("Nome:")
nascimento = st.date_input("Data de nascimento:")

if tipo == "Funcionario":
    salario = st.number_input("Salário:")

    if st.button("Cadastrar Funcionário"):
        f = Funcionario(nome, nascimento, salario)
        st.success(f"Funcionário cadastrado! Idade: {f.obter_idade()}")

elif tipo == "Cliente":
    profissao = st.text_input("Profissão:")

    if st.button("Cadastrar Cliente"):
        c = Cliente(nome, nascimento, profissao)
        st.success(f"Cliente cadastrado! Idade: {c.obter_idade()}")
