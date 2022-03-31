from stack import Stack

qnt = int(input())

pilha = Stack()

tempo_total = 0


for c in range(qnt):
    tipo,cor,tempo = input().split()
    tempo_total += int(tempo)
    pilha.push(cor)
    pilha.push(tipo)

for c in range(qnt):
    print(f'Tipo: {pilha.pop()}, Cor: {pilha.pop()}')
    
print('Total de roupas:', qnt)
print('Total de tempo:', tempo_total)