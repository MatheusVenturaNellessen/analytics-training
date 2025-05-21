# O algorítimo possui um bug onde, ao usar a flag 'w', o arquivo new é apagado e escrito novamente, resultando em somente uma linha. 

import csv

with open('capacitacao_senai_python_daniella_torelli/21_05/exc_part1/vendas.csv', mode='r', encoding='utf-8', newline='') as original:
    reader = csv.reader(original, delimiter=',')
    
    header = next(reader)

    for line in reader:
        json = dict(zip(header, line))

        if float(json['preco']) > 100:
            with open('C:/Users/mathe/Documentos/Development/tcs-workspace/capacitacao_senai_python_daniella_torelli/21_05/exc_part1/price_above100.csv', mode='a', encoding='utf-8', newline='') as new:

                new.write(','.join(line))
                new.write('\n')
