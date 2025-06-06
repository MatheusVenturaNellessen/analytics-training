import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import date, datetime, timedelta
import numpy as np

# Estilos
st.markdown("""
<style>
    .mc-default {
        background: #fff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-right: 15px;
    }
    .ml-default {
        color: #111827;
        font-size: 25px;
        font-weight: 600;
        font-variant: small-caps;
        text-align: center;
    }
    .mv-default {
        color: #111827;
        font-size: 45px;
        font-weight: 700;
        text-align: center;
    }
    .mdescription-default {
        color: #7C3AED;
        font-size: 20px;
        font-weight: 600;
        text-align: left;
    }

    .mc-bad {
        background: #F59E42;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-right: 15px;
    }
    .ml-bad {
        color: #111827;
        font-size: 25px;
        font-weight: 600;
        font-variant: small-caps;
        text-align: center;
    }
    .mv-bad {
        color: #111827;
        font-size: 45px;
        font-weight: 700;
        text-align: center;
    }
    .mdescription-bad {
        color: #7C3AED;
        font-size: 20px;
        font-weight: 600;
        text-align: left;
    }
    .md-bad {
        color: red;
        font-weight: 700;
                font-size: 20px;
    }
    .md-bad:before {
        content: "↓ ";
    }

    h1 {
        color: #111827;
        text-align: center;
        font-variant: small-caps;
    }

    .diminuir-font {
        font-size: 31px;
    }
</style>
""", unsafe_allow_html=True)

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
    st.markdown("""
    <h1 class="h1-home">Análise Geral</h1>
    """,
    unsafe_allow_html=True
    )

    valor_total_sum = df['valor_total'].sum()  # Soma todos os valores da coluna valor_total
    qtd_vendas = df.shape[0]  # Retorna a quantidade de linhas ~= quantidade de vendas
    valor_medio = df['valor_total'].mean()  # Faz média dos valores da coluna valor_total
    qtd_clientes_unique = df['cliente'].nunique()  # Conta quantos clientes únicos há
    produto_mais_vendido = df['produto'].value_counts().idxmax()  # Produto mais vendido
    forma_pagamento_mais_usada = df['forma_pagamento'].value_counts().idxmax()  # Forma de pagamento mais usada

    # Exibe os indicadores em colunas
    col1, col2, = st.columns(2)
    col3, col4, = st.columns(2)
    col5, col6 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Faturamento total</div>
            <div class="mv-default">R$ {valor_total_sum:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Vendas (em quantidade)</div>
            <div class="mv-default">{qtd_vendas}</div>
        </div>
        <style>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Ticket médio</div>
            <div class="mv-default">R$ {valor_medio:,.2f}</div>
            <div class="mdescription-default">Valor médio do valor de venda</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Clientes únicos</div>
            <div class="mv-default">{qtd_clientes_unique}</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Melhor produto</div>
            <div class="mv-default">{produto_mais_vendido}</div>
            <div class="mdescription-default">Item mais vendido</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
        <div class="mc-default">
            <div class="ml-default">Método mais usado</div>
            <div class="mv-default">{forma_pagamento_mais_usada}</div>
        </div>
        """, unsafe_allow_html=True)

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
    with col7:
        st.markdown(f"""
        <div class="mc-bad">
            <div class="ml-bad">Comparação de vendas</div>
            <div class="mv-bad">R$ {diferenca_vendas_entre_mes_atual_e_menos1:,.2f}</div>
            <div class="md-bad">{diferenca_porcem_entre_mes_atual_e_menos1:.2f}%</div>
            <div class="mdescription-bad">Entre os meses {mes_atual} vs. {mes_menos1}</div>
        </div>
        """, unsafe_allow_html=True)

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
    st.markdown('''
    <h1>Valor total por categoria</h1>
    ''',
    unsafe_allow_html=True
    )

    categorias = sorted(df['categoria'].unique())

    categorias_opt = st.selectbox('Selecione a categoria:', categorias)

    df_categoria = df[df['categoria'] == categorias_opt]
    soma_valor_total_por_categoria = df_categoria['valor_total'].sum()

    st.markdown(f'''
        <div class="mc-default">
            <div class="ml-default">Soma de categoria {categorias_opt}</div>
            <div class="mv-default">R$ {soma_valor_total_por_categoria:,.2f}</div>
        </div>
    ''',
    unsafe_allow_html=True
    )

    # 2º filtro: média do "valor_total" agrupada por "forma_pagamento"
    st.markdown('''
        <h1>Venda média por método de pagamento</h1>
    ''',
    unsafe_allow_html=True
    )

    formas_pagamento = sorted(df['forma_pagamento'].unique())

    forma_pagamento_opt = st.selectbox('Selecione a forma de pagamento:', formas_pagamento)

    media_valor_total = df[df['forma_pagamento'] == forma_pagamento_opt]['valor_total'].mean()

    st.markdown(f'''
        <div class="mc-default">
            <div class="ml-default">Valor médio com {forma_pagamento_opt}</div>
            <div class="mv-default">R$ {media_valor_total:,.2f}</div>
        </div>
    ''',
    unsafe_allow_html=True
    )

    # 3º filtro: top 3 clientes
    st.markdown('''
        <h1>Maiores clientes</h1>
    ''',
    unsafe_allow_html=True
    )

    valor_total_por_cliente = df.groupby('cliente')['valor_total'].sum().sort_values(ascending=False)

    top3_clientes = valor_total_por_cliente.head(3)

    nomes = top3_clientes.index.tolist()
    valores = top3_clientes.values.tolist()

    col11, col22, col33 = st.columns(3)
    with col11:
        st.markdown(f'''
        <div class="mc-default">
            <div class="ml-default">{nomes[0]}</div>
            <div class="mv-default diminuir-font">R$ {valores[0]:,.2f}</div>
        </div>
        ''',
        unsafe_allow_html=True
        )

    with col22:
        st.markdown(f'''
        <div class="mc-default">
            <div class="ml-default">{nomes[1]}</div>
            <div class="mv-default diminuir-font">R$ {valores[1]:,.2f}</div>
        </div>
        ''',
        unsafe_allow_html=True
        )

    with col33:
        st.markdown(f'''
        <div class="mc-default">
            <div class="ml-default">{nomes[2]}</div>
            <div class="mv-default diminuir-font">R$ {valores[2]:,.2f}</div>
        </div>
        ''',
        unsafe_allow_html=True
        )

    # mensagem = ' | '.join([f'{nome}: R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') for nome, valor in zip(nomes, valores)])

    # st.markdown(f'''
    #     <div class="mc-default">
    #         <div class="ml-default">Top 3 clientes</div>
    #         <div class="mv-default diminuir-font">{mensagem}</div>
    #     </div>
    # ''',
    # unsafe_allow_html=True
    # )

elif pagina == "Análises Gráficas":
    # 1º gráfico
    st.markdown('''
        <h1>Produtos mais vendidos</h1>
    ''',
    unsafe_allow_html=True
    )

    top5_produtos = df['produto'].value_counts().head(5)

    fig1, ax1 = plt.subplots()
    top5_produtos.sort_values().plot.barh(ax=ax1)
    ax1.set_xlabel('Quantidade vendida')
    ax1.set_ylabel('Produtos')
    st.pyplot(fig1)

    # 2º gráfico
    st.markdown('''
        <h1>Vendas por categorias</h1>
    ''',
    unsafe_allow_html=True
    )

    categorias = sorted(df['categoria'].unique())
    default_categorias = categorias.copy()

    if 'categorias_multiselect' not in st.session_state:
        st.session_state['categorias_multiselect'] = default_categorias

    if st.button('Resetar filtros'):
        st.session_state['categorias_multiselect'] = default_categorias

    categorias_multiselect = st.multiselect(
        'Selecione a(s) categoria(s) para exibir no gráfico:',
        categorias,
        default=st.session_state['categorias_multiselect'],
        key='categorias_multiselect'
    )

    df_filtro_vendas_por_categoria = df[df['categoria'].isin(categorias_multiselect)]
    vendas_por_categoria_sum = df_filtro_vendas_por_categoria.groupby('categoria')['valor_total'].sum().sort_values()

    fig2, ax2 = plt.subplots()
    vendas_por_categoria_sum.plot.barh(ax=ax2)
    ax2.set_xlabel('Total de Vendas')
    ax2.set_ylabel('Categoria(s)')
    st.pyplot(fig2)

    # 3º gráfico
    st.markdown('''
        <h1>Vendas por produtos</h1>
    ''',
    unsafe_allow_html=True
    )

    produtos = sorted(df['produto'].unique())
    default_produtos = produtos.copy()

    if 'produtos_multiselect' not in st.session_state:
        st.session_state['produtos_multiselect'] = default_produtos

    if st.button('Resetar filtos'):
        st.session_state['produtos_multiselect'] = default_produtos

    produtos_multiselect = st.multiselect(
        'Selecione o(s) produto(s) para exibir no gráfico:',
        produtos,
        default=st.session_state['produtos_multiselect'],
        key='produtos_multiselect'
        )

    df_filtro_vendas_por_produto = df[df['produto'].isin(produtos_multiselect)]

    vendas_por_produto_sum = df_filtro_vendas_por_produto.groupby('produto')['valor_total'].sum().sort_values()

    fig3, ax3 = plt.subplots()
    vendas_por_produto_sum.plot.barh(ax=ax3)
    ax3.set_xlabel('Total de vendas')
    ax3.set_ylabel('Produtos')
    st.pyplot(fig3)

    # 4º gráfico
    st.markdown('''
        <h1>Vendas por horário</h1>
    ''',
    unsafe_allow_html=True
    )

    df['hora'] = df['data_venda'].dt.hour

    vendas_por_hora = df['hora'].value_counts().sort_index()

    fig4, ax4 = plt.subplots()
    vendas_por_hora.plot(ax=ax4, marker='o')
    ax4.set_xlabel("Hora do dia")
    ax4.set_ylabel("Quantidade de vendas")
    st.pyplot(fig4)

    # 5º gráfico
    st.markdown('''
        <h1>Vendas por dias da semana</h1>
    ''',
    unsafe_allow_html=True
    )

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
    st.markdown('''
        <h1>Distribuição: métodos de pagamento</h1>
    ''',
    unsafe_allow_html=True
    )

    qtd_formas_pagamento = df['forma_pagamento'].value_counts()

    fig6, ax6 = plt.subplots()
    ax6.pie(qtd_formas_pagamento, labels=qtd_formas_pagamento.index, autopct='%1.2f%%', startangle=90)
    st.pyplot(fig6)

    # 7º gráfico
    st.markdown('''
        <h1>Somatória: vendas por métodos de pagamento</h1>
    ''',
    unsafe_allow_html=True
    )

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
    st.pyplot(fig8)

    # 8º gráfico
    st.markdown('''
        <h1>Comparação: vendas por mês</h1>
    ''',
    unsafe_allow_html=True
    )

    df['mes'] = df['data_venda'].dt.month

    qtd_vendas_por_mes = df['mes'].value_counts().sort_index()

    fig9, ax9 = plt.subplots()
    qtd_vendas_por_mes.plot(ax=ax9, marker='o')
    ax9.set_xlabel('Mês')
    ax9.set_ylabel('Quantidade de vendas')
    st.pyplot(fig9)

elif pagina == "Tabelas":
    # 1ª tabela: filtra por período
    st.markdown('''
        <h1>Filtragem por períodos</h1>
    ''',
    unsafe_allow_html=True
    )

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
    st.markdown('''
        <h1>Filtragem por métodos de pagamento</h1>
    ''',
    unsafe_allow_html=True
    )

    forma_pagamento_opt = st.selectbox(
        'Selecione a forma de pagamento:',
        sorted(df['forma_pagamento'].unique())
    )

    df_filtro_forma_pagamento = df[df['forma_pagamento'] == forma_pagamento_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_forma_pagamento)

    # 3ª tabela: filtra por cliente
    st.markdown('''
        <h1>Filtragem por clientes</h1>
    ''',
    unsafe_allow_html=True
    )

    clientes = sorted(df['cliente'].unique())

    clientes_opt = st.selectbox(
        'Selecione (ou digite o nome) do cliente:',
        clientes
    )

    df_filtro_cliente = df[df['cliente'] == clientes_opt]

    with st.expander("Clique aqui para ver a tabela"):
        st.dataframe(df_filtro_cliente)

    # 4ª tabela: filtros interativos
    st.markdown('''
        <h1>Filtragens por <span class="hover-me">👆</span></h1>
        <style>
                .hover-me:hover::after {
                    content: " categorias, mês, métodos de pagamento e cliente";
                }
        </style>
    ''',
    unsafe_allow_html=True
    )

    df['mes'] = df['data_venda'].dt.month

    categorias_list = sorted(df['categoria'].unique().tolist())
    mes_list = sorted(df['mes'].unique().tolist())
    formas_pagamento_list = sorted(df['forma_pagamento'].unique().tolist())
    clientes_list = ['Todos'] + sorted(df['cliente'].unique().tolist())

    # 2. Inicializa session_state de cada filtro se não existir
    if 'categorias_selected' not in st.session_state:
        st.session_state['categorias_selected'] = categorias_list

    if 'mes_selected' not in st.session_state:
        st.session_state['mes_selected'] = mes_list

    if 'formas_pagamento_selected' not in st.session_state:
        st.session_state['formas_pagamento_selected'] = formas_pagamento_list

    if 'cliente_selected' not in st.session_state:
        st.session_state['cliente_selected'] = 'Todos'

    # 3. Botão de reset antes dos widgets
    if st.button('Resetar filtros'):
        st.session_state['categorias_selected'] = categorias_list
        st.session_state['mes_selected'] = mes_list
        st.session_state['formas_pagamento_selected'] = formas_pagamento_list
        st.session_state['cliente_selected'] = 'Todos'
        st.rerun()

    # 4. Widgets usando o session_state (com key)
    categorias_selected = st.multiselect(
        "Selecione a(s) categoria(s):",
        options=categorias_list,
        default=st.session_state['categorias_selected'],
        key='categorias_selected'
    )

    mes_selected = st.multiselect(
        'Selecione o mês:',
        options=mes_list,
        default=st.session_state['mes_selected'],
        key='mes_selected'
    )

    formas_pagamento_selected = st.multiselect(
        "Selecione a(s) forma(s) de pagamento:",
        options=formas_pagamento_list,
        default=st.session_state['formas_pagamento_selected'],
        key='formas_pagamento_selected'
    )

    cliente_selected = st.selectbox(
        "Selecione o cliente:",
        clientes_list,
        index=clientes_list.index(st.session_state['cliente_selected']),
        key='cliente_selected'
    )

    # 5. Filtra o DataFrame conforme seleção
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
