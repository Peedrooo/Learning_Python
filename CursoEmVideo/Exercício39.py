print('PROGRAMA ALISTAMENTO')
from datetime import date
year = (date.today().year)
sexo = input('Qual o seu sexo? ').upper().strip()
if sexo[0] == 'M':
    ano=int(input('Qual o ano do seu nascimento? '))
    idade = year - ano
    if idade == 18:
        print(f'Quem nasceu em {ano} tem {idade} anos no ano atual: {year}.\nPortanto deve se alista IMEDIATAMENTE')
    elif idade < 18:
        print(f'''Quem nasceu em {ano} tem {idade} anos no ano atual: {year}.\nRestando { 18 - idade} anos para o seu alistamento
        Alistamento previsto para o ano de {year + idade - 18}''')
    else:
        print(f'''Quem nasceu em {ano} tem {idade} anos no ano atual: {year}.\nDeveria ter se alistado há {idade - 18} anos em {year - (idade - 18)}''')
else:
    print('Por ser mulher o alistamento não é obrigratório !!!')