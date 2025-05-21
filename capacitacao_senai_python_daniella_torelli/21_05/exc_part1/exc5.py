import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    for line in reader:
        json = dict(zip(header, line))

        print(f'Valor da venda: Produto: {json['produto']} | Quantidade: {float(json['quantidade'])} | Valor: {float(json['preco'])} | Total: {float(json['quantidade']) * float(json['preco'])}')