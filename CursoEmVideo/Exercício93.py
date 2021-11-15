def linha():
    print('-='*20)
    return()


jogo = {}
jogo["Nome"] = input("Nome do jogador ")
jogos = int(input(f'Quantas partidas {jogo["Nome"]} jogou? '))

jogo["Gols"] = []


for c in range(1, jogos + 1 ):
    jogo["Gols"].append(int(input(f"Quantos gols na partida {c} ")))
jogo["Total"] = sum(jogo["Gols"])

linha()
print(jogo)
linha()

for k, v in jogo.items():
    print(f'O campo {k} possui valor {v}')
linha()

print(f'O jogador {jogo["Nome"]} jogou {len(jogo["Gols"])} partidas')
for e,v in enumerate (jogo["Gols"] ):
    print(f"=> Na partida {c}, fez {v} gols.")
print(f'Foi um total de {jogo["Total"]} gols.')
