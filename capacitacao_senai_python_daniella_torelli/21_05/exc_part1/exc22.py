import csv
from datetime import date, datetime, timedelta, time


with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    hoje = datetime.today()

    for line in reader:
        json = dict(zip(header, line))

        diferenca = hoje - datetime.strptime(json['data'], '%Y-%m-%d')
        print(diferenca)

