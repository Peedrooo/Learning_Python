print('PROGRAMA SEXO')
sex = input('Qual o seu sexo? ').upper().strip()
while sex[0] != 'M' and sex[0] != 'H' :
    print(sex[0])
    sex = input('Sexo inválido, digite novamente !! ').upper().strip()
print('Sexo cadastrado com sucesso :) ')
