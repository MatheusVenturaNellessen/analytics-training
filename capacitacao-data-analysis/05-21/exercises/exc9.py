import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    minor = 9999999999
    major = -9999999999 

    for line in reader:
        json = dict(zip(header, line))

        if int(json['quantidade']) <= minor:
            minor = int(json['quantidade'])
        if int(json['quantidade']) >= major:
            major = int(json['quantidade'])

print(f'Menor quantidade: {minor}')
print(f'Maior quantidade: {major}')
