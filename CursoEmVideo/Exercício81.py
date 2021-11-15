valores = []
r = "s"
while r != "N":
    valores.append(int(input("Digite um valor ")))
    r = input("Gostaria de continuar? ").strip().upper()
print(f"No total {len(valores)}, foram digitados, sendo eles: ")
valores.sort(reverse=True)
for c in range (len(valores)):
    print(valores[c],end="..,")
if 5 in valores:
    print(f"\nO número cinco foi encontrado na posição {valores.index(5)+1}")
else:
    print("\nO Valor 5 não foi encontrado")