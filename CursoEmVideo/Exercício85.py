num = [[],[]]

while True:
    escolha = int(input("escolha um número inteiro "))
    if escolha%2 == 0:
        num[0].append(escolha)
    else:
        num[1].append(escolha)

    cont = input("Gostaria de continuar? ").strip()
    if cont in "nN":
        break

num[0].sort()
num[1].sort()


print(f'Números em ordem crescente {num}')
