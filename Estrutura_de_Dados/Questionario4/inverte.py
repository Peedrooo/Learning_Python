def inverte(S, tamanho = 0):
    if tamanho == 0:
        tamanho = len(S)
    if tamanho == 1:
        return S
    else:
        return inverte(S[1:], tamanho-1) + S[0]
    
print(inverte('lamina'))