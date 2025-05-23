'''
1. Quais são os diretores mais recorrentes?
2. Qual a média das avaliações?
3. Quais os filmes mais antigos e mais recentes?
4. Qual a média de duração dos filmes?
5. Quantos filmes há por década?
6. Qual gênero é mais frequente?
7. Quais os filmes com mais de 3 horas de duração?
8. Quais são os 10 melhores filmes de acordo com as avaliações? E os 10
piores?
'''

import pandas as pd

df = pd.read_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/imdb_top_250_movies.csv', sep=',', encoding='utf-8', parse_dates=['year'])

# Exercise 1

counts_directors = df['directors'].value_counts()

print(counts_directors)
print('--------------------------------------------------')
print(counts_directors.head(5))
print('--------------------------------------------------')

# Exercise 2

print(f'Média das avaliações dos {df.shape[0]} filmes: {df['rating'].mean():.2f}')
print('--------------------------------------------------')

# Exercise 3

df['year_format'] = df['year'].dt.year

years_ascends = df.sort_values('year')

print('5 Filmes mais antigos:')
print(years_ascends.head(5)[['name', 'year_format']])
print('--------------------------------------------------')

print('5 Filmes mais novos:')
print(years_ascends.tail(5)[['name', 'year_format']])
print('--------------------------------------------------')

# Exercise 4

df['duration'] = df['run_time'].str.extract(r'(\d+)h').astype(float) * 60 + df['run_time'].str.extract(r'(\d+)m').astype(float)

average = df['duration'].mean()

print(f'A média dos filmes é: {average:.2f} minutos ou {(average / 60):.2f} horas')
print('--------------------------------------------------')

# Exercise 5 

df['decade'] = (df['year'].dt.year // 10) * 10

print(df['decade'].value_counts())
print('--------------------------------------------------')

# Exercise 6

print(df['genre'].mode())
print('--------------------------------------------------')

# Exercise 7

print('Filmes com mais de 3 horas de duração (180 minutos):')
print(df.loc[df['duration'] > 180][['name', 'duration']])
print('--------------------------------------------------')

# Exercise 8

top = df.groupby('name')['rating'].first() # Usando qualquer método para indexar e formar uma Série/DateFrame
top10 = top.sort_values(ascending = False).head(10)
not_top10 = top.sort_values(ascending = False).tail(10)

print('10 Filmes mais avaliados:')
print(top10)
print('--------------------------------------------------')

print('10 Filmes menos avaliados:')
print(not_top10)
print('--------------------------------------------------')

'''
1. Análise de décadas
1.1. Crie uma nova coluna chamada Década;
1.2. Agrupe os filmes por década e mostre quantos filmes há em cada.
1.3. Qual foi a década com mais filmes no Top 250?
1.4. Para cada década, calcule a nota média e duração média dos filmes.
1.5. Salve esse resumo em um novo arquivo .csv chamado decades_summary.csv.
'''

# Exercise 1.1

print(df['decade'])
print('--------------------------------------------------')

# Exercise 1.2

print(df.groupby('decade')['name'].count())
print('--------------------------------------------------')

movies_decades = df.groupby('decade')['name'].apply(list)
print(movies_decades)
print('--------------------------------------------------')

# Exercise 1.3

decade_counter = df.groupby('decade')['name'].count()
print(df['decade'].value_counts().head(1)) # Option 1
print('--------------------------------------------------')

aux =decade_counter.sort_values(ascending = False) # Option 2
print(aux.head(1))
print('--------------------------------------------------')

# Exercise 1.4

decade_average = df.groupby('decade')[['rating', 'duration']].mean()
print('Media de avaliações (0-10) e duração (em minutos) dos filmes por década:')
print(decade_average)
print('--------------------------------------------------')

# Exercise 1.5 

decade_average.to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/decades_summary.csv', index = True)
