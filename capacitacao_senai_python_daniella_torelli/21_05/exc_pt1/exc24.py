import csv
from datetime import datetime
from collections import defaultdict

counter = defaultdict(int)

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_pt1/vendas.csv', mode='r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)

    for line in reader:
        order = dict(zip(header, line))

        data = datetime.strptime(order['data'], '%Y-%m-%d')

        counter[data.month] += 1
        
print(counter)
print(sorted(counter))


for month in sorted(counter):
    print(f"Mês {month}: {counter[month]} vendas")
