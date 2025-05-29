import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime

# Conecta ao banco de dados
conn = sqlite3.connect("capacitacao_senai_python_daniella_torelli/29_05/exercises/db/produtos.db", check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela produtos (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
)
''')

# Criação da tabela vendas (DDL)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    data_venda TEXT NOT NULL,
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')

conn.commit()

# Inserção inicial de produtos (DML)
cursor.execute("SELECT COUNT(*) FROM produtos")
if cursor.fetchone()[0] == 0:
    produtos_iniciais = [
        ('Sorvete de Chocolate', 7.5, 'Sobremesa'),
        ('Picolé de Morango', 4.0, 'Sobremesa'),
        ('Água Mineral', 2.0, 'Bebida'),
        ('Refrigerante', 6.0, 'Bebida'),
        ('Café Gelado', 5.0, 'Bebida'),
    ]
    cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", produtos_iniciais)

    conn.commit()

# Título principal (Streamlit)
st.title("Fundamentos de SQL com Python + Streamlit")

# SELECT * FROM produtos
st.subheader("📋 Tabela: SELECT * FROM produtos")

df = pd.read_sql_query("SELECT * FROM produtos", conn)

st.dataframe(df) # Exibe tabela (sem nenhum filtro)

# Filtro: WHERE preco > range
st.subheader("Filtro: WHERE preco > Range")

range = st.slider("Range:", 0.0, 10.0, 5.0, 0.5)

df_filtro = pd.read_sql_query("SELECT * FROM produtos WHERE preco > ?", conn, params=(range,))

st.dataframe(df_filtro) # Exibe tabela filtrada por preço com range

# SELECT {nome, preco}
st.subheader("SELECT {nome, preco}")

df_select = pd.read_sql_query("SELECT nome, preco FROM produtos", conn)

st.dataframe(df_select) # Exibe tabela filtrada por registros de "name" e "preco"

# Funções agregadas (AVG, SUM, COUNT)
st.subheader("Funções agregadas (AVG, SUM, COUNT)")

df_agregado = pd.read_sql_query('''
    SELECT
        ROUND(AVG(preco), 2) AS media,
        ROUND(SUM(preco), 2) AS soma,
        COUNT(*) AS total
    FROM produtos
''', conn)

st.dataframe(df_agregado) # Exibe tabela filtrada por funções agregadas (média, soma e contabilizador)

# GROUP BY categoria
st.subheader("GROUP BY categoria")

df_group = pd.read_sql_query('''
    SELECT categoria,
		COUNT(*) AS total_produtos,
		ROUND(AVG(preco), 2) AS media_preco
    FROM produtos
    GROUP BY categoria
''', conn)

st.dataframe(df_group) # Exibe tabela filtrada por agrupamento, contabilizada e aplicando média por grupamento

# Inserir novo produto
st.subheader("Inserir novo produto")

with st.form("form_inserir"):
    nome = st.text_input("Nome do produto:")
    preco = st.number_input("Preço:", min_value=0.0, step=0.5)
    categoria = st.selectbox("Categoria:", ['Sobremesa', 'Bebida', 'Outros'])
    enviar = st.form_submit_button("Inserir")

    if enviar and nome and preco > 0:
        cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", (nome, preco, categoria))

        conn.commit() # Salva alterações (inserção de novo produto)

        st.success(f"Produto '{nome}' inserido com sucesso!")

        st.rerun() # Atualiza banco da dados

# Registro de venda
st.subheader("Registrar nova venda")

produtos = pd.read_sql_query("SELECT id, nome FROM produtos", conn) #  Executa uma consulta SQL no banco de dados, buscando os registros id e nome, e armazena o resultado em um DataFrame.

produto_nome = st.selectbox("Produto:", produtos["nome"]) # Cria um menu suspenso no Streamlit com as opções vindas do registro nome. O valor selecionado pelo usuário é salvo.

quantidade = st.number_input("Quantidade:", min_value=1, step=1) # Exibe um campo numérico. O número escolhido é salvo.

registrar = st.button("Registrar venda") # Adiciona um botão que será True apenas no instante em que o usuário clicar nele.

if registrar:
    produto_id = int(produtos[produtos["nome"] == produto_nome]["id"].values[0]) # Filtra o DataFrame "produtos" para encontrar a linha que o nome bata com "produto_nome", extrai o "id" correspondente e converte em inteiro.

    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Captura data e hora atuais e formata como string no formato YYYY-MM-DD HH:MM:SS, para armazenar no banco de dados.

    cursor.execute("INSERT INTO vendas (produto_id, quantidade, data_venda) VALUES (?, ?, ?)", (produto_id, quantidade, data_venda)) # Executa o comando SQL de inserção.

    conn.commit() # salva as alterações, gravando permanentemente a nova venda no arquivo do banco SQLite.

    st.success(f"Venda registrada: {quantidade} und. x {produto_nome}") # Exibe uma mensagem de sucesso (feedback), confirmando quantas unidades do produto foram vendidas.

    st.rerun() # Força o Streamlit a recarregar o script desde o início, para que a tabela de histórico (abaixo) seja atualizada imediatamente.

# Tabela de vendas com JOIN
st.subheader("📈 Histórico de vendas")

df_vendas = pd.read_sql_query('''
    SELECT v.id, p.nome AS produto, v.quantidade, v.data_venda
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    ORDER BY v.data_venda DESC
''', conn) #  Executa uma query que faz um JOIN entre "vendas" (apelidada "v") e "produtos" (apelidada "p"), selecionando o ID da venda, o nome do produto, a quantidade e a data, e ordena da mais recente para a mais antiga. Resultado vai para o DataFrame "df_vendas".

st.dataframe(df_vendas) # Renderiza o DataFrame "df_vendas" como uma tabela interativa no Streamlit

conn.close() # Encerra a conexão SQLite, liberando recursos.
