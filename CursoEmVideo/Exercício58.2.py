print('PROGRAMA ADIVINHAÇÃO')
from time import sleep
from random import randint
nov = "S"
while nov == "S":
    num = randint(0,10)
    user = int(input('Pensei em um número entre 0 e 10, tente adivinhar qual foi... '))
    print('PROCESSANDO...')
    sleep(1)
    cont = 1
    

    while user != num:
        cont += 1
        
        if user > num: 
            user = int(input('Menos.. Tenta escolher mais um aí.. '))
        elif user < num:
            user = int(input('Mais.. Tenta escolher mais um aí.. '))
      
        print('PROCESSANDO...')
        sleep(1)
                   
    if cont > 1:
        print(f'BOAAA, Com {cont} tentativas vc acertou o número {num}')
    else: print('Resga, de primeira tu acertou o número',num)

    print('FIM DE JOGO')
    escolha = (input('Gostaria de jogar novamente? [S/N]')).upper()
    nov = escolha[0]
    
print('Programa finalizado')