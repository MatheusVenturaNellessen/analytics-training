'''
1. Resumo estatístico das colunas idade e salario:
    - média;
    - moda;
    - mediana;
    - variância;
    - amplitude.
2. Criação de uma nova coluna "Faixa Etária":
    - Até 25 anos: Jovem;
    - 26–45 anos: Adulto;
    - Acima de 45: Sênior.
3. Visualizações:
    - Gráfico de barras com a distribuição por estado;
    - Boxplot de salário por departamento;
    - Gráfico de dispersão entre idade e salario, colorido por departamento.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/26_05/exercises/csv/statistics_visualization.csv', sep=',', encoding='utf-8')

# Exercício 1.1

media_idade = df['idade'].mean()
media_salario = df['salario'].mean()

print(f'Média das idades: {media_idade}')
print('--------------------------------------------------')

print(f'Média dos salários: {media_salario}')
print('--------------------------------------------------')

# Exercício 1.2

moda_idade = df['idade'].mode()
moda_salario = df['salario'].mode()

print(f'Moda das idades: {moda_idade.values[0]}')
print('--------------------------------------------------')

print(f'Moda dos salários: {moda_salario.values[0]}')
print('--------------------------------------------------')

# exercício 1.3

mediana_idade = df['idade'].median()
mediana_salario = df['salario'].median()

print(f'Mediana das idades: {mediana_idade}')
print('--------------------------------------------------')

print(f'Mediana dos salários: {mediana_salario}')
print('--------------------------------------------------')

# Exercício 1.4

variancia_idade = df['idade'].var()
variancia_salario = df['salario'].var()

print(f'Variância das idades: {variancia_idade}')
print('--------------------------------------------------')

print(f'Variância dos salários: {variancia_salario}')
print('--------------------------------------------------')

# Exercício 1.5

amplitude_idade = df['idade'].max() - df['idade'].min()
amplitude_salario = df['salario'].max() - df['salario'].min()

print(f'Amplitude das idades: {amplitude_idade}')
print('--------------------------------------------------')

print(f'Amplitude dos salários: {amplitude_salario}')
print('--------------------------------------------------')

# Exercício 2

def categorizar_idade(idade):
    if idade <= 25:
        return 'Jovem'
    elif idade < 46:
        return 'Adulto'
    else:
        return 'Sênior'

df['faixa_etaria'] = df['idade'].apply(categorizar_idade)

print(df['faixa_etaria'])
print('--------------------------------------------------')

sns.countplot(x = 'faixa_etaria', data = df) # Exibi a nova coluna em gráfico de barras
plt.show()

# Exercício 3.1

sns.countplot(x = 'estado', data = df)
plt.show()

# Exercício 3.2

sns.boxplot(x = 'departamento', y = 'salario', data = df)
plt.show()

# Exercício 3.3

sns.scatterplot(
    x = 'idade',
    y = 'salario',
    hue = 'departamento',
    palette = 'bright',
    s = 60,
    alpha = 0.6,
    data = df
)

plt.title('Dispersão: Idade x Salário por Departamento')
plt.xlabel('Idade (em Anos)')
plt.ylabel('Salário (em Reais)')
plt.legend(title='Departamento', bbox_to_anchor=(1.01, 1), loc='upper left')
plt.tight_layout()
plt.show()
