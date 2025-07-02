import csv 
from datetime import datetime

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_pt1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    sells_may = []

    for line in reader:
        order = dict(zip(header, line))

        date = datetime.strptime(order['data'], '%Y-%m-%d')

        if date.month == 5:
            sells_may.append(order)

for i in range(len(sells_may)):
    print(sells_may[i])
