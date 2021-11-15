escolha = []
select = int(input('Escolha um número '))

print('Certo, primeiro número adicionado \nPara cancelar a adição basta digitar 999')

while select != 999:
    escolha.append(select)
    select = int(input('Mais um '))


print(f'{len(escolha)} números foram escolhidos, \nSendo eles: {escolha}, \na soma entre eles resulta em: {sum(escolha)}')