import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Exibindo Estatísticas")

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/26_05/exercises/csv/statistics_visualization.csv', sep=',', encoding='utf-8')

menu = st.sidebar.selectbox("Escolha uma coluna numérica:", ['idade', 'salario'])

# Exibir análise de dados

st.subheader(f"Média de {menu}", divider= True)
st.write(df[menu].mean())

st.subheader(f"Moda de {menu}", divider= True)
st.write(df[menu].mode().values[0])

st.subheader(f"Mediana de {menu}", divider= True)
st.write(df[menu].median())

st.subheader(f"Variância de {menu}", divider= True)
st.write(df[menu].var())

st.subheader(f"Amplitude de {menu}", divider= True)
st.write(df[menu].max() - df[menu].min())

# Plotar gráficos

st.subheader('Gráfico de Distribuição por Estados')

fig1, ax1 = plt.subplots()
sns.countplot(x='estado', data=df, ax=ax1)
plt.title('Gráfico de Distribuição por Estados')
plt.xlabel('Estado')
plt.ylabel('Quantidade')
st.pyplot(fig1)

st.subheader('BoxPlot entre Departamento e Salário')

fig2, ax2 = plt.subplots()
sns.boxplot(x='departamento', y='salario', data=df, ax=ax2)
plt.title('BoxPlot: Departamento x Salário')
plt.xlabel('Departamento')
plt.ylabel('Salário (em Reais)')
st.pyplot(fig2)

st.subheader('Gráfico de dispersão entre idade e salário, categorizado por Departamento')

fig3, ax3 = plt.subplots()
sns.scatterplot(
    x='idade',
    y='salario',
    hue='departamento',
    palette='bright',
    s=60,
    alpha=0.6,
    data=df,
    ax=ax3
)

plt.title('Dispersão: Idade x Salário por Departamento')
plt.xlabel('Idade (em Anos)')
plt.ylabel('Salário (em Reais)')
plt.legend(title='Departamento', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.tight_layout()

st.pyplot(fig3)
