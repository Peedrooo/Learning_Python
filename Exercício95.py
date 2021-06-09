def linha():
    print('-='*20)
    return()
c = "s"
jogo = {}
jogadores = []
while c not in "Nn": 
    jogo["Nome"] = input("Nome do jogador ")
    jogos = int(input(f'Quantas partidas {jogo["Nome"]} jogou? '))
    jogo["Gols"] = []
    for c in range(1, jogos + 1 ):
        jogo["Gols"].append(int(input(f"Quantos gols na partida {c} ")))
    jogo["Total"] = sum(jogo["Gols"])
    jogadores.append(jogo.copy())
    jogo.clear()
    c = input('Gostaria de continuar ? ').upper()

linha()
print('cod  nome         gols        total')
linha()

for e,v in enumerate (jogadores):
    print(e, v.values())
linha()




