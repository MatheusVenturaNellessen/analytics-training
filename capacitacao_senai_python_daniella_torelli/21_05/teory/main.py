# How to read .csv files 
import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_example/vendas.csv', mode='r', encoding="utf-8", newline='') as f:
    reader = csv.reader(f, delimiter=',')

    header = next(reader)

    for line in reader:
        json = dict(zip(header, line))

        print(f"Data: {json['data']} | Produto: {json['produto']} | Quantidade: {json['quantidade']} | Preço: {json['preco']}")



# Defaultdict - example 1
from collections import defaultdict

vendas_tuplas = [('camisa',3), ('calça',2), ('camisa',1)]

soma = defaultdict(int) 

for prod, qtd in vendas_tuplas:
    soma[prod] += qtd 

print(soma)

# Example 2
pedidos = [
    ('Ana',    'camisa'),
    ('Bruno',  'calça'),
    ('Ana',    'boné'),
    ('Ana',    'chinelo'),
    ('Ana',    'vestido'),
    ('Bruno',    'camisa')
]

agrupado = defaultdict(list)

for cliente, produto in pedidos:
    agrupado[cliente].append(produto)

print(dict(agrupado))


# Working with dates
from datetime import date, datetime, timedelta, time

hoje = date.today()
print(f'Data de hoje: {hoje}')

aniversario = date(2001, 8, 11)
print(f'Meu aniversário: {aniversario}')

agora = datetime.now()
print(f'Data de agora: {agora}')

#                    yyyy mm  dd  mm  ss ms
dt_evento = datetime(2025, 8, 11, 12, 30, 0)
print(f'Data do evento (meu aniversário): {dt_evento}')



texto = "2025-05-20 14:30"
formato = "%Y-%m-%d %H:%M"
dt = datetime.strptime(texto, formato) # strptime == "string parse time"
print(dt)

hoje = date.today()
# formata como "dd/mm/yyyy"
print(hoje)
print(hoje.strftime("%d/%m/%Y")) # strftime == "string format time"


agora = datetime.now()
# formata como "dd-nn-yyyy hh:mm"
print(agora)
print(agora.strftime("%d-%m-%Y %H:%M"))



dia = timedelta(days=1)
horas = timedelta(hours=7,minutes=15,seconds=45)
print(dia,horas)

amanha = hoje + dia
anteontem = hoje - timedelta(days=2)
print("Amanhã:", amanha)
print("Anteontem:", anteontem)



inicio = datetime(2025,5,21,9,0)
fim    = datetime(2025,5,21,16,0)
duracao = fim - inicio
print(duracao)                
print(duracao.total_seconds())
