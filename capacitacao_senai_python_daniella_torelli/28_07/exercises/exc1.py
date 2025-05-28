import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/28_07/exercises/csv/life_expectancy_data.csv', sep=',', encoding='utf-8')

st.title('Análise de Expectativa de Vida')
st.subheader('Análise das imunizações:', divider=True)

fig1, ax1 = plt.subplots()

sns.scatterplot(
    x='Hepatitis B',
    y='Life expectancy',
    # hue='Year',
    ax=ax1,
    data=df,
    alpha=0.7
)

ax1.set_title('Relação entre Hepatite B e Expectativa de Vida')
ax1.set_xlabel('Cobertura Hepatite B (porcentagem em recém-nascidos)')
ax1.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig1)

corr_hepatite_b = df['Hepatitis B'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre a cobertura de Hepatite B em recém-nascidos e expectativa de vida ficou em {corr_hepatite_b:.2f}, indicando uma relação fraca e positiva. Portanto, é correto dizer existe um aumento pequeno no percentual de {((corr_hepatite_b ** 2) * 100):.2f}% na expectativa de vida com base no aumento da imunização de Hepatite B em recém-nascidos.')

fig2, ax2 = plt.subplots()

sns.scatterplot(
    x='Polio',
    y='Life expectancy',
    ax=ax2,
    data=df,
    alpha=0.7
)

ax2.set_title('Relação entre Poliomelite e Expectativa de Vida')
ax2.set_xlabel('Cobertura Poliomelite (porcentagem em recém-nascidos)')
ax2.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig2)

corr_poliomelite = df['Polio'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre cobertura de Poliomelite e expectativa de vida ficou em {corr_poliomelite:.2f}, indicando uma relação moderada e positiva. Portanto, é correto dizer que existe um aumento moderado no percentual de {((corr_poliomelite ** 2) * 100):.2f}% na expectativa de vida com base no aumento da imunização de Poliomelite em recém-nascidos.')

fig3, ax3 = plt.subplots()

sns.scatterplot(
    x='Diphtheria',
    y='Life expectancy',
    ax=ax3,
    data=df,
    alpha=0.7
)

ax3.set_title('Relação entre Difteria e Expectativa de Vida')
ax3.set_xlabel('Cobertura Difteria (porcentagem em recém-nascidos)')
ax3.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig3)

corr_difteria = df['Diphtheria'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre cobertura de Difteria e expectativa de vida ficou em {corr_difteria:.2f}, indicando uma relação moderada e positiva. Portanto, é correto dizer que há um aumento moderado no percentual de {((corr_difteria ** 2) * 100):.2f}% na expectativa de vida com base no aumento da imunização de Difteria em recém-nascidos.')

st.subheader('Análise das Mortalidades', divider=True)

fig4, ax4 = plt.subplots()

sns.regplot(
    x='Adult Mortality',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax4,
    data=df

)

ax4.set_title('Relação entre Mortalidade Adulta e Expectativa de Vida')
ax4.set_xlabel('Mortalidade Adulta (por 1000 adultos entre 15-60 anos)')
ax4.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig4)

corr_morte_adulta = df['Adult Mortality'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre mortalidade adulta e expectativa de vida ficou em {corr_morte_adulta:.2f}, indicando uma relação forte e negativa. Portanto, é correto dizer que existe uma diminuição grande no percentual de {((corr_morte_adulta ** 2) * 100):.2f}% na expectativa de vida com base no aumento da mortalidade adulta.')

fig5, ax5 = plt.subplots()

sns.regplot(
    x='infant deaths',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax5,
    data=df
)

ax5.set_title('Relação entre Mortalidade Infantil e Expectativa de Vida')
ax5.set_xlabel('Mortalidade Infantil (por 1000 habitantes)')
ax5.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig5)

corr_morte_infaltil = df['infant deaths'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre mortalidade Infantil e Expectativa de Vida ficou em {corr_morte_infaltil:.2f}, indicando uma relação fraca e negativa. Portanto, é correto dizer que existe uma diminuição pequena no percentual de {((corr_morte_infaltil ** 2) * 100):.2f}% na expectativa de vida com base no aumento da mortalidade infantil.')

fig6, ax6 = plt.subplots()

sns.regplot(
    x='under-five deaths',
    y='Life expectancy',
	scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax6,
    data=df
)

ax6.set_title('Relação entre Mortalidade de Crianças < 5 Anos e Expectativa de Vida')
ax6.set_xlabel('Mortalidade Crianças < 5 Anos (por 1000 habitantes)')
ax6.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig6)

corr_morte_crianca = df['under-five deaths'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre mortalidade de crianças com menos de 5 anos de idade e expectativa de vida ficou em {corr_morte_crianca:.2f}, indicando uma relação fraca e negativa. Portanto, é correto dizer que existe uma diminuição pequena no percentual de {((corr_morte_crianca ** 2) * 100):.2f}% na expectativa de vida com base no aumento da mortalidade infantil.')

st.subheader('Análise de Aspectos Econômicos', divider=True)

df_brazil = df[df["Country"] == "Brazil"].copy()

df_brazil["percentage expenditure"] = (df_brazil["percentage expenditure"].str.replace(r"\.", "", regex=True).astype(float))

df_brazil["GDP"] = (df_brazil["GDP"].str.replace(r"\.", "", regex=True).astype(float))

df_brazil["Life expectancy"] = df_brazil["Life expectancy"].astype(float)

fig7, ax7 = plt.subplots()

sns.regplot(
    data=df_brazil,
    x="percentage expenditure",
    y="Life expectancy",
	scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax7
)

ax7.set_title("Relação entre Gastos em Saúde no Brasil e Expectativa de Vida")
ax7.set_xlabel("Gastos em Saúde")
ax7.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig7)

corr_gastos = df_brazil['percentage expenditure'].corr(df_brazil['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre gastos em saúde no Brasil e expectativa de vida ficou em {corr_gastos:.2f}, indicando uma relação fraca e positiva. Portanto, é correto dizer que existe um aumento pequeno no percentual de {((corr_gastos ** 2) * 100):.2f}% na expectativa de vida com base no aumento dos gastos em saúde no Brasil.')

fig8, ax8 = plt.subplots()

sns.regplot(
    data=df_brazil,
    x='GDP',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax8
)

ax8.set_title("Relação entre PIB Brasileiro e Expectativa de Vida")
ax8.set_xlabel("PIB Brasileiro (em dólar)")
ax8.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig8)

corr_pib_brazil = df_brazil['GDP'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre o PIB brasileiro e expectativa de vida ficou em {corr_pib_brazil:.2f}, indicando uma relação fraca e negativa. Portanto, é correto dizer que existe uma diminuição pequena no percentual de {((corr_pib_brazil ** 2) * 100):.2f}% na expectativa de vida com base no aumento do PIB brasileiro.')

fig9, ax9 = plt.subplots()

df["GDP"] = (df["GDP"].str.replace(r"\.", "", regex=True).astype(float))

df["Life expectancy"] = df["Life expectancy"].astype(float)

sns.regplot(
    data=df,
    x='GDP',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax9
)

ax9.set_title("Relação entre PIB (demais países) e Expectativa de Vida")
ax9.set_xlabel("PIB (em dólar)")
ax9.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig9)

corr_pib = df['GDP'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre os PIBs dos demais países e expectativa de vida ficou em {corr_pib:.2f}, indicando uma relação praticamente inexistente. Portanto, é correto dizer que existe um percentual de {((corr_pib ** 2) * 100):.2f}% na expectativa de vida com base nos PIBs dos demais países.')

fig10, ax10 = plt.subplots()

df["Total expenditure"] = df["Total expenditure"].astype(float)

sns.regplot(
    data=df,
    x='Total expenditure',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax10
)

ax10.set_title("Relação entre Despesa Total do Governo em Saúde (%) e Expectativa de Vida")
ax10.set_xlabel("Despesa Total do Governo em Saúde (%)")
ax10.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig10)

corr_investimento = df['Total expenditure'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre a porcentagem da despesa total do governo em saúde e expectativa de vida ficou em {corr_investimento:.2f}, indicando uma relação fraca e negativa. Portanto, é correto dizer que existe uma diminuição pequena no percentual de {((corr_investimento ** 2) * 100):.2f}% na expectativa de vida com base no aumento da(s) despesa(s) total do governo em saúde.')

st.subheader('Análise de Aspectos Sociais', divider=True)

fig11, ax11 = plt.subplots()

sns.regplot(
    data=df,
    x='Schooling',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax11
)

ax11.set_title("Relação entre Escolaridade e Expectativa de Vida")
ax11.set_xlabel("Escolaridade (número de anos em escola)")
ax11.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig11)

corr_escolaridade = df['Schooling'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre o nível de escolaridade e expectativa de vida ficou em {corr_escolaridade:.2f}, indicando uma relação forte e positiva. Portanto, é correto dizer que existe um aumento grande no percentual de {((corr_escolaridade ** 2) * 100):.2f}% na expectativa de vida com base no aumento do nível de escolaridade.')

fig12, ax12 = plt.subplots()

sns.regplot(
    data=df,
    x='Income composition of resources',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax12
)

ax12.set_title("Relação entre Índice de Desenvolvimento Humano e Expectativa de Vida")
ax12.set_xlabel("IDH (0 - 1000)")
ax12.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig12)

corr_idh = df['Income composition of resources'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre o IDH e expectativa de vida ficou em {corr_idh:.2f}, indicando uma relação moderada e positiva. Portanto, é correto dizer que existe um aumento moderado no percentual de {((corr_idh ** 2) * 100):.2f}% na expectativa de vida com base no aumento do IDH.')

fig13, ax13 = plt.subplots()

sns.regplot(
    data=df,
    x='Population',
    y='Life expectancy',
    scatter={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax13
)

ax13.set_title('Relação entre População e Expectativa de Vida')
ax13.set_xlabel('População')
ax13.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig13)

st.text('Os dados da coluna “Population” apresentam inconsistências, o que inviabiliza uma análise precisa e confiável.')

fig14, ax14 = plt.subplots()

sns.regplot(
    data=df,
    x='Alcohol',
    y='Life expectancy',
    scatter_kws={'alpha':0.5},
    line_kws={'color':'red'},
    ax=ax14
)

ax14.set_title('Relação entre Alcoolismo per capita e Expectativa de Vida')
ax14.set_xlabel('Alcoolismo per capita (litros de álcool)')
ax14.set_ylabel('Expectativa de Vida (em anos)')

st.pyplot(fig14)

corr_alcoolismo = df['Alcohol'].corr(df['Life expectancy'])

st.text(f'O coeficiente de correlação de Pearson entre o alcoolismo per capita e expectativa de vida ficou em {corr_alcoolismo:.2f}, indicando uma relação moderada e positiva. Portanto, é correto dizer que existe um aumento moderado no percentual de {((corr_alcoolismo ** 2) * 100):.2f}% na expectativa de vida com base no aumento do alcoolismo per capita.')

fig15, ax15 = plt.subplots()

sns.boxplot(
    data=df,
    x="Status",
    y="Life expectancy",
    ax=ax15
)
ax15.set_title("Relação entre Nível de Desenvolvimento do País e Expectativa de Vida")
ax15.set_xlabel("Nível de Desenvolvimento")
ax15.set_ylabel("Expectativa de Vida (em anos)")

st.pyplot(fig15)

st.text('Analisando o gráfico (boxplot), observa-se que os países desenvolvidos apresentam mediana maior (~80 anos) em relação aos países em desenvolvimento (~70 anos).')

st.subheader('Análise de Aspectos de Saúde', divider=True)
