dados = {'nome':'Pedro','idade':25}
print(dados["nome"])
dados["sexo"]="M"
print(dados)

for k, v in dados.items():
    print(f'O {k} é {v}')