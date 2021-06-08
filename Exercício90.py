'''
dados = {'nome':'Pedro','idade':25}
print(dados["nome"])
dados["sexo"]="M"

print(dados)
print(dados.keys())
print(dados.values())
print(dados.items())

for k, v in dados.items():
    print(f'O {k} é {v}')
'''

alunos = {}

alunos["Nome"] = input('Nome: ')
alunos["Média"] = float(input('Média: '))
if alunos["Média"] >= 5:
    alunos["Situação"] = "Aprovado"
else:
    alunos["Situação"] = "Reprovado"

for k, v in alunos.items():
    print(f"{k} é igual a {v}")