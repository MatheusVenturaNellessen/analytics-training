'''
1 - Carregue sells.csv;
2 - Exiba estatísticas gerais;
3 - Liste os 3 produtos mais vendidos;
4 - Crie uma coluna de valor total e exiba as 5 maiores vendas;
5 - Filtre apenas vendas do último mês;
6 - Exporte o resultado filtrado para relatorio_maio.csv.
'''

import pandas as pd

# Exercise 1

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/sells.csv', sep=',', encoding='utf-8', parse_dates=['data'])

# Exercise 2

print(f'Total de vendas: {len(df)}')

print('-----------------------------------------------')

print(f'A soma dos valores é: R$ {(df['quantidade'] * df['preco']).sum():.2f}')

print('-----------------------------------------------')

print(f'Média das vendas: R$ {((df['quantidade'] * df['preco']).sum() / len(df)):.2f}')

print('-----------------------------------------------')

# Exercise 3 

# print(f'Os 3 produtos mais vendidos: {df['produto'].value_counts().head(3)}')

# Exercício 4

df['total'] = df['quantidade'] * df['preco']
print(df)

print('-----------------------------------------------')

print(df.nlargest(5, 'total'))

print('-----------------------------------------------')

# Exercício 5

last_month = df['data'].dt.month.max()

month = df.loc[df['data'].dt.month == last_month]

report_month = month.copy()

report_month.to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/report_month.csv', index = False)




# print(last_month)