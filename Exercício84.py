dado = []
Galera = []
peso = []
pesada = []
leve = []

while True:
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Peso: ")))
    Galera.append(dado[:])
    dado.clear()

    c = input("Gostaria de continuar?[N/S] ").strip()
    if c in "nN":
        break


for c in range(len(Galera)):
    peso.append(Galera[c][1])

for c in range(len(Galera)):
    if Galera[c][1]==max(peso):
        pesada.append(Galera[c][0])
    if Galera[c][1]==min(peso):
        leve.append(Galera[c][0])


print(f'''Ao todo {len(Galera)}, foram cadastradas,sendo:
Maior peso de {max(peso)}Kg, correspondente à {pesada}
Menor peso de {min(peso)}Kg, correspondente à {leve}''')

