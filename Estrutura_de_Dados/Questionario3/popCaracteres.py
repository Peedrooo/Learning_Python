from stack import Stack

pilha = Stack()
caracteres = input()
saida = ''
for e in caracteres:
    if e == '*':
        saida = saida + str(pilha.pop())
    else:
        pilha.push(e)

print(saida)



