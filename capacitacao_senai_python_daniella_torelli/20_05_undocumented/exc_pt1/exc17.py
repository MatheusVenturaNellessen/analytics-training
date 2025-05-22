with open('./capacitacao_senai_python_daniella_torelli/20_05/names_fruits.txt', 'r') as f:
    content = f.read()


aux = content.split(' ')
aux.pop()

for i in aux:
    if aux.count(i) > 1:
        aux2 = True

if aux2:
    print('Há duplicatas!')
else:
    print('Não há duplicatas!')

print(f'Frutas em ordem alfabética: {sorted(aux)}.')
    