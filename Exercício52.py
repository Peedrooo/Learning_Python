print('PROGRAMA NÚMEROS PRIMOS')
num = int(input('Escolha um número para verificar se ele é primo '))
divisivel = []
for c in range (1,num + 1):
    if num != c :
        if num / c % 2 == 0:
            divisivel.append(c)
        else:
            print('Número PRIMO')
            break   
    elif num == 1:
        print('Número COMUM')
    else:
        print('Entrada invalida')
        break        
print(divisivel)