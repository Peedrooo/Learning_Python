print('CALCULO FATORIAL ')
from numpy import prod
num = int(input('Escolha um número para ver o seu calculo fatorial '))
numeros = []

escolha = num

while num > 0:
    numeros.append(num)
    num = (num - 1)

print(f'O fatoria de {escolha} é {prod(numeros)}')

print(f'Os termos são {numeros}')
