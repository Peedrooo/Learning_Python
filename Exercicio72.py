numero  = int(input('Escolha um número de 0-10 '))
extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while 0 < numero > 10:
    numero(int(input('[ERRO] Tente novamente! Escolha um novo número ')))

print(f'{numero} por extenso é {extenso[numero]}')
