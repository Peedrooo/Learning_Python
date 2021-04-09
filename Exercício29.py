print('PROGRAMA MULTA')
velo = float (input('Qual a velocidade do veículo? '))
if velo > 80:
    print('Limite de velocidade excedido'.upper())
    print(f'Uma multa de R${(velo-80)*7}será aplicada!!!')
else:
    print('''Velocidade dentro do limite, veículo liberado !!
    A equipe de TI deseja uma boa viagem :)''')
    