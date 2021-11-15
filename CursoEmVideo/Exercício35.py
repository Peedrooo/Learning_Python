print('CONDIÇÃO DE TRIANGULOS')
reta = []
for c in range (1,4):
    reta.append(int(input(f'Qual a medida da {c}º reta? ')))
reta.sort()
if reta[0] + reta[1] > reta [2] :
    print('Condição para triangulo satisfeita')
else:
    print('Medidas insuficientes para formar um triangulo')
