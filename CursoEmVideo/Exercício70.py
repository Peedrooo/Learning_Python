produtos = []
valor = []
cem = 0
c = 'NAN'
while True:
    nome = input('Qual o nome do produto ? ')
    preco = float(input('Qual o valor do produto ? '))
    produtos.append(nome)
    produtos.append(preco)
    while c != 'S' and c != 'N':
        c = input('Gostaria de continuar ? [S/N] ').upper().strip()[0]
    print(produtos)
    if c == 'N':
        break
    c = 'nan'

for x in range(1,len(produtos),2):
    valor.append(produtos[x])
    if produtos[x] >= 100:
        cem+=1

b = produtos.index(min(valor))- 1

print(f'O total gasto será de R${sum(valor)},00\nTeremos {cem} produtos custando mais de R$ 100,00 \nO produto mais barato será o {produtos[b]}, custando R${min(valor)}0')
