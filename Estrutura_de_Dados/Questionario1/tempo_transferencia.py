# path tempo de transferência restante

from math import ceil


total_bytes = int(input().strip())
print(f'Transmitindo {total_bytes} bytes...')

tempo = 0
while True:
    tempo +=1
    transferencia = int(input())
    total_bytes -= transferencia
    if total_bytes <= 0:
        break
    if tempo % 5 == 0:
        if transferencia == 0:
            print('Tempo restante: pendente...')
        else:
            print(f'Tempo restante: {ceil(total_bytes/transferencia)} segundos.')
print(f'Tempo total: {tempo} segundos.')


 