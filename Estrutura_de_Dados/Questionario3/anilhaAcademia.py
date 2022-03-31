from stack import Stack
pilha_pesos = Stack()
peso_movimentado = 0
anilha_movimentada = 0 

while True:
    peso = int(input())
    if peso == 0:
        break
    else:
        pilha_pesos.push(peso)

peso_desejado = int(input())

while True:
    anilha_movimentada += 1
    peso_retirado = pilha_pesos.pop()
    peso_movimentado += peso_retirado
    
    print('Peso retirado:',peso_retirado)

    if peso_retirado == peso_desejado:
        break
    
print('Anilhas retiradas:',anilha_movimentada)
print('Peso total movimentado:',peso_movimentado)
