price = list(range(10, 120, 12))

'''
Testando de formas diferentes
'''

control_variable = 0

while control_variable != len(price):
    print(f'R$ {price[control_variable] * 0.9}')
    control_variable += 1
