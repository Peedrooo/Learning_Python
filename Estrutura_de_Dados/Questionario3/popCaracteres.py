class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] 
        
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)



pilha = Stack()
caracteres = input()
saida = ''
for e in caracteres:
    if e == '*':
        saida = saida + str(pilha.pop())
    else:
        pilha.push(e)
        
print(saida)



