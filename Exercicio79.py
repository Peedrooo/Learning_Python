r = "s"
valores = []
while r != "N":
    valor = int(input("Digite um valor: "))
    if valor not in valores:
        valores.append(valor)
    r = input("Gostaria de continuar ?").strip().upper()
valores.sort()
print(f'Os valores escolhidos foram: {valores}')

