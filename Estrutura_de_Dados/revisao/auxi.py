import time

num_testes = 5
media = 0

def soma_ate(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

for _ in range(num_testes):
    inicio = time.time()
    soma_ate(10000)
    fim = time.time()
    
    tempo_de_execucao = fim - inicio
    media += tempo_de_execucao
    print(f'Tempo: {tempo_de_execucao}')

media /= num_testes
print(f'Média de tempo: {media}')