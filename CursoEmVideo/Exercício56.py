print('PROGRAMA FINAL FOR ANALISADOR COMPLETO')

for x in range (1,5):
    (x) = []
    str(x)
    x.append(input('Qual o nome do indivíduo '))
    x.append(int(input(f'Qual a idade do(a) {x[0]} indivíduo? ')))
    print('''[ M ] para MASCULINO
[ F ] para FEMININO''')
    x.append(str(input('Qual o sexo ? digite de acordo com a tabela acima!! ')).strip().upper())
    print(x)


idade_m = []
for x in range (1,5):
    if x[2] == 'M':
        idade_m.append(x[1])

mulher = 0
for x in range (1,5):
    if x[2] == 'F':
        if x[1] < 20:
            mulher += 1
print(f'{mulher} mulheres abaixo de 20 anos foram cadastradas')


for x in range (1,5):
    if x[2] == 'M':
        if x[1] == (max(idade_m)):
            print(f'{x[0]} é o homem que possui mais idade')
            break

total = 0
for x in range (1,5):
    total += x[1]
media = total/4
print(f'A media de idade do grupo todo é de {media}')


