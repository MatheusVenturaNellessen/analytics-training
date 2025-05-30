# 1. Crie um banco SQLite com as seguintes 4 tabelas: autores,
# categorias, livros, empréstimos;
# 2. Insira dados fictícios em cada tabela (pelo menos 10 livros);
# 3. No Streamlit, mostre:
# 	3.1 Todos os livros com nome do autor e da categoria.
# 	3.2 Filtro de livros por ano de publicação.
# 	3.3 Quantidade total de livros, de empréstimos e devolvidos.
# 	3.4 Número de livros por categoria (agrupado).
# 	3.5 Formulário para registrar novo empréstimo ou novo livro.
# 	3.6 Formulário para editar um pedido (alterar a quantidade de itens)
# 	3.7 Formulário para editar um Produto (alterar preço, nome,
# quantidade disponível)
# 	3.8 Formulário para Deletar um livro ou autor.

import sqlite3
from datetime import datetime, date, timedelta
import pandas as pd
import streamlit as st

conn = sqlite3.connect('capacitacao_senai_python_daniella_torelli/29_05/exercises/db/biblioteca.db')
cursor = conn.cursor()

# Exercício 1

cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
	autor_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    quantidade_disponivel INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS emprestimos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
	data_emprestimo TEXT NOT NULL,
	devolvido INTEGER NOT NULL
)
''')

conn.commit()

# Exercício 2

cursor.execute("SELECT COUNT(*) FROM autores")
if cursor.fetchone()[0] == 0:
	autores = [
		("George Orwell",),
		("Isaac Asimov",),
		("J.R.R. Tolkien",),
		("J.K. Rowling",),
		("Jane Austen",),
		("Fyodor Dostoevsky",),
		("Mark Twain",),
		("Gabriel García Márquez",),
		("Arthur C. Clarke",),
		("Yuval Noah Harari",),
	]
	cursor.executemany("INSERT INTO autores (nome) VALUES (?)", autores)

cursor.execute("SELECT COUNT(*) FROM categorias")
if cursor.fetchone()[0] == 0:
	categorias = [
		("Ficção Científica",),
		("Fantasia",),
		("Romance",),
		("Suspense",),
		("Clássicos",),
		("Não Ficção",),
		("História",),
	]
	cursor.executemany("INSERT INTO categorias (nome) VALUES (?)", categorias)

cursor.execute("SELECT COUNT(*) FROM livros")
if cursor.fetchone()[0] == 0:
	livros = [
		("1984", 1, 1, 1949,  4),
		("Fundação", 2, 1, 1951,  2),
		("O Hobbit", 3, 2, 1937,  5),
		("Harry Potter e a Pedra Filosofal", 4, 2, 1997, 3),
		("Orgulho e Preconceito", 5, 3, 1813,  1),
		("Crime e Castigo", 6, 5, 1866,  2),
		("As Aventuras de Tom Sawyer", 7, 5, 1876,  3),
		("Cem Anos de Solidão", 8, 5, 1967,  2),
		("2001: Uma Odisseia no Espaço", 9, 1, 1968,  3),
		("Sapiens", 10, 7, 2011,  4)
	]

	cursor.executemany("INSERT INTO livros (titulo, autor_id, categoria_id, ano, quantidade_disponivel) VALUES (?, ?, ?, ?, ?)", livros)

cursor.execute("SELECT COUNT(*) FROM emprestimos")
if cursor.fetchone()[0] == 0:
	emprestimos = [
		(1,  "2025-05-10 10:00:00", 1),
		(3,  "2025-05-20 15:30:00", 0),
		(5,  "2025-05-25 14:00:00", 0),
		(10, "2025-04-30 09:15:00", 1),
		(2,  "2025-05-01 11:00:00", 1)
	]
	cursor.executemany("INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES (?, ?, ?)", emprestimos)

	conn.commit()

st.title('Sistema bibliotecário v1.0.0')

st.header('Tabela dos livros filtrados por nome de autor e categoria do livro', divider=True)

# Exercício 3.1: Mostre todos os livros com nome do autor e da categoria

df_filtro_31 = pd.read_sql_query('''
	SELECT l.titulo as titulo_livro, a.nome as autor_nome, c.nome as categoria_nome
	FROM livros l
	JOIN autores a ON l.autor_id = a.id
	JOIN categorias c ON l.categoria_id = c.id
	ORDER BY l.titulo ASC
''', conn)

st.dataframe(df_filtro_31)

# Exercício 3.2: Mostre um filtro de livros por ano de publicação.

st.header('Tabela dos livros filtrados por ano de publicação', divider=True)

df_livros = pd.read_sql_query('SELECT * FROM livros', conn)

livro_ano = st.selectbox('Selecione um ano:', df_livros['ano'])

df_filtro_32 = pd.read_sql_query('SELECT * FROM livros WHERE ano = ?', conn, params=(livro_ano,))

st.dataframe(df_filtro_32)

# Exercício 3.3: Mostre a quantidade total de livros, de empréstimos e devolvidos.

st.header('Tabela da quantidade de livros, empréstimos e livros devolvidos', divider=True)

df_filtro_33 = pd.read_sql_query('''
	SELECT
        (SELECT COUNT(*) FROM livros) AS total_livros,
        (SELECT COUNT(*) FROM emprestimos) AS total_emprestimos,
		(SELECT COUNT(*) FROM emprestimos WHERE devolvido = 1) AS total_devolvidos;
''', conn)

st.dataframe(df_filtro_33)

# Exercício 3.4: Mostre o número de livros por categoria

st.header('Tabela da quantidade de livros por categoria', divider=True)

df_filtro_34 = pd.read_sql_query('''
    SELECT
        c.nome AS categoria_livro,
        COUNT(*) AS total_livros_por_categoria
    FROM livros l
    JOIN categorias c
    	ON l.categoria_id = c.id
    GROUP BY c.nome
    ORDER BY total_livros_por_categoria DESC
''', conn)

st.dataframe(df_filtro_34)

# Exercício 3.5: Crie um formulário para registrar novo empréstimo ou novo livro.

st.subheader("Formulário para inserir novo livro")

with st.form("form_inserir"):
    titulo = st.text_input("Título do livro:").strip()

    # 1) Input do tipo TEXT p/ buscar autor
    busca_autor = st.text_input("Digite nome do autor:").strip()

    # 2) Busca dinâmica no banco de dados
    df_autores = pd.read_sql_query(
        """
        SELECT id, nome
        FROM autores
        WHERE nome LIKE ? COLLATE NOCASE
        ORDER BY nome
        """,
        conn,
        params=(f"%{busca_autor}%",),  # % antes e depois para filtrar em qualquer parte do TEXT
    )

    opcoes = df_autores["nome"].tolist()

    # 3) Se não existir exatamente igual, adiciona opção de criar novo autor
    if busca_autor and busca_autor not in opcoes:
        opcoes.append(f"Criar novo autor: '{busca_autor}'")

    # 4) Dropdown (selectbox) dos autores existentes sempre visível
    autor_escolhido = st.selectbox(
        "Selecione um autor existente (se autor não estiver presente, selecionar o primeiro):",
        options=opcoes,
    )

    # Demais variáveis / chaves
    categorias = pd.read_sql_query(
        "SELECT id, nome FROM categorias ORDER BY nome",
        conn
    )
    categoria = st.selectbox(
        "Categoria:",
        options=categorias["id"].tolist(),
        format_func=lambda x: categorias.loc[categorias["id"] == x, "nome"].iloc[0],
    ) # Estudar mais a fundo esse código

    data_min = date(1900, 1, 1)
    data_max = date.today()
    data_default = date.today() - timedelta(days=365)

    data_pub = st.date_input(
        "Data da publicação do livro:",
        value=data_default,		# Data inicial selecionada
        min_value=data_min,		# Menor data permitida
        max_value=data_max		# Maior data permitida
        # help="Escolha uma data entre 01/01/1900 e hoje"
    )

    qtd = st.number_input(
        "Quantidade disponível:",
        min_value=1,
        step=1,
        value=1
    )

    enviar = st.form_submit_button("Inserir novo livro")

if enviar:
    # 1) Validação básica
    if not (titulo and busca_autor and qtd > 0):
        st.error("Preencha os campos corretamente.")
    else:
        # 2) Lista de autores existentes
        lista_nomes = df_autores["nome"].tolist()

        # 3) Definição clara da opção "novo autor"
        nova_opcao = (f"Criar novo autor: '{busca_autor}'")

        # 4) Upsert de autor
        if autor_escolhido in lista_nomes: # Autor já existe
            autor_id = int(df_autores.loc[df_autores["nome"] == autor_escolhido, "id"].iloc[0]) # Estudar mais a fundo esse código
        else: # Autor não está na lista → Criamos
            cursor.execute(
                "INSERT INTO autores (nome) VALUES (?)",
                (busca_autor,),
            )

            conn.commit()

            autor_id = cursor.lastrowid # Estudar mais a fundo esse código

        # 5) Inserção do livro
        cursor.execute(
            """
            INSERT INTO livros
              (titulo, autor_id, categoria_id, ano, quantidade_disponivel)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                titulo,
                autor_id,
                categoria,
                data_pub.isoformat(), # YYYY-MM-DD
                qtd,
            ),
        )

        conn.commit()

        st.success("Livro inserido com sucesso!")


