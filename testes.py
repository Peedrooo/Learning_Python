
cl_cadastrados = [{'nome': 'ana', 'cpf': '1000', 'endereco': 'rua xxxx'}, {'nome': 'carlos', 'cpf': '7770', 'endereco': 'Rua aaaa'}]
nome = (input("Digite o nome que deseja buscar: "))   
for i in range(0,len(cl_cadastrados)):
    cl = cl_cadastrados[i]

    if (nome == cl['nome']):
        print(cl["cpf"])
        
jogador = {}
jogadores = []
d = 0

while True:
    jogador["Cod"] = d
    jogador["Nome"] = input("Nome: ")
    jogador["Jogos"] = int(input("Jogos: "))
    Gols = []
    for c in range(jogador["Jogos"]):
        Gols.append(int(input(f"Gols feitos na {c+1}º partida ")))
    jogador["Gols"] = Gols[:]
    jogador["Total"] = sum(Gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    conti = input("Gostaria de continuar ? ").upper().strip()
    if conti in "nN":
        break
    d += 1

print("cod     nome   jogos    gols     total ")
for v in jogadores:
    print(v["Cod"], v["Nome"], v["Jogos"], v["Gols"], v["Total"])

while True:
    escolha = int(input("Qual jogador gostaria de escolher"))
    if escolha == 999:
        break
    elif escolha not in range(len(jogadores)):
        print("Código não encontrado")
    for v in jogadores:
        if v["Cod"] == escolha:
            print(f'--Levantamento do jogador {v["Nome"]}')
            for c in range(len(jogadores)):
                print(f'No jogo {c} fez {v["Gols"][c]}')
    
        
print("PROGRAMA FINALIZADO")     
help()