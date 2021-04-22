from random import randint
print('Vamos jogar par ou impar')
vitorias = 0
def linha():
    print('--'*30)
    return

while True:
    pc = randint(0,10)
    escolha = int(input("Qual valor voce escolhe? ")) 
    paridade = input('Par ou Ímpar? [P/I]').upper().strip()[0]
    linha()
    soma = escolha + pc

    if soma % 2 == 0 :
        resul = 'PAR'
    else:
        resul = 'IMPAR'

    
    print(f'Voce jogou {escolha} e o computador {pc}. Total: {soma}. Deu {resul}')
    linha()

    if paridade == resul.strip()[0]:
        vitorias += 1
        print('YOU WINNNN')
        print('Mais uma...')
    else:
        print('LOSERR')
        linha()
        print(f'GAME OVER! você venceu {vitorias} vezes')
        break