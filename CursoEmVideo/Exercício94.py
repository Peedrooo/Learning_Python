every = []
while True: 
    indiv = {}
    indiv["Nome"] = input("Nome: ")
    indiv["Sexo"] = input("Sexo: [M/F] ").strip().upper()
    while indiv["Sexo"] not in 'MnFf':
        indiv["Sexo"] = input("Sexo inválido, digite novamente [M/F] ").strip().upper()[0]
    indiv["Idade"] = int(input("Idade: "))
    every.append(indiv.copy())
    indiv.clear()
    conti = input("Gostaria de continuar ? ")
    while conti not in "SsNn":
        conti = input("Resposta inválida, [S/N] ").strip().upper()[0]
    if conti in "Nn": 
        break
print(f"- O grupo tem {len(every)} pessoas")

soma = 0
for p in every:
    soma += p["Idade"]
media = soma/len(every)
print(f"- A média de idade é {media}")


print("- As mulheres cadastradas foram:", end=' ')
for p in every:
    if p["Sexo"] in "Ff":
        print(p['Nome'], end=' ')
print()
print("- Pessoas acima da média:")

for p in every:
    if p["Idade"] > media:
        for k, v in p.items():
            print(f'{k}: {v}', end = ' ')
        print()

print("<<<ENCERRANDO>>>")
 
