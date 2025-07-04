import csv
from collections import defaultdict

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    price_product = defaultdict(list)

    for line in reader:
        json = dict(zip(header, line))

        price_product[json['produto']].append(float(json['preco']))

print(dict(price_product))
