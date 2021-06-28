from random import randint
from time import sleep

numeros = []

def sorteia():
    qnt = randint(0,10)
    print(f"Sorteando {qnt} números: ", end = '', flush = True)
    for c in range(qnt):
        numeros.append(randint(0,10))
        print(numeros[c], end= ' ')
    print()


def somapar(numeros):
    print(f"Somando os valores pares de {numeros}, temos :", end=' ',flush = True)
    soma = 0
    for v in numeros:
        if v%2 == 0:
            soma += v
    print(soma)

sorteia()
somapar(numeros)
