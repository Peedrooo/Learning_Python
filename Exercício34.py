print('Programa salário '.upper())
sal = int(input('Qual o seu salário atual? '))
if sal > 1250:
    print(f'Com aumento seu salário irá para: R${sal + sal * 10 / 100} reais')
else:
    print(f'Com aumento seu salário irá para: R${sal + sal * 15 / 100} reais')
