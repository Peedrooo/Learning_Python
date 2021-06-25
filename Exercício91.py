'''
from time import sleep
from random import randint
# from operator import itemgetter

jogadas = {}

for c in range(1,5):
    jogadas[f"jogador{str(c)}"] = (randint(0,6))

print("Valores sorteados: ")
for k,v in jogadas.items():
    print(f" O {k} tirou {v}")
    sleep(0.5)

jogos = {k: v for k, v in sorted(jogadas.items(), key = lambda item: item[1], reverse = True)}


print("Ranking: ")

for e, (k,v) in enumerate (jogos.items()):
    print(f" {e+1}º lugar: {k} com {v}")
    sleep(0.5)
'''
# Resolução Guanabara [com uma pitada de otimização do Pedro :) ]: 
from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
for c in range(1,5):
    jogo[f"jogador{str(c)}"] = randint(1,6)
ranking = {}
print("Valores sorteados") 
for k, v in jogo.items():
    print(f'{k} com {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print("Ranking")
for e, (k,v) in enumerate (ranking):
    print(f'{e+1}º lugar {k} com {v}')
    sleep(0.5)

