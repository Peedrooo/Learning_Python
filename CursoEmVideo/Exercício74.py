from random import sample
from time import sleep
maior = menor = 0

numeros = sample(range(0,50),5)
print(f'Os valores sorteados foram: ',end='')

for c in range (0,len(numeros)):

    print(numeros[c], end=' ')
    if maior < numeros[c]:
        maior = numeros[c]
    elif menor < numeros[c]:
        menor = numeros[c]

sleep(1)
print(f'\nO maior valor foi {maior} e o menor foi {menor}')