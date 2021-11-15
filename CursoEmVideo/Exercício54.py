print('PROGRAMA MAIOR IDADE')
from datetime import date
idade = []

for x in range (1,9):
    idade.append(int(input(f'Qual o ano de nascimento do {x}º indivíduo ')))

maior = 0
menor = 0

for x in range (0,len(idade)):
    if date.today().year - idade[x] >= 18:
        maior += 1
    else:
        menor += 1
print(f'{menor} indivíduos são menores de idade')
print(f'{maior} indivíduos são maiores de idade')
