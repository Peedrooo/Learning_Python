print('PROGRAMA SOMA DE PARES')
soma = 0
for x in range (1,7):
    esc = int(input(f'Escolha o {x}º número '))
    if esc%2 == 0:
        soma += esc

print(f'A soma entre os pares escolhidos resultará em {soma}')
