import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    counter = 0

    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    for line in reader:
        counter += 1

print(f'Quantidade de linhas do aquivo vendas.csv: {counter}')