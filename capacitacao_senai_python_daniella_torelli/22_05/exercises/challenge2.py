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
1.2. Agrupe os filmes por década e mostre quantos filmes por década;
1.3. Qual foi a década com mais filmes no Top 250?;
1.4. Por década, calcule a nota média e duração média dos filmes;
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


'''
2. Diretores e frequência:
2.1. Quantos diretores diferentes existem na lista?;
2.2. Quais são os 5 diretores mais frequentes?;
2.3. Qual é a nota média dos filmes de cada diretor (>= 3 filmes)?;
2.4. Qual diretor tem o filme mais bem avaliado?;
2.5. Exporte para .csv um ranking com diretor, quantidade de filmes, nota média.
'''

# Exercise 2.1

# print(df['directors'].count)

df['directors'] = df['directors'].str.split(',')
# print(directors_split)

df = df.explode('directors')
# print(directors_exploded)

df['directors'] = df['directors'].str.strip()

unique_directors = df['directors'].nunique()

print(f'Total de diretores: {unique_directors}')
print('--------------------------------------------------')

# print(df['directors'])
# print('FUNCIONOU!!!')

# Exercise 2.2

print('Os 5 diretores mais frequentes e quantas vezes aparecem no DataFrame:')
print((df['directors'].value_counts()).head(5))
print('--------------------------------------------------')

# Exercise 2.3

# directors_counter = df['directors'].value_counts()

# directors_more_than3_movies = directors_counter[directors_counter >= 3]

# print(directors_more_than3_movies.groupby(['directors'])['rating'].mean())

# directors_counter = df['directors'].value_counts()

# if directors_counter[directors_counter >= 3]:

#     print(df.groupby('directors')[['rating']].mean())

directors_counter = df['directors'].value_counts()

directors_more_3_movies = directors_counter[directors_counter >= 3].index

df_filtered_by_directors = df[df['directors'].isin(directors_more_3_movies)]

averages = df_filtered_by_directors.groupby('directors')['rating'].mean()

print(averages.sort_values(ascending = False))
print('--------------------------------------------------')

# Exercise 2.4

director_high_ranking_movie = df.sort_values(by='rating', ascending = False)['directors']

# print(director_high_ranking_movie)

director_most_ranking_movie = director_high_ranking_movie.head(1)

print(f'Diretor do filme mais bem avaliado: {director_most_ranking_movie}')

# Exercise 2.5 

directors_summary = df.groupby('directors').agg(
    qtd_movies=('name', 'count'),
    ranking_average=('rating', 'mean')
).reset_index()

print(directors_summary)
print('--------------------------------------------------')

directors_summary.to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/directors_summary.csv', index = False)

'''
3. Filmes por duração:
3.1. Crie uma nova coluna chamada com base nas regras:
    - Curto se duração < 90 min;
    - Médio se entre 90 e 150;
    - Longo se > 150.
3.2. Mostre quantos filmes tem em cada categoria;
3.3. Qual a nota média de cada categoria?;
3.4. Qual categoria é mais comum no Top 250?
'''

# Exercise 3.1

def categorize_duration(duration):
    if duration < 90:
        return 'Curto'
    elif duration <= 150:
        return 'Médio'
    else:
        return 'Longo'

df['duration_category'] = df['duration'].apply(categorize_duration)

print(df['duration_category'])
print('--------------------------------------------------')

# Exercise 3.2

movies_by_category = df['duration_category'].value_counts()

print(movies_by_category)
print('--------------------------------------------------')


# Exercise 3.3 

average_by_category = df.groupby('duration_category')['rating'].mean()

print(average_by_category)
print('--------------------------------------------------')

# Exercise 3.4

comum_category = movies_by_category.sort_values(ascending = False)

print(comum_category.head(1))
print('--------------------------------------------------')

