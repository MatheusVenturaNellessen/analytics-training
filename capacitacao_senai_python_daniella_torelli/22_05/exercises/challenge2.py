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

print('Série "decade":')
print(df['decade'])
print('--------------------------------------------------')

# Exercise 1.2

print('Quantidade de filmes por década:')

print(df.groupby('decade')['name'].count())
print('--------------------------------------------------')

movies_decades = df.groupby('decade')['name'].apply(list)
print(movies_decades)
print('--------------------------------------------------')

# Exercise 1.3

decade_counter = df.groupby('decade')['name'].count()
print(f'Década com mais filmes: {df['decade'].value_counts().head(1)}') # Option 1
print('--------------------------------------------------')

aux =decade_counter.sort_values(ascending = False) # Option 2
print(f'Década com mais filmes: {aux.head(1)}')
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

print('Nota média dos filmes de cada diretor:')
print(averages.sort_values(ascending = False))
print('--------------------------------------------------')

# Exercise 2.4

director_high_ranking_movie = df.sort_values(by='rating', ascending = False)['directors']

# print(director_high_ranking_movie)

director_most_ranking_movie = director_high_ranking_movie.head(1)

print(f'Diretor do filme mais bem avaliado: {director_most_ranking_movie}')
print('--------------------------------------------------')


# Exercise 2.5 

directors_summary = df.groupby('directors').agg(
    qtd_movies=('name', 'count'),
    ranking_average=('rating', 'mean')
).reset_index()

print('DataFrame com diretor, nome e nota dos filmes:')
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

print('Categoriza filmes em "Curto", "Médio", "Longo":')
print(df['duration_category'])
print('--------------------------------------------------')

# Exercise 3.2

movies_by_category = df['duration_category'].value_counts()

print('Quantidade de filmes por categoria:')
print(movies_by_category)
print('--------------------------------------------------')


# Exercise 3.3 

average_by_category = df.groupby('duration_category')['rating'].mean()

print('Nota média por categoria de filme:')
print(average_by_category)
print('--------------------------------------------------')

# Exercise 3.4

comum_category = movies_by_category.sort_values(ascending = False)

print('Categoria de filme mais comum:')
print(comum_category.head(1))
print('--------------------------------------------------')

'''
4. Filmes por ano:
4.1. Quantos filmes foram lançados em cada ano?;
4.2. Qual ano teve mais filmes no Top 250?;
4.3. Quais os filmes lançados entre 1990 e 1999 com nota acima de 3?;
4.4. Exporte esses filmes outro arquivo .csv.
'''

# Exercise 4.1

movies_by_year = df['year_format'].value_counts()

print('Filmes lançados por ano:')
print(movies_by_year)
print('--------------------------------------------------')

# Exercise 4.2

print('Ano com mais filmes:')
print(movies_by_year.head(1))
print('--------------------------------------------------')

# Exercise 4.3 

movies_decade90_rating3plus = df[(df['decade'] == 1990) & (df['rating'] > 3)]

print('Filmes lançados entre 1990 e 1999 com nota acima de 3:')
print(movies_decade90_rating3plus[['name', 'rating', 'year_format']])
print('--------------------------------------------------')

# Exercise 4.4

movies_decade90_rating3plus[['name', 'rating', 'year_format']].to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/decade90_movies_rating3plus_summary.csv', index = False)

'''
5. Análise textual (coluna "Title"):
5.1. Quantos filmes contêm a palavra "Love" no título?;
5.2. Liste os filmes que têm a palavra "War", "God" ou "King" no título;
5.3. Crie uma nova coluna com os títulos em letras maiúsculas;
5.4. Quantos títulos têm mais de 25 caracteres?;
5.5. Qual o título mais longo da lista?
'''

# Exercise 5.1

print(f'Quantidade de filmes que contém a palavra "Love": {df['name'].str.contains('Love').sum()}')
print('--------------------------------------------------')

# Exercise 5.2 

filter = df['name'].str.contains(r"\bWar|God|King\b", case = False, na = False)

print('Filmes que contém a(s) palavra(s) "War", "God" e/ou "King" em seu título:')
print(df[filter]['name'])
print('--------------------------------------------------')

# Exercise 5.3

df['name_upper_case'] = df['name'].str.upper()
print('Serie "name_upper_case":')
print(df['name_upper_case'])
print('--------------------------------------------------')

# Exercise 5.4 

print('Quantidade de filmes com títulos com mais de 25 caracteres:')
print(df['name'].str.len().gt(25).sum())
print('--------------------------------------------------')

# Exercise 5.5

longest_name = df.loc[df['name'].str.len().idxmax()] # Retorna o index
print(f'Filme com título mais longo: {longest_name['name']}')
print('--------------------------------------------------')

'''
6. Filtros múltiplos:
6.1. Mostre todos os filmes:
    - Nota >= 9;
    - Duração <= 100 minutos;
    - Lançados após o ano 2000;
6.2. Filtre os filmes que:
    - Têm duração entre 120 e 150 minutos;
    - Foram dirigidos por "Christopher Nolan";
    - Estão entre os 50 primeiros do ranking;
    - Exporte para outro arquivo .csv;
6.3. Mostre os filmes com título iniciado pela letra "A" e nota acima de 8.0;
6.4. Liste todos os filmes que não foram dirigidos por "Steven Spielberg"
'''

# Exercise 6.1

filter_6_1 = df[
    (df['rating'] >= 8) &
    (df['duration'] <= 100) &
    (df['year_format'] > 2000)
].drop_duplicates(subset = ['name'])

print('Filmes com nota igual ou maior a 8, duração menor ou igual a 100 minutos e pós anos 2000:')
print(filter_6_1[['name', 'rating', 'duration', 'year_format']])
print('--------------------------------------------------')

# Exercise 6.2

filter_6_2 = df[
    (df['duration'] >= 120) &
    (df['duration'] <= 150) &
    (df['directors'] == 'Christopher Nolan') &
    (df['rank'] <= 50)
]

filter_6_2.to_csv('capacitacao_senai_python_daniella_torelli/22_05/csv/filter_6_2.csv', index = False)

print('Filmes de 120 a 150 minutos, de Christopher Nolan e estão no top 50:')
print(filter_6_2[['rank', 'name', 'rating', 'duration']])
print('--------------------------------------------------')

# Exercise 6.3

filter_6_3 = df[
    df['name'].str.startswith('A') &
    (df['rating'] > 8.0)
].drop_duplicates(subset = ['name'])

print("Filmes com título iniciando em 'A' e nota maior que 8.0:")
print(filter_6_3[['name', 'rating']])
print('--------------------------------------------------')

# Exercise 6.4

filter_6_4 = df[
    df['directors'] != 'Steven Spielberg'
]

print("Filmes sem direção de Steven Spielberg:")
print(filter_6_4[['name', 'directors']])
print('--------------------------------------------------')

print('\nFim.\n')
