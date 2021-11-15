print('PROGRAMA PA')
inicio = int(input('Qual o primeiro termo da PA? '))
ra = int(input('Qual a razão da PA? '))

c = inicio
while c <= (inicio + ( 10 ) * ra):
    c += ra
    print(c, end = ' ')





'''for c in range (inicio,inicio + ( 10 ) * ra , ra):
    print(c, end = ' ')'''