import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import date, datetime, timedelta
import numpy as np

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/05_06/exercises/database/csv_vendas_acai.csv', sep=',', parse_dates=['data_venda'])

# print(df.info()) # os dados estão sem ruído

df_bkp = df.copy() # cria backup de DataFrame origem

df.to_csv('capacitacao_senai_python_daniella_torelli/05_06/exercises/database/csv_vendas_acai_limpo.csv', sep=',', index=False)

# Inicia streamlit
# Sidebar para navegação
st.sidebar.title("Bem vindo(a)!")
pagina = st.sidebar.selectbox(
    "Navegue entre as páginas:",
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
    col4.metric('Quantidade Total de Clientes (únicos)', qtd_clientes_unique)
    col5.metric('Produto mais Vendido', produto_mais_vendido)
    col6.metric('Forma de Pagamento mais Usada', forma_pagamento_mais_usada)

    # Exibe big-number de diferença entre último mês e - 1
    df['mes'] = df['data_venda'].dt.month

    meses_ordenados = sorted(df['mes'].unique()) # ordena os meses únicos

    df_meses_ordenados = pd.DataFrame({'mes': meses_ordenados}) # cria um DataFrame dos meses ordenados, com coluna intitulada "mes"

    df_ultimos_meses = df_meses_ordenados.tail(2) # pega os últimos 2 meses

    df_ultimos_meses = df_ultimos_meses.reset_index(drop=True) # fundamental para funcionar o iloc

    # Calcula o valor total de vendas do penúltimo mês (mes_menos1)
    mes_menos1 = df_ultimos_meses.iloc[0]['mes']
    df_mes_menos1 = df[df['mes'] == mes_menos1]
    valor_total_mes_menos1 = df_mes_menos1['valor_total'].sum()

    # Calcula o valor total de vendas do últimos mes (mes_atual)
    mes_atual = df_ultimos_meses.iloc[1]['mes']
    df_mes_atual = df[df['mes'] == mes_atual]
    valor_total_mes_atual = df_mes_atual['valor_total'].sum()

    diferenca_vendas_entre_mes_atual_e_menos1 = valor_total_mes_atual - valor_total_mes_menos1

    diferenca_porcem_entre_mes_atual_e_menos1 = (valor_total_mes_atual - valor_total_mes_menos1) / valor_total_mes_menos1 * 100

    col7, = st.columns(1)
    col7.metric(
        label=f'Diferença de Vendas: Mês {mes_atual} (mês atual) vs. {mes_menos1} (últimos mês)',
        value=f"R$ {diferenca_vendas_entre_mes_atual_e_menos1:,.2f}".replace(",", "@").replace(".", ",").replace("@", "."),
        delta=f"{diferenca_porcem_entre_mes_atual_e_menos1:.2f}%"
    )

    # Exibe evolução do(s) produto(s)
    with st.expander('Clique aqui para visualizar a evolução de venda do(s) produto(s).'):
        produtos = sorted(df['produto'].unique().tolist())
        produto_selected = st.selectbox('Selecione o produto:', produtos)

        df_produto_selected = df[df['produto'] == produto_selected]

        df_produto_selected['ano_mes'] = df_produto_selected['data_venda'].dt.to_period('M')

        vendas_por_produto_selected = df_produto_selected.groupby('ano_mes').size()

        fig10, ax10 = plt.subplots()
        vendas_por_produto_selected.plot(ax=ax10, marker='o')
        ax10.set_title(f'Evolução das vendas de "{produto_selected}"')
        ax10.set_xlabel('Data da venda (em dias)')
        ax10.set_ylabel('Quantidade de vendas')
        st.pyplot(fig10)

elif pagina == "Filtragens":
    # 1º filtro: somatório de "valor_total" por "categoria"
    st.header('Somatória: Valor Total por Categoria')

    categorias = sorted(df['categoria'].unique())

    categorias_opt = st.selectbox('Selecione a Categoria:', categorias)

    df_categoria = df[df['categoria'] == categorias_opt]
    soma_valor_total_por_categoria = df_categoria['valor_total'].sum()

    st.write(f"A soma do valor total para a categoria **{categorias_opt}** é: R$ {soma_valor_total_por_categoria:,.2f}".replace(",", "@").replace(".", ",").replace("@", "."))

    # 2º filtro: média do "valor_total" agrupada por "forma_pagamento"
    st.header('Valor de Venda Médio por Método de Pagamento')

    formas_pagamento = sorted(df['forma_pagamento'].unique())

    forma_pagamento_opt = st.selectbox('Selecione a forma de pagamento:', formas_pagamento)

    media_valor_total = df[df['forma_pagamento'] == forma_pagamento_opt]['valor_total'].mean()

    st.markdown(f'O valor médio de venda feito com **{forma_pagamento_opt}** foi: **R$ {media_valor_total:,.2f}**'.replace(",", "@").replace(".", ",").replace("@", "."))

    # 3º filtro: top 3 clientes
    st.header('Os 3 Maiores Clientes')

    valor_total_por_cliente = df.groupby('cliente')['valor_total'].sum().sort_values(ascending=False)

    top3_clientes = valor_total_por_cliente.head(3)

    nomes = top3_clientes.index.tolist()
    valores = top3_clientes.values.tolist()

    mensagem = ' | '.join([f'{nome}: R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') for nome, valor in zip(nomes, valores)])

    st.text(f'Os top 3 clientes são: {mensagem}')

elif pagina == "Análises Gráficas":
    # 1º gráfico
    st.header('Produtos mais Vendidos')

    top5_produtos = df['produto'].value_counts().head(5)

    fig1, ax1 = plt.subplots()
    top5_produtos.sort_values().plot.barh(ax=ax1)
    ax1.set_xlabel('Quantidade vendida')
    ax1.set_ylabel('Produtos')
    st.pyplot(fig1)

    # 2º gráfico
    st.header('Vendas por Categorias')

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
    st.header('Vendas por Produtos')


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
    st.header('Vendas por Horário')

    df['hora'] = df['data_venda'].dt.hour

    vendas_por_hora = df['hora'].value_counts().sort_index()

    fig4, ax4 = plt.subplots()
    vendas_por_hora.plot(ax=ax4, marker='o')
    ax4.set_xlabel("Hora do dia")
    ax4.set_ylabel("Quantidade de vendas")
    st.pyplot(fig4)

    # 5º gráfico
    st.header('Vendas por Dias da Semana')

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

    # 6º gráfico
    st.header('Distribuição: Formas de Pagamento')

    qtd_formas_pagamento = df['forma_pagamento'].value_counts()

    fig6, ax6 = plt.subplots()
    ax6.pie(qtd_formas_pagamento, labels=qtd_formas_pagamento.index, autopct='%1.2f%%', startangle=90)
    ax6.set_title('Distribuição das Formas de Pagamento (%)')
    st.pyplot(fig6)

    # 7º gráfico
    st.header('Somatório: Vendas por Formas de Pagamento')

    def func_abs(values):
        def my_autopct(pct):
            total = np.sum(values)
            val = int(round(pct * total / 100.0))
            return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return my_autopct

    group_formas_pagamento_by_valor_total = df.groupby('forma_pagamento')['valor_total'].sum()

    fig8, ax8 = plt.subplots()
    ax8.pie(
        group_formas_pagamento_by_valor_total,
        labels=group_formas_pagamento_by_valor_total.index,
        autopct=func_abs(group_formas_pagamento_by_valor_total.values),
        startangle=90
    )
    ax8.set_title('Somatório de Vendas por Formas de Pagamento')
    st.pyplot(fig8)

    # 8º gráfico
    st.header('Comparação de Vendas por Mês')

    df['mes'] = df['data_venda'].dt.month

    qtd_vendas_por_mes = df['mes'].value_counts().sort_index()

    fig9, ax9 = plt.subplots()
    qtd_vendas_por_mes.plot(ax=ax9, marker='o')
    ax9.set_xlabel('Mês')
    ax9.set_ylabel('Quantidade de vendas')
    st.pyplot(fig9)

elif pagina == "Tabelas":
    # 1ª tabela: filtra por período
    st.header('Filtro por Períodos')

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
    st.header('Filtro por Formas de Pagamentos')

    forma_pagamento_opt = st.selectbox(
        'Selecione a forma de pagamento:',
        sorted(df['forma_pagamento'].unique())
    )

    df_filtro_forma_pagamento = df[df['forma_pagamento'] == forma_pagamento_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_forma_pagamento)

    # 3ª tabela: filtra por cliente
    st.header('Filtro por Clientes')

    clientes = sorted(df['cliente'].unique())

    clientes_opt = st.selectbox(
        'Selecione (ou digite o nome) do cliente:',
        clientes
    )

    df_filtro_cliente = df[df['cliente'] == clientes_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_cliente)

    # 4ª tabela: filtros interativos
    st.header('Filtros por Formas de Pagamento, Categorias, Cliente e Mês')

    df['mes'] = df['data_venda'].dt.month

    # Filtro por categoria
    categorias_list = sorted(df['categoria'].unique().tolist())
    categorias_selected = st.multiselect(
        "Selecione a(s) categoria(s):",
        options=categorias_list,
        default=categorias_list
    )

    # Filtro por mês
    mes_list = sorted(df['mes'].unique().tolist())
    mes_selected = st.multiselect(
        'Selecione o mês:',
        options=mes_list,
        default=mes_list
    )

    # Filtro por forma de pagamento
    formas_pagamento_list = sorted(df['forma_pagamento'].unique().tolist())
    formas_pagamento_selected = st.multiselect(
        "Selecione a(s) forma(s) de pagamento:",
        options=formas_pagamento_list,
        default=formas_pagamento_list
    )

    # Filtro por cliente
    clientes_list = ['Todos'] + sorted(df['cliente'].unique().tolist())
    cliente_selected = st.selectbox("Selecione o cliente:", clientes_list)

    # Filtra o DataFrame conforme seleção
    df_filtrado = df.copy()

    if categorias_selected and len(categorias_selected) < len(categorias_list):
        df_filtrado = df_filtrado[df_filtrado['categoria'].isin(categorias_selected)]

    if mes_selected and len(mes_selected) < len(mes_list):
        df_filtrado = df_filtrado[df_filtrado['mes'].isin(mes_selected)]

    if formas_pagamento_selected and len(formas_pagamento_selected) < len(formas_pagamento_list):
        df_filtrado = df_filtrado[df_filtrado['forma_pagamento'].isin(formas_pagamento_selected)]

    if cliente_selected != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['cliente'] == cliente_selected]

    with st.expander('Clique aqui para ver a tabela'):
        st.dataframe(df_filtrado)
