def aumentar(valor):
    total = valor + valor * 10/100
    return total

def diminuir(valor):
    total = valor - valor * 13/100
    return total

def dobro(valor):
    total = valor * 2
    return total

def metade(valor):       
    total = valor / 2       
    return total

def moeda(valor):
    return 'R$ {:.2f}'.format(valor)