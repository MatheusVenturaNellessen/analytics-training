import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    for line in reader:
        json = dict(zip(header, line))
        print(f'Produto: {json['produto']} | Preço: {json['preco']}')
