qnt = int(input())
dado = input()

habilidades = (list(map(int, dado.split(' '))))
ordem_habilidade = sorted(habilidades,reverse=True)
more = 0
less = 0

if qnt < 11:
    for c in range(qnt):
        more += ordem_habilidade[c]

else:
    for c in range(11):
        more += ordem_habilidade[c]
    less = sum(ordem_habilidade[11:22])

print(more - less)



