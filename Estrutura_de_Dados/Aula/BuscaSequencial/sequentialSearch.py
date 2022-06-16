def sequentialSearch(lista, item):
    for e in lista:
        if e == item:
            return True
        
    return False


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print('dsf')
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))