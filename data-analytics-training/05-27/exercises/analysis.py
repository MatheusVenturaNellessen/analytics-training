import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/27_05/exercises/csv/bank_clients.csv', sep=',', encoding='utf-8')


df['Cliente'] = df['Categoria'] == 'Cliente'
df['Ex-cliente'] = df['Categoria'] == 'Cancelados'

st.title('Análise de Dados ::')
st.subheader('Distribuição por Gênero:', divider=True)

distribuicao_genero, ax1 = plt.subplots()

sns.countplot(x='Sexo', hue='Categoria', data=df, ax=ax1)

st.pyplot(distribuicao_genero)

st.text('Este gráfico de Distribuição por Gênero faz uma contagem de gênero (homens e mulheres) por categoria (clientes e cancelados) resultando se há diferença de comportamento entre os sexos. Podemos analisar que as mulheres têm taxa de cancelamento maior em relação aos homens. Embora essa diferença não é muito significativa, pode valer a pena investigar ofertas ou comunicações específicas para o público feminino.')

st.subheader('Gráfico de Idade por Categoria', divider=True)

idade_por_categoria, ax2 = plt.subplots()

sns.boxplot(x='Categoria', y='Idade', data=df, ax=ax2)

st.pyplot(idade_por_categoria)

st.text('Este Gráfico Idade por Categoria destaca medianas, quartis e outliers da idade dos clientes ativos e inativos (cancelados). Pode-se analisar que a mediana de idade dos cancelados é ligeiramente maior que a dos ativos. Ambas distribuições se sobrepõem muito, sugerindo que idade isoladamente não é um forte preditor de cancelamento.')

st.subheader('Gráfico de Transações nos Últimos 12 Meses por Categoria', divider=True)

transacoes_por_categoria, ax3 = plt.subplots()

sns.boxplot(x='Categoria', y='Qtde Transacoes 12m', data=df, ax=ax3)

st.pyplot(transacoes_por_categoria)

st.text('Este Gráfico de Transações nos Últimos 12 Meses por Categoria revela diferenças de engajamento. A análise revela que clientes inativos têm uma menor mediana em relação aos clientes ativos. Em conclusão, um baixo uso do cartão está fortemente associado ao cancelamento.')

st.subheader('Gráfico de Meses como Cliente por Quantidade de Transações nos Últimos 12 Meses', divider=True)

qtd_meses_por_qnt_transacoes, ax4 = plt.subplots()

sns.scatterplot(x="Meses como Cliente", y="Qtde Transacoes 12m", hue='Categoria', data=df, ax=ax4, alpha=0.7)

st.pyplot(qtd_meses_por_qnt_transacoes)

st.write('Gráfico entre tempo de relacionamento e volume de transações ajuda a identificar padrões de comportamento. A análise aponta que Clientes inativos combinam poucos meses como cliente e baixa quantidade de transações. Já clientes ativos possuem longa data como clientes e alto volume de transações.')

st.header('Conclusão')
st.markdown("""
1. Focar em campanhas de reengajamento para quem tem baixo uso nos primeiros meses.
2. Testar ofertas especiais ou educação financeira para grupos com perfil demográfico.
3. Monitorar clientes nos primeiros 6 meses de uso e intervir proativamente caso o número de transações fique abaixo de um limiar.
""")
