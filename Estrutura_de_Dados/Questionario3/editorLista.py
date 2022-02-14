# Editor de Listas I

lista_valores = []

while True:

    instrucao = input().split()

    if instrucao[0] == 'X':
        for e in lista_valores:
            print(e)
        break
    
    elif instrucao[0] == 'D':
        print(lista_valores.pop(0))

    elif instrucao[0] == 'P':
        print(lista_valores.pop())


    else: 
        
        comando, valor = instrucao

        if comando == 'I':
            lista_valores.insert(0,valor)

        elif comando == 'F':
            lista_valores.append(valor)

        elif comando == 'P':
            lista_valores
        


