print('PROGRAMA NÚMEROS PRIMOS')
num = int(input('Escolha um número para verificar se ele é primo '))
divisivel = []
for c in range (1,num+1):
    if num % c == 0:
        divisivel.append(str(c))
total = len(divisivel)

if total > 2:
    divisivel = ', '.join(divisivel)
    print(f'{num} \033[31mNÃO É PRIMO\033[m, pois é divisível por {divisivel}\nOu seja foi divisivel por um total de {total} vezes' )
elif num == 1:
    print(f'\033[31mNÃO É PRIMO\033[m')
else:
    print(f'{num} \033[34mÉ PRIMO\033[m, pois é divisivel apenas por 1 e {num}, ou seja ele mesmo')