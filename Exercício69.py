cont = homem = mulher = maior = 0
genero = 'Nan'
while True:
    cont += 1
    idade = []
    old = (int(input(f'Digite a idade do cadidato {cont} ')))
    idade.append(old)
    if old >= 18:
        maior += 1
    
    while genero != 'H' and genero != 'M':
        genero = input('Qual o sexo? [H/M] ').upper().strip()[0]
        print(genero)

    if genero == 'H':
        homem += 1
    elif genero == 'M' and idade[1 - cont] < 20:
        mulher += 1

    while user != 'S' and user != 'N':
        user = input('Gostaria de continuar os cadastros ? [S/N]').upper().strip()[0]
        if user == 'N':
            break

print(f'Temos: \n{maior} pessoas maiores de idade. \n{homem} homens cadastrados. \n{mulher} com menos de 20 anos')

