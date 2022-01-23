def palindromo(string):
    qnt = len(string)
    if qnt == 1:
        qnt += 1
    elif qnt %2 == 0:
        if string == string[::-1]:
            return False
    cont = 0
    for c in range(qnt//2):
        if string[c] == string[-c-1]:
            cont += 1
    if cont + 4 - qnt >= 0 and cont > 0:
        return True
    else:
        return False


if palindromo(input()):
    print('POSSÍVEL')
else:
    print('IMPOSSÍVEL')
    
# 0,71 -> necessario refatorar