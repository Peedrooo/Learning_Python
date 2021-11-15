def linha():
    print('=='*20)
    return()
cem = cinq = vint = dez = cinc = dois = um = 0

linha()
print('BANCO CEV')
linha()
valor = int(input('Qual valor gostaria de sacar? '))
while True:

    while True:
        if valor - 100 >= 0:
            cem +=1
            valor -= 100
        else:
            break

    while True:
        if valor - 50 >= 0:
            cinq +=1
            valor -= 50
        else:
            break

    while True:
        if valor - 20 >= 0:
            vint +=1
            valor -= 20
        else:
            break

    while True:
        if valor - 10 >= 0:
            dez +=1
            valor -= 10
        else:
            break

    while True:
        if valor - 5 >= 0:
            cinc +=1
            valor -= 5
        else:
            break
    
    while True:
        if valor - 2 >= 0:
            dois +=1
            valor -= 2
        else:
            break

    while True:
        if valor - 1 >= 0:
            um +=1
            valor -= 1
        else:
            break

    if valor == 0:
        break


if cem > 0:
    print (f'Total de {cem} cédulas de R$100')

if cinq > 0:
    print(f'Total de {cinq} cédulas de R$50')

if dez > 0:
    print(f'Total de {vint} cédulas de R$20')

if cinc > 0:
    print(f'Total de {cinc} cédulas de R$5')

if dois >0:
    print(f'Total de {dois} cédulas de R$2')

if um > 0:
    print(f'Total de {um} cédulas de R$1')


'''
print(f'Total de {cem} cédulas de R$100
Total de {cinq} cédulas de R$50
Total de {vint} cédulas de R$20
Total de {dez} cédulas de R$10
Total de {cinc} cédulas de R$5
Total de {dois} cédulas de R$2
Total de {um} cédulas de R$1')
'''


linha()

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')