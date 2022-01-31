def decrescente(num):
    valores = []
    for i in range(len(num)):       
        if num[i].isalnum():
            valores.append(int(num[i]))
    valores.sort(reverse=True)
    return valores

print(decrescente('2, 21, 2'))


