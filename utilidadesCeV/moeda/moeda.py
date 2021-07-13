def aumentar(valor,Conversão = True):
    total = valor + valor * 10/100
    if Conversão:       
        return ('R$ {:.2f}'.format(total))
    else:
        return (total)

def diminuir(valor,Conversão = True):
    total = valor - valor * 13/100
    if Conversão:       
        return ('R$ {:.2f}'.format(total))
    else:
        return (total)

def dobro(valor,Conversão = True):
    total = valor * 2
    if Conversão:       
        return ('R$ {:.2f}'.format(total))
    else:
        return (total)

def metade(valor,Conversão = True):       
    total = valor / 2
    if Conversão:       
        return ('R$ {:.2f}'.format(total))
    else:
        return (total)

def moeda(valor,Conversão = True):
    if Conversão:
        return ('R$ {:.2f}'.format(valor))
    else:
        return (valor)
def linha():
    print("-="*16)

def resumo(valor,au=10,red=5):
    linha()
    print("RESUMO DO VALOR".center(16))
    linha()
    print(f'Valor analisado:   R${valor:.2f}')
    print(f'Dobro do preço:    R${valor*2:.2f}')
    print(f'Metade do preço:   R${valor/2:.2f}')
    print(f'{au}% de aumento:    R${valor + valor*(au/100):.2f}')
    print(f'{red}% do redução:   R${valor - valor*(red/100):.2f}')
    linha()