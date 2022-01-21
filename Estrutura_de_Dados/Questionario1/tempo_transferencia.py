# path tempo de transferência restante

from time import sleep

while True:
    total_bytes = int(input())
    print(f'Transmitindo {total_bytes} bytes...')

    while total_bytes > 0:
        frequencia = int(input())

        if frequencia == 0:
            print('Tempo restante: pendente...')
            sleep(5)
        else:
            total_bytes -= frequencia
            print(f'Tempo restante: {round()} segundos.')
            sleep(5)


