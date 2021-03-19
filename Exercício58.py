print('PROGRAMA ADIVINHAÇÃO')
from time import sleep
from random import randint
num = randint(0,10)
user = int(input('Pensei em um número entre 0 e 10, tente adivinhar qual foi... '))
print('PROCESSANDO...')
sleep(2)
cont = 0
while user != num:
    cont += 1
    print('PROCESSANDO...')
    sleep(2)
    print(f'Erou meu colega kkkk')
    user = int(input('Tenta escolher mais um aí.. '))
print(f'BOAAA, Dps de {cont} tentativas vc acertou o número {num}')
print('FIM DE JOGO')
