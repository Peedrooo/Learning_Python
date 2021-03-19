print('PROGRAMA MENU')
escolha = 0
while escolha != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Finalizar programa''')
    num = int(input('Escolha um número '))
    num2 = int(input('Mais um '))
    escolha = int(input('Como deseja proseguir com os número? '))

    if escolha == 1:
        print(f'A soma entre {num} e {num2} recebe {num + num2}')


    elif escolha == 2:
        print(f'A multiplicação entre {num} e {num2} temos {num * num2}')


    elif escolha == 3:

        if num > num2:
            print(f'O número {num} é maior {num2}')

        if num2 > num:
            print(f'O número {num2} é maior {num}')

        else:
            print('Os número são iguais')

    elif escolha == 4:
        num = int(input('Escolha um número '))
        num2 = int(input('Mais um '))
    
    else:
        print('Opção escolhida não cadastrada')
