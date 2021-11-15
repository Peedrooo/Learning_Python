print('JOKEMPÔ')
from random import choice
from time import sleep

print('''[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA''')
escolha = int(input('Qual a sua jogada? '))


if escolha == 1:
    esco = 'Pedra'
elif escolha == 2:
    esco = 'Papel'
elif escolha == 3:
    esco = 'Tesoura'
else:
    print('OPÇÃO INVALIDA')

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')
sleep(0.5)

lista = ['Pedra' , 'Papel' , 'Tesoura']
pc = choice( lista )


if pc == esco:
    print('EMPATE')
else:
    if pc == 'Tesoura' and esco == 'Papel' or pc == 'Papel' and esco == 'Pedra' or pc == 'Pedra' and esco == 'Tesoura':
        print('A MAQUINA GANHOU MEU COLEGA, THE CRY IS FREE')
        print(f'Eu havia escolhido {pc} e vc perdeu escolhendo {esco}')
    else:
        print('Parabéns vc ganhou, nossa como ele é incrivel') 
        print(f'Eu havia escolhido {pc} e vc {esco}')
