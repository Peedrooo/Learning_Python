# valor que mais se repete em uma string

"""
def frequencia(string):
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    maior = 0
    for i in dic:
        if dic[i] > maior:
            maior = dic[i]
            letra = i
    return letra

"""

def frequencia(string):
    maior = 0
    try:
        for i in string:  
            valor_atual = string.count(i)   
            if valor_atual  > maior:
                maior = valor_atual
                letra = i
        return letra
    except:
        return ''

print(frequencia(''))
