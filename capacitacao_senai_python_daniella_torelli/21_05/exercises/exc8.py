import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    counter = 0
    adder = 0

    for line in reader:
        counter += 1
        
        json = dict(zip(header, line))

        adder += float(json['preco'])
    
average = adder / counter

print(f'R$ {round(average, 2)}')
