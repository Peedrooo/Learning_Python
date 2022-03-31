from queue import Queue
from math import floor

m,n = map(int,input().split())
valores = list(map(int,input().split()))

inicio = 0
aux = n 
while aux < m+1:
    
    print(floor(sum(valores[inicio:aux])/n))
    
    inicio += 1
    aux += 1

'''

movel = Queue()
for v in valores: movel.enqueue(v)

ind = 0
aux = n-1
#while True:
# print(floor(sum(movel.show()[ind:aux])/n))
print(movel.show())
ind += 1
aux += 1'''

