matriz = [[],[],[]]
par = terc = 0
segun = []
for c in range(3):
    for d in range(3):
        valor = (int(input(f'Valor para {[c, d]} ')))
        matriz[c].append(valor)
        if valor %2 == 0:
            par += valor
        if d == 2:
            terc += valor
        if c == 1:
            segun.append(valor)

print("-="*15)

for c in range(3):
    for d in range(3):
        print(f"[{matriz[c][d]:^3}]", end=' ')
    print()
print("-="*15)

print(f'''A soma dos valores pares é = {par}
A soma dos valores da terceira coluna é = {terc}
O maior valor da segunda linha é = {max(segun)}
''')





