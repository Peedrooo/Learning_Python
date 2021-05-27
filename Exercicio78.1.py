# Valores na lista

valores = []
pmaior=[]
pmenor=[]

for c in range(0,5):
    valores.append(int(input('Digite um valor ')))


print(f"O maior valor digitado foi {max(valores)}, nas posições: ", end="")
for x, c in enumerate(valores):
    if max(valores) == c:
        print(f'{x}...',end="")

print(f"\nO menor valor foi {min(valores)}, nas posições: ",end="")
for x, c in enumerate(valores):
    if min(valores) == c:
        print(f"{x}...",end="")
    
