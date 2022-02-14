from queue import Queue

fila = Queue()

for i in input().split(): fila.enqueue(i)

for x in range(int(input())): 
    fila.enqueue(fila.dequeue())
    
print('Pessoa da frente:',fila.dequeue())
print('Pessoa do fim:',fila.first())