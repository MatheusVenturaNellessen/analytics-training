import csv
from datetime import date, datetime, timedelta, time


with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    today = datetime.today()

    flag = timedelta(days=30)

    for line in reader:
        json = dict(zip(header, line))

        difference = today - datetime.strptime(json['data'], '%Y-%m-%d')
        
        if difference < flag:
            print(f'Data: {difference}: {json}')
