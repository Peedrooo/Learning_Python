print('CONDIÇÃO DE TRIANGULOS E CLASSIFICAÇÃO DE TRIANGULOS')
reta = []
tipo = []
for c in range (1,4):
    reta.append(int(input(f'Qual a medida da {c}º reta? ')))

reta.sort()


if reta[0] + reta[1] > reta [2] :
    print('Condição para triangulo satisfeita')
    print('ANALIZANDO TIPO DE TRIANGULO...')

    if reta[0] == reta[1] == reta[2]:
        print('Triangulo EQUILÁTERO')

    elif reta[0] != reta[1] != reta[2] != reta[0]:
        print('Triangulo ESCALENO')
    
    else: 
        print('Triangulo ISÓCELES')
else:
    print('Medidas insuficientes para formar um triangulo')
