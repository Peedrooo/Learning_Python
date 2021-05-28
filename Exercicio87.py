matriz = [[],[],[]]

for d in range(0,3):
    for c in range(0,3):
        matriz[d].append(int(input(f"Digite um valor para {[d,c]} ")))
print("-="*20)

for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        print(f"[{matriz[coluna][linha]:^5}]",end='')
    print("\n")


