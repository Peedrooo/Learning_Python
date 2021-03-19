print('PROGRAMA ATLETA')
from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
print(f'Idade: {idade}')
if idade <= 9:
    print('Atleta classificado como MIRIM')
elif idade <= 14:
    print('Atleta classificado como INFANTIL')
elif idade <= 19:
    print('Atleta classificado como JÚNIOR')
elif idade <= 25:
    print('Atleta classificado como SENIOR')
else:
    print('Atleta classificado como MASTER')
