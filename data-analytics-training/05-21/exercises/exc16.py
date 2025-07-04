import csv
from collections import Counter

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    seels_above5 = []

    for line in reader:
        json = dict(zip(header, line))

        if float(json['quantidade']) > 5:
            seels_above5.append(f"Produto: {json['produto']} | Preço: {float(json['preco'])}")

print(seels_above5)