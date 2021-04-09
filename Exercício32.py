from datetime import date
print('ANO BISSEXTO')
ano_atual = (date.today().year)
ano = int(input('Qual ano gostaria de analizar?, Se for o ano atual basta digitar 0  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano {ano}, não é bissexto')
