import csv
from collections import Counter

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    aux = []

    for line in reader:

        aux.append(line[1])

        frequency = Counter(aux)

print(frequency.most_common()) # Para encontrar o produto mais vendido: passar parâmetro 1 
