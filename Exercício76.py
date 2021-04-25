def linha():
    print('-='*20)
    return
produtos = ('Detergente',9,'sabao',2.5,'sorvete',32,'jantinha',14, 'espetinho',17)

linha()
print(f'{"LISTAGEM DE PREÇOS":^40}')
linha()
for itens in range(0,len(produtos),2):
    print(f'{produtos[itens]:.<30}R$ {produtos[itens+1]:.2f}')
linha()