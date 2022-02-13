import time, random, string


def len01(palavra):
    resposta = 0
    for _ in palavra:
        resposta += 1
    return resposta

def len02(palavra):
    return len(palavra)

lista = []

for c in range (10):
    lista.append(random.choice(string.ascii_letters))
    
print(lista)

'''

start = time.time()

for c in range(100):
    len01(lista)

end = time.time()

print(end - start)
'''


