def linha():
    print('-='*20)
    return()
c = "s"
cont = 0
jogo = {}
jogadores = []
while c not in "Nn":
    jogo["Cod"] = cont 
    jogo["Nome"] = input("Nome do jogador ")
    jogos = int(input(f'Quantas partidas {jogo["Nome"]} jogou? '))
    jogo["Gols"] = []
    for c in range(1, jogos + 1 ):
        jogo["Gols"].append(int(input(f"Quantos gols na partida {c} ")))
    jogo["Total"] = sum(jogo["Gols"])
    jogadores.append(jogo.copy())
    jogo.clear()
    c = input('Gostaria de continuar ? ').upper()
    cont += 1

linha()
print('cod  nome         gols        total')
linha()

for v in jogadores:
    print(v["Cod"], v["Nome"], v["Gols"],v["Total"])
linha()

esc = int(input("Mostrar dados de qual jogador ? "))



while esc != 999:
    if esc not in range(len(jogadores)) :
        print(f'ERRO! Não exite jogador com o código {esc}! Tente novamente')
    else:
        for v in jogadores:
            if v["Cod"] == esc:
                print(f'--Levantamento do jogador {v["Nome"]}')
                for c in range(len(v["Gols"])):
                    print(f'No jogo {c} fez {v["Gols"][c]}')
    esc = int(input("Mostrar dados de qual jogador ? "))
                       
print('FINALIZANDO')
