extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
cont = True
while cont :
    numero  = int(input('Escolha um número de 0-10 '))
    while numero > 10 or numero < 0:
        numero=int(input('[ERRO] Tente novamente! Escolha um novo número '))

    print(f'{numero} por extenso é {extenso[numero]}')

    escolha = input('Gostaria de continuar ? [S/N] ').upper().strip()[0]
    if escolha != 'S':
        cont = False
print('Programa finalizado')