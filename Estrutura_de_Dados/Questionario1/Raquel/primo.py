def e_primos(entrada):
    if entrada == 1:return False
    else:
        for v in range(2, entrada):
            if entrada % v == 0:
                return False
        return True

def primos_gemeos(entrada):
    gemeos = []
    cont, p1, p2 = 0, 1, 3

    while cont < entrada:
        while True:
            p1, p2 = p1 + 2, p2 + 2
            if e_primos(p1) and e_primos(p2):
                if p1 + 2 == p2:
                    gemeos.append(tuple((p1, p2)))
                    break
        cont += 1
    return gemeos


print(primos_gemeos(2))
