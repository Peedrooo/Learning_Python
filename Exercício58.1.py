print('PROGRAMA ADIVINHAÇÃO')
from time import sleep
from random import randint
num = randint(0,10)
user = int(input('Pensei em um número entre 0 e 10, tente adivinhar qual foi... '))
print('PROCESSANDO...')
sleep(1)
cont = 1
while user != num:
    cont += 1
    if cont != 2:
        print('PROCESSANDO...')
        sleep(1)
    print(f'Erou meu colega kkkk')
    user = int(input('Tenta escolher mais um aí.. '))

if cont > 1:
    print(f'BOAAA, Com {cont} tentativas vc acertou o número {num}')
else: print('Resga, de primeira tu acertou o número',num)
print('FIM DE JOGO')
