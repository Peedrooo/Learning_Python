print('PROGRAMA PA')
inicio = int(input('Qual o primeiro termo da PA? '))
ra = int(input('Qual a razão da PA? '))

c = inicio
while c <= (inicio + ( 10 ) * ra):
    c += ra
    print(c, end = ' ')

print('\n',end = '')

print('Quando não quiser adicionar mais números digite 0')

more = int(input('Mais quantos termos gostaria de mostrar? '))

while more > 0:

    while c <= (inicio + ( 10 + more) * (ra)):
        c += ra
        print(c, end = ' ')

    print('\n',end = '')

    add = int(input('Mais quantos termos gostaria de mostrar? '))

    if add == 0 :
        break
    more += add

print('Fim do programa')
 