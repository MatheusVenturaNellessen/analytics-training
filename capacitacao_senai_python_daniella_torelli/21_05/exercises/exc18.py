import csv
from collections import Counter

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    date = []

    for line in reader:
        # json = dict(zip(header, line))
        date.append(line[0])

print(Counter(date).most_common())
