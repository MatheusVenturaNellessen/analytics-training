'''
1. Ler os dados do arquivo feedbacks.csv
2. Calcular média de nota por curso
3. Identifica o curso com melhor e pior avaliação
4. Contar quantas pessoas recomendaram cada curso
5. Ver quantidade de feedbacks por dia
6. Filtrar só os feedbacks negativos (nota <= 2)
7. Salvar um relatório negatives_feedbacks.csv
'''

import pandas as pd

# Exercise 1

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/feedbacks.csv', sep=',', encoding='utf-8', parse_dates=['data'])

# Exercise 2

average = df.groupby('curso')['nota'].mean()
print(average)

print('-------------------------------')

# Exercício 3

max_average = df.groupby('curso')['nota'].mean()
min_average = df.groupby('curso')['nota'].mean()

print(f'Curso melhor avaliado: {max_average.idxmax()} | Nota {df.groupby('curso')['nota'].mean()[min_average.idxmax()]}')
print(f'Curso menos avaliado: {min_average.idxmin()} | Nota: {df.groupby('curso')['nota'].mean()[min_average.idxmin()]}')

print('-------------------------------')

# Exercise 4 

# counter = 0
# for i in range(len(df.loc[:, 'recomendaria'].values)):
#     if (df.loc[:, 'recomendaria'].values)[i] == 'Sim':
#         counter +=1

# print(counter)

recommended = df.loc[df['recomendaria'] == 'Sim']

print(recommended.groupby('curso')['recomendaria'].count())

print('-------------------------------')

# Exercise 5

print(df.groupby('data').size())

print('-------------------------------')

# Exercise 6

print(df.loc[df['nota'] < 2])

print('-------------------------------')

# Exercise 7

negative_feedbacks = df.loc[df['nota'] < 2]

backup = negative_feedbacks.copy()

negative_feedbacks.to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/negative_feedbacks.csv', index = False)
