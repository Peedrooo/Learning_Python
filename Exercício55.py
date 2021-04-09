print('PROGRAMA PESOS')
peso = []
for d in range(1,6):
    peso.append(float(input(f'Qual o peso do {d}º indivíduo? ')))
print(f'O maior peso lido foi de {max(peso):.2f}, já o menor de {min(peso):.2f}')

