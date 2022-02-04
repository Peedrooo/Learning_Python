def e_primo(entrada):
    if entrada == 1: return False
    else:
        for v in range(2,entrada):
            if entrada % v == 0:
                return False
        return True


def gemeos(entrada):
    gemos_primos = []
    aux1,aux2,cont = 0,1,3

    while cont < entrada:
        while True:
            aux1,aux2 = aux1+2,aux2+2
            if e_primo(aux1) and e_primo(aux2):
                if aux1 + 2 == aux2:
                    gemos_primos.append((aux1,aux2))
                    break
        cont += 1
    return gemos_primos
