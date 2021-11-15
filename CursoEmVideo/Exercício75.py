numero1 = int(input('valor 1 '))
numero2 = int(input('valor 2 '))
numero3 = int(input('valor 3 '))
numero4 = int(input('valor 4 '))
nov = par = 0
tupla = numero1, numero2, numero3, numero4

for c in range(0,len(tupla)):
    if tupla[c] %2 == 0:
        par+=1
print(f'O número nove apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    tres = tupla.index(3)
    print(f'O valor tres apareceu pela primeira vez na posição {tres+1}')
else:
    print('O número 3 não apareceu')

print(f'Temos {par} valores pares, sendo eles: ',end='')

for c in range(0,len(tupla)):
    if tupla[c] %2 == 0:
        par+=1
        print(tupla[c],end = ' ')



    


