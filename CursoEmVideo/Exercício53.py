print('VERIFICADOR DE PALINDROMOS')

frase = input('Digite uma frase ').upper().strip().split()
frase = ''.join(frase)


lista = []
for c in range (0,len(frase)):
    lista.append(frase[c])
lista.reverse()
lista = ''.join(lista)


if lista == frase:
    print('Temos um palíndromo')
else:
    print(f'O inverso de {frase} é {lista}, ou seja não se trata de um palídromo')
