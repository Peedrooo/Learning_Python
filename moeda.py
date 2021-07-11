def aumentar(valor,Conversão = True):
    total = valor + valor * 10/100
    if Conversão:       
        return 'R$ {:.2f}'.format(total)
    else:
        return (total)

def diminuir(valor,Conversão = True):
    total = valor - valor * 13/100
    if Conversão:       
        return 'R$ {:.2f}'.format(total)
    else:
        return (total)

def dobro(valor,Conversão = True):
    total = valor * 2
    if Conversão:       
        return 'R$ {:.2f}'.format(total)
    else:
        return (total)

def metade(valor,Conversão = True):       
    total = valor / 2
    if Conversão:       
        return 'R$ {:.2f}'.format(total)
    else:
        return (total)

def moeda(valor,Conversão = True):
    if Conversão:
        return 'R$ {:.2f}'.format(valor)
    else:
        return (valor)
