import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import date, datetime, timedelta

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/05_06/exercises/database/csv_vendas_acai.csv', sep=',', parse_dates=['data_venda'])

# print(df.info()) # os dados estão sem ruído

df_bkp = df.copy() # cria backup de DataFrame origem

df.to_csv('capacitacao_senai_python_daniella_torelli/05_06/exercises/database/csv_vendas_acai_limpo.csv', sep=',', index=False)

# Inicia streamlit
# Sidebar para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox(
    "Escolha a página:",
    ["Home", "Filtragens", "Análises Gráficas", "Tabelas"],
    index=0  # Página default (Home) ao abrir o app
)

# Exibição condicional conforme página selecionada
if pagina == "Home":
    st.title("Análise Geral")

    valor_total_sum = df['valor_total'].sum()  # Soma todos os valores da coluna valor_total
    qtd_vendas = df.shape[0]  # Retorna a quantidade de linhas ~= quantidade de vendas
    valor_medio = df['valor_total'].mean()  # Faz média dos valores da coluna valor_total
    qtd_clientes_unique = df['cliente'].nunique()  # Conta quantos clientes únicos há
    produto_mais_vendido = df['produto'].value_counts().idxmax()  # Produto mais vendido
    forma_pagamento_mais_usada = df['forma_pagamento'].value_counts().idxmax()  # Forma de pagamento mais usada

    # Exibe os indicadores em colunas
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col1.metric('Faturamento Total', f'R$ {valor_total_sum:,.2f}'.replace(",", "@").replace(".", ",").replace("@", "."))
    col2.metric('Quantidade de Vendas', qtd_vendas)
    col3.metric('Ticket Médio', f'R$ {valor_medio:,.2f}'.replace(",", "@").replace(".", ",").replace("@", "."))
    col3.caption('Valor médio de venda')
    col4.metric('Quantidade Total de Clientes', qtd_clientes_unique)
    col5.metric('Produto mais Vendido', produto_mais_vendido)
    col6.metric('Forma de Pagamento mais Usada', forma_pagamento_mais_usada)

elif pagina == "Filtragens":
    # 1º filtro: somatório de "valor_total" por "categoria"
    st.header('Somatória do Valor Total por Categoria')

    categorias = sorted(df['categoria'].unique())

    categorias_opt = st.selectbox('Selecione a Categoria:', categorias)

    df_categoria = df[df['categoria'] == categorias_opt]
    soma_valor_total_por_categoria = df_categoria['valor_total'].sum()

    st.write(f"A soma do valor total para a categoria **{categorias_opt}** é: R$ {soma_valor_total_por_categoria:,.2f}".replace(",", "@").replace(".", ",").replace("@", "."))

    # 2º filtro: média do "valor_total" agrupada por "forma_pagamento"
    st.header('Valor Médio de Venda por Método de Pagamento')

    formas_pagamento = sorted(df['forma_pagamento'].unique())

    forma_pagamento_opt = st.selectbox('Selecione a forma de pagamento:', formas_pagamento)

    media_valor_total = df[df['forma_pagamento'] == forma_pagamento_opt]['valor_total'].mean()

    st.markdown(f'O valor médio de venda feito com **{forma_pagamento_opt}** foi: **R$ {media_valor_total:,.2f}**'.replace(",", "@").replace(".", ",").replace("@", "."))

    # 3º filtro: top 3 clientes
    st.header('Top 3 Clientes')

    valor_total_por_cliente = df.groupby('cliente')['valor_total'].sum().sort_values(ascending=False)

    top3_clientes = valor_total_por_cliente.head(3)

    nomes = top3_clientes.index.tolist()
    valores = top3_clientes.values.tolist()

    mensagem = ' | '.join([f'{nome}: R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') for nome, valor in zip(nomes, valores)])

    st.text(f'Os top 3 clientes são: {mensagem}')

elif pagina == "Análises Gráficas":
    # 1º gráfico
    st.subheader('Quantidade de produtos mais vendidos')

    top5_produtos = df['produto'].value_counts().head(5)

    fig1, ax1 = plt.subplots()
    top5_produtos.sort_values().plot.barh(ax=ax1)
    ax1.set_xlabel('Quantidade vendida')
    ax1.set_ylabel('Produtos')
    st.pyplot(fig1)

    # 2º gráfico
    st.subheader('Quantidade de Vendas por Categoria(s)')

    categorias = sorted(df['categoria'].unique())

    categorias_multiselect = st.multiselect('Selecione a(s) categoria(s) para exibir no gráfico:', categorias, default=categorias)

    df_filtro_vendas_por_categoria = df[df['categoria'].isin(categorias_multiselect)]

    vendas_por_categoria_sum = df_filtro_vendas_por_categoria.groupby('categoria')['valor_total'].sum().sort_values()

    fig2, ax2 = plt.subplots()
    vendas_por_categoria_sum.plot.barh(ax=ax2)
    ax2.set_xlabel('Total de Vendas')
    ax2.set_ylabel('Categoria(s)')
    st.pyplot(fig2)

    # 3º gráfico
    st.subheader('Quantidade de Vendas por Produto(s)')


    produtos = sorted(df['produto'].unique())

    produtos_multiselect = st.multiselect('Selecione o(s) produto(s) para exibir no gráfico:', produtos, default=produtos)

    df_filtro_vendas_por_produto = df[df['produto'].isin(produtos_multiselect)]

    vendas_por_produto_sum = df_filtro_vendas_por_produto.groupby('produto')['valor_total'].sum().sort_values()

    fig3, ax3 = plt.subplots()
    vendas_por_produto_sum.plot.barh(ax=ax3)
    ax3.set_xlabel('Total de vendas')
    ax3.set_ylabel('Produtos')
    st.pyplot(fig3)

    # 4º gráfico
    st.subheader('Quantidade de Vendas por Horário')

    df['hora'] = df['data_venda'].dt.hour

    vendas_por_hora = df['hora'].value_counts().sort_index()

    fig4, ax4 = plt.subplots()
    vendas_por_hora.plot(ax=ax4, marker='o')
    ax4.set_xlabel("Hora do dia")
    ax4.set_ylabel("Quantidade de vendas")
    st.pyplot(fig4)

    # 5º gráfico
    st.subheader('Quantidade de Vendas por Dias da Semana')

    df['dia_semana'] = df['data_venda'].dt.day_name()

    dias_pt = {
        'Monday': 'Segunda',
        'Tuesday': 'Terça',
        'Wednesday': 'Quarta',
        'Thursday': 'Quinta',
        'Friday': 'Sexta',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }

    df['dia_semana'] = df['dia_semana'].map(dias_pt)

    dias_ordem = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

    df['dia_semana'] = pd.Categorical(df['dia_semana'], categories=dias_ordem, ordered=True)

    vendas_por_dia_semana = df['dia_semana'].value_counts().reindex(dias_ordem)

    fig5, ax5 = plt.subplots()
    vendas_por_dia_semana.plot(ax=ax5, marker='o')
    ax5.set_xlabel('Dias da semana')
    ax5.set_ylabel("Quantidade de vendas")
    plt.xticks(rotation=45)
    st.pyplot(fig5)

elif pagina == "Tabelas":
    # 1ª tabela: filtra por período
    st.header('Tabela por período')

    data_min = df['data_venda'].min()
    data_max = df['data_venda'].max()

    data_inicio, data_fim = st.date_input(
        "Selecione o período de venda:",
        value=(data_min, data_max),
        min_value=data_min,
        max_value=data_max,
        help='Selecione uma data inicial e uma final para filtrar as vendas dentro desse intervalo.'
    )

    df_filtro_data_venda = df[
        (df['data_venda'].dt.date >= data_inicio) &
        (df['data_venda'].dt.date <= data_fim)
    ]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_data_venda)

    # 2ª tabela: filtra por forma(s) de pagamento
    st.header('Tabela por formas de pagamentos')

    forma_pagamento_opt = st.selectbox(
        'Selecione a forma de pagamento:',
        sorted(df['forma_pagamento'].unique())
    )

    df_filtro_forma_pagamento = df[df['forma_pagamento'] == forma_pagamento_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_forma_pagamento)

    # 3ª tabela: filtra por cliente
    st.header('Tabela por clientes')

    clientes = sorted(df['cliente'].unique())

    clientes_opt = st.selectbox(
        'Selecione (ou digite o nome) do cliente:',
        clientes
    )

    df_filtro_cliente = df[df['cliente'] == clientes_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_cliente)

