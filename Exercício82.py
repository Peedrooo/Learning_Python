valores = []
impar = []
par = []

r = "s"

while r != "N":
    valores.append(int(input("Digite um valor ")))
    r = input("Gostaria de continuar? ").strip().upper()

for c in range(len(valores)):
    if valores[c] %2 == 0:
        par.append(valores[c])
    else:
        impar.append(valores[c]) 

print(f'''
Lista completa: {valores},
Lista pares: {par},
Lista impar: {impar}
''')