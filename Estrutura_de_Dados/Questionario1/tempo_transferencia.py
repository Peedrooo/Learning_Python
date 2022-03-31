# path tempo de transferência restante

from math import ceil

total_bytes = int(input().strip())
print(f'Transmitindo {total_bytes} bytes...')

tempo = 0
transferencia = []

while True:
    tempo +=1
    transferencia.append(int(input().strip()))
    resta = total_bytes - sum(transferencia)
    if resta == 0:
        break
    if tempo % 5 == 0:
        try:
            media_transferencia = ceil(round(resta/(sum(transferencia[::-1][0:5])/5),3))
            print(f'Tempo restante: {media_transferencia} segundos.')
        except ZeroDivisionError:
            print('Tempo restante: pendente...')
print(f'Tempo total: {tempo} segundos.')


