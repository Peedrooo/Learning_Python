print('SOMA DE MULTIPLOS DE 3')
soma = 0
for x in range (1,500):
    if x % 2 != 0:
        if x % 3 == 0:
            soma += x
print(soma) 

multiplo = 0
for x in range (3,500,3):
    print('.', end=' ')
    if x % 2 != 0:
        multiplo += x
        print(x)

print(multiplo)