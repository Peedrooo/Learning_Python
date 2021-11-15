valores = []
for c in range(0,5):
    
    valor = int(input("Digite um valor "))
    if len(valores) == 0:
        valores.append(valor)
        print("Primeiro valor adicionado")

    elif valor in valores:
        print("Falha ao adicionar número, este já foi cadastrado")

    else:
        maior = max(valores)
        menor = min(valores)
        
        if valor > maior:
            valores.append(valor)
            print("Valor adicionado na ultima posição da lista")
        elif valor < menor:
            valores.insert(0,valor) 
            print("Valor adicionada no início da lista")
        else:
            for c in range(len(valores)):
                if valores[c] < valor < valores [c+1]:
                    valores.insert(c+1,valor)
                    print(f"Valor adicionadona posição {c+1}")

print(f"Os valores digitados em ordem {valores}")
 