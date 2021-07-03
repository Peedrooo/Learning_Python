# Programa interactive help
# Fazendo com ajuda do copilot, foco em velocidade !!!
def ajuda(var):
    return(help(var))

while True:
    var = input("Digite uma função ou comando: ")
    if var == "fim":
        break
    print(ajuda(var))
print("Fim do programa")
