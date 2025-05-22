# Calcule a média de dias entre as vendas de um mesmo produto

import csv 
from datetime import datetime
from collections import defaultdict

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_pt1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    product_days = defaultdict(list)

    for line in reader:
        order = dict(zip(header, line))
        date = datetime.strptime(order['data'], '%Y-%m-%d')
        product_days[order['produto']].append(date)

# A partir deste ponto, foi necessário ajuda de IA
for product, dates in product_days.items():
    if len(dates) < 2:
        print(f"{product}: Apenas uma venda, média não calculada.")
        continue

    dates.sort()  
    diference = []

    for i in range(1, len(dates)):
        diff = (dates[i] - dates[i - 1]).days
        diference.append(diff)

    average = sum(diference) / len(diference)
    print(f"{product}: média de {average:.2f} dias entre vendas")

# Até calcular a média, consegui sozinho, mas depois foi necessário ajuda de IA