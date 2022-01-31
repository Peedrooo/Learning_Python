def decrescente(*num):
    valores = list(map(int,num))
    valores.sort(reverse=True)
    return tuple(valores)

print(decrescente(2, 21, 2))


