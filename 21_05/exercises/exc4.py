import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    adder = 0
    
    for line in reader:

        aux = dict(zip(header, line))

        adder += float(aux['preco'])
        
print(adder)
