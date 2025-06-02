import sqlite3
import pandas as pd
import streamlit as st
# from datetime import datetime, date, timedelta

# Conecta ou cria o banco de dados SQLite
conn = sqlite3.connect("capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/db/sistema_academia.db", check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela "clientes"
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes_academia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    sexo TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    plano_id INTEGER NOT NULL,
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')

# Criação da tabela "instrutores"
cursor.execute('''
CREATE TABLE IF NOT EXISTS instrutores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especialidade TEXT NOT NULL
)
''')

# Criação da tabela "planos"
cursor.execute('''
CREATE TABLE IF NOT EXISTS planos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco_mensal REAL NOT NULL,
    duracao_meses INTEGER NOT NULL
)
''')

# Criação da tabela "exercicios"
cursor.execute('''
CREATE TABLE IF NOT EXISTS exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    grupo_muscular TEXT NOT NULL
)
''')

# Criação da tabela "treinos"
cursor.execute('''
CREATE TABLE IF NOT EXISTS treinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    instrutor_id INTEGER NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    plano_id INTEGER NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes_academia(id),
    FOREIGN KEY(instrutor_id) REFERENCES instrutores(id),
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')

# Criação da tabela "treino_exercicio"
cursor.execute('''
CREATE TABLE IF NOT EXISTS treino_exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    treino_id INTEGER NOT NULL,
    exercicio_id INTEGER NOT NULL,
    series TEXT NOT NULL,
    repeticoes INTEGER NOT NULL,
    FOREIGN KEY(treino_id) REFERENCES treinos(id),
    FOREIGN KEY(exercicio_id) REFERENCES exercicios(id)
)
''')

# Criação da tabela "pagamentos"
cursor.execute('''
CREATE TABLE IF NOT EXISTS pagamento_clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    plano_id INTEGER NOT NULL,
    valor_pago REAL NOT NULL,
    data_pagamento TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes_academia(id),
    FOREIGN KEY(plano_id) REFERENCES planos(id)
)
''')
conn.commit()

# Popula o banco de dados SQLite

cursor.execute('PRAGMA foreign_keys = ON;')

cursor.execute("SELECT COUNT(*) FROM exercicios")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/exercicios.csv')
    df_exercicios.to_sql('exercicios', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM instrutores")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/instrutores.csv')
    df_exercicios.to_sql('instrutores', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM planos")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/planos.csv')
    df_exercicios.to_sql('planos', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM clientes_academia")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/clientes_academia.csv')
    df_exercicios.to_sql('clientes_academia', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM pagamento_clientes")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/pagamento_clientes.csv')
    df_exercicios.to_sql('pagamento_clientes', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM treinos")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/treinos.csv')
    df_exercicios.to_sql('treinos', conn, if_exists='append', index=False)

cursor.execute("SELECT COUNT(*) FROM treino_exercicios")
if cursor.fetchone()[0] == 0:
    df_exercicios = pd.read_csv('capacitacao_senai_python_daniella_torelli/30_05_to_04_06/project/csv/treino_exercicios.csv')
    df_exercicios.to_sql('treino_exercicios', conn, if_exists='append', index=False)

# 3. Criar uma aplicação Streamlit para:
# 	3.1. Listar clientes e seus planos;
# 	3.2. Filtrar e mostrar treinos e seus exercícios;
# 	* 3.3. Mostrar total de pagamentos e último pagamento por cliente;
# 	* 3.4. Mostrar quantos clientes cada instrutor atende;
# 	3.5. Formulário para cadastro de clientes, pagamentos, treinos e exercícios nos treinos;
# 	3.6. EXTRA: Usar a função de autenticação do streamlit para criar um login e senha.

# Exercício 3.3

st.subheader('Pagamentos por Clientes', divider=True)

df_nomes_clientes = pd.read_sql('''
	SELECT id, nome FROM clientes_academia
	''',
    conn
)

nomes_clientes_dict = {
    f"{row['nome']} (ID {row['id']})": row['id']
    for _, row in df_nomes_clientes.iterrows()
}

cliente_selecionado = st.selectbox(
    'Selecione um cliente:',
    options=list(nomes_clientes_dict.keys())
)

# Recupera o ID correspondente
cliente_selecionado_id = nomes_clientes_dict[cliente_selecionado]

# 5.1) Conta quantos pagamentos esse cliente já fez
cursor.execute(
    'SELECT COUNT(*) FROM pagamento_clientes WHERE cliente_id = ?',
    (cliente_selecionado_id,)
)
total_pagamentos = cursor.fetchone()[0]

# 5.2) Busca o último pagamento (valor e data), ordenando pela data
cursor.execute('''
    SELECT valor_pago, data_pagamento
    FROM pagamento_clientes
    WHERE cliente_id = ?
    ORDER BY data_pagamento DESC
    LIMIT 1
''', (cliente_selecionado_id,))
ultimo_pagamento = cursor.fetchone()

# 6) Exibe os resultados na tela
st.write(f'O cliente **{cliente_selecionado}** fez **{total_pagamentos}** pagamentos.')

if ultimo_pagamento:
    valor, data = ultimo_pagamento
    st.write(f'Seu último pagamento foi de **R$ {valor:.2f}**, em **{data}**.')
else:
    st.write('Ainda não há pagamentos registrados para este cliente.')

# Exercício 3.4

st.subheader('Quantidade de Clientes por Instrutor', divider=True)

df_nomes_instrutor = pd.read_sql_query('''
    SELECT id, nome FROM instrutores
    ''',
    conn
)

nomes_instrutor_dict = {
    f"{row['nome']} (ID {row['id']})": row['id']
    for _, row in df_nomes_instrutor.iterrows()
}

instrutor_selecionado = st.selectbox(
    'Selecione um instrutor:',
    options=list(nomes_instrutor_dict.keys())
)

instrutor_selecionado_id = nomes_instrutor_dict[instrutor_selecionado]

cursor.execute(
    '''
    SELECT COUNT(DISTINCT cliente_id)
    FROM treinos
    WHERE instrutor_id = ?
    ''',
    (instrutor_selecionado_id,)
)
total_alunos = cursor.fetchone()[0]

st.write(f'O instrutor **{instrutor_selecionado}** possui **{total_alunos}** alunos.')


# =============================
#       Exercício Extra
# =============================

import hashlib

# Criação da tabela "usario"
cursor.execute('''
	CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
	)
	''')
conn.commit()

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest() # Retorna o SHA da senha

# Popula tabela "usuario"
cursor.execute("SELECT COUNT(*) FROM usuarios")
if cursor.fetchone()[0] == 0:
    usuarios = [
        ("Alice Santos", "alice@email.com", "senha123"),
        ("Bruno Silva", "bruno@email.com", "segredo"),
        ("Carlos Lima", "carlos@email.com", "academia"),
        ("Diana Costa", "diana@email.com", "fitness"),
        ("Eduarda Reis", "eduarda@email.com", "malhacao")
    ]
    for nome, email, senha in usuarios:

        senha_hash = hash_senha(senha)

        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                        (nome, email, senha_hash))
    conn.commit()

