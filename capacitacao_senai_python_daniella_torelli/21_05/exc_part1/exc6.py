import csv
from collections import defaultdict

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)

    contagem = defaultdict(int)

    for line in reader:
        json = dict(zip(header, line))
        produto = json['produto']
        contagem[produto] += 1 

print(dict(contagem))
