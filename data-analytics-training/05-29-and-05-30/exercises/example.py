import sqlite3 # Importa SQL nativo do Python
import pandas as pd # Utiliza o SQLite
import streamlit as st # Exibe em aplicação web

conn = sqlite3.connect("capacitacao_senai_python_daniella_torelli/29_05/exercises/db/produtos.db") # Conecta ou cria um banco de dados SQLite
cursor = conn.cursor() # Cria um cursos (?)

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
)
''') # Cria o banco de dados se não existir (DDL)

conn.commit() # Ele salva as alterações do banco de dados

cursor.execute("SELECT COUNT(*) FROM produtos")
if cursor.fetchone()[0] == 0: # Verifica se banco de dados já existe
    produtos_iniciais = [
        ('Sorvete de Chocolate', 7.5, 'Sobremesa'),
        ('Picolé de Morango', 4.0, 'Sobremesa'),
        ('Água Mineral', 2.0, 'Bebida'),
        ('Refrigerante', 6.0, 'Bebida'),
        ('Café Gelado', 5.0, 'Bebida'),
    ]
    cursor.executemany("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", produtos_iniciais) # Executa uma instrução SQL mais de uma vez (quando tem mais de um parâmetro) | Insere produtos ao banco de dados / tabela

    conn.commit() # .: Insere os dados no banco de dados

# Apresentar no Streamlit

st.title("Fundamentos de SQL com Python + Streamlit")

st.subheader("Tabela: SELECT * FROM produtos")

df = pd.read_sql_query("SELECT * FROM produtos", conn) # Seleciona todos os registros do banco de dados
st.dataframe(df) # Mostra o banco de dados / DataFrame

st.subheader("Filtro: WHERE preco > ?")

valor_min = st.slider("Preço mínimo", 0.0, 10.0, 5.0, 0.5) # Cria um Range para selecionar o preço mínimo

df_filtro = pd.read_sql_query("SELECT * FROM produtos WHERE preco > ?", conn, params=(valor_min,)) # Seleciona todos os registros onde o preço é maior que o Range
st.dataframe(df_filtro) # Mostra o banco de dados filtrado com precos acima do Range

st.subheader('SELECT das colunas "nome" e "preco"')

df_select = pd.read_sql_query("SELECT nome, preco FROM produtos", conn) # Seleciona os registros nome e preço do banco de dados

st.dataframe(df_select) # Mostra o banco de dados filtrado pro registro nome e preço

st.subheader("Funções agregadas")

df_agregado = pd.read_sql_query('''
    SELECT
        ROUND(AVG(preco), 2) AS media,
        ROUND(SUM(preco), 2) AS soma,
        COUNT(*) AS total
    FROM produtos
''', conn) # Seleciona o registro preco do banco de dados e aplica as funções agregadas AVG como media, SUM como soma e COUNT como total

st.dataframe(df_agregado) # Mostra banco de dados filtrado

st.subheader("GROUP BY categoria")

df_group = pd.read_sql_query('''
    SELECT categoria,
		COUNT(*) AS total_produtos,
		ROUND(AVG(preco), 2) AS media_preco
	FROM produtos
	GROUP BY categoria
''', conn) # Agrupa por categoria, contabiliza como total_produtos e realiza média como media_preco por grupo

st.dataframe(df_group) # Mostra grupo do banco de dados

# Como inserir novos produtos no banco de dados

st.subheader("Inserir novo produto")

with st.form("form_inserir"): #
    nome = st.text_input("Nome do produto:") # Um input do tipo string para inserir nome do novo produto
    preco = st.number_input("Preço:", min_value=0.0, step=0.5) # Um input do tipo number para inserir preço do novo produto
    categoria = st.selectbox("Categoria:", ['Sobremesa', 'Bebida', 'Outros']) # Um select para selecionar a categoria do novo produto
    enviar = st.form_submit_button("Inserir") # Botão de submit

    if enviar and nome and preco > 0: # Validação
        cursor.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)",(nome, preco, categoria)) # Insere novo produto ao banco de dados / tabela já existente

        conn.commit() # Salva alteração

        st.success(f"Produto '{nome}' inserido com sucesso!") # Mensagem de feedback

        st.rerun() # Recarrega página automaticamente

conn.close() # Fechando conexão
