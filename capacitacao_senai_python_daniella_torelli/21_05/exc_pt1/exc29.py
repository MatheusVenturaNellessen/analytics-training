import csv 
from datetime import date, datetime, timedelta

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_pt1/vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)

    today = datetime.today()

    for line in reader:
        order = dict(zip(header, line))

        date = datetime.strptime(order['data'], '%Y-%m-%d')

        if (today - date) <= timedelta(days = 90) and (today - date) > timedelta(days = 1):
            print(f'A venda: {order} foi efetuada há {(today - date).days} dias, portanto possui garantia.')
