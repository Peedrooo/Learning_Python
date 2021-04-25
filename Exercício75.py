numero1 = int(input('valor 1 '))
numero2 = int(input('valor 2 '))
numero3 = int(input('valor 3 '))
numero4 = int(input('valor 4 '))
cont = 0
tupla = numero1, numero2, numero3, numero4

for c in range(0,len(tupla)):
    if tupla[c] == '9':
        cont += 1
        print(cont)
    print (tupla[c])


