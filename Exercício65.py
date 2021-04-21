print('PROGRAMA VALORES')

escolha = int(input('Qual valor gostaria de adicionar '))
continuacao = input('Gostaria de continuar? [S/N] ')

valores = []

while continuacao != 'N':
    valores.append(escolha)
    escolha = int(input('Qual valor gostaria de adicionar '))
    valores.append(escolha)
    continuacao = input(('Gostaria de continuar? [S/N] ')).upper().strip()[0]

print(f'Os valores escolhidos foram: {valores}, \nO maior é o {max(valores)},\nO menor é o {min(valores)}, \nA média é de {sum(valores)/len(valores)}')