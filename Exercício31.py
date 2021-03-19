print('PROGRAMA PREÇO VIAGEM')
dist = int(input('Digite a distancia que pretende percorrer em km: '))
print(f'Distância selecionada: {dist}')
if dist > 200:
    print(f'''Custo de viagem: R${dist*0.45} reais
    Preço posto para viagens acima de 200km''')
else:
    print(f'''Custo de viagem: R${dist*0.75} reais
    Preço posto para viagens menores ou equivalentes à 200km''') 