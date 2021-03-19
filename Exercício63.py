print('Programa FIBONACCI')

Fn = int(input('Qual número gostaria de escolher para ver sua sequência? '))
q = int(input('Quantos termos gostaria de ver? '))


if Fn == 1 or Fn == 0:
    print('1')
    
cont = 0
while cont < q:
    cont += 1

    Fn += Fn - 1

    print(Fn, end = ' ')

