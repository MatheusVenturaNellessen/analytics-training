import csv
from collections import defaultdict

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    adder = defaultdict(int)

    for line in reader:
        json = dict(zip(header, line))

        adder[json['produto']] += 1

print(dict(adder))
