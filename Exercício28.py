print('PROGRAMA ADIVINHAÇÃO')
from time import sleep
from random import randint
num = randint(0,5)
user = int(input('Pensei em um número entre 0 e 5, tente adivinhar qual foi... '))
print('PROCESSANDO...')
sleep(2)
if user == num:
    print(f'Parabens vc acertou, escolhi o número {num} e voce tbm')
else:
    print(f'Erou meu colega, eu havia pensado no número {num}')
print('FIM DE JOGO')
