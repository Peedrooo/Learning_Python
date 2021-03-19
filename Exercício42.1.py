print('CONDIÇÃO DE TRIANGULOS E CLASSIFICAÇÃO DE TRIANGULOS')
reta = []
tipo = []
for c in range (1,4):
    reta.append(int(input(f'Qual a medida da {c}º reta? ')))

reta.sort()


if reta[0] + reta[1] > reta [2] :
    print('Condição para triangulo satisfeita')
    print('ANALIZANDO TIPO DE TRIANGULO...')

    for valor in reta:
        tipo.append(reta.count(valor))

    lados_semelhantes = max(tipo)   


    if lados_semelhantes == 3:
        print('Triangulo do tipo EQUILÁTERO')

    elif lados_semelhantes == 2:
            print('Triangulo ISÓSCELES')       

    else:
        print('Triangulo ESCALENO')

else:
    print('Medidas insuficientes para formar um triangulo')


