print('PROGRAM PAGAMENTOS')
valor = float (input('Qual o valor da compra? '))
print('''[1] A VISTA NO DINHEIRO
[2] A VISTA NO CARTÃO
[3] EM 2X NO CARTÃO
[4] EM 3X OU MAIS NO CATÃO''')
pagamento = int(input('Qual a maneira de pagamento? '))
if pagamento == 1:
    print(f'''Realizando o pagamento a vista no dinheiro terá um desconto de 10%, \npassado de R${valor:.2f} para R${valor - valor * 1 / 10:.2f}''')
elif pagamento == 2:
    print(f'''Pagando a vista no cartão, terá um desconto de 5%, \npassando de R${valor:.2f} para R${valor - valor * 5 / 100:.2f}''')
elif pagamento == 3:    
    print(f'''Pagando em duas vezes no cartão o preço cobrado será o mesmo,\ncada parcela sairá por R${valor/2:.2f}, totalizando R${valor:.2f} no final''')
else:
    vezes = int(input('Em quantas vezes gostaria de realizar o pagamento? '))
    print(f'''Sua compra será realizada em {vezes}x de R${(valor + valor * 20 /100)/vezes} COM JUROS,\nsaindo de R${valor} por R${valor + valor * 20 /100} no final''')
