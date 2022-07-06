class Queue:    
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def first(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def show(self):
        return self.items

fila = Queue()
caracteres = input()
saida = ''
for e in caracteres:
    if e == '*':
        saida = saida + str(fila.dequeue())
    else:
        fila.enqueue(e)

print(saida)