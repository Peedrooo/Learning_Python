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
alunos["Média"] = float(input(f'Média de {alunos["Nome"]} '))
if alunos["Média"] >= 7:
    alunos["Situação"] = "Aprovado"
elif alunos["Média"] >= 5:
    alunos["Situação"] = "Recuperação"
else:
    alunos["Situação"] = "Reprovado"

for k, v in alunos.items():
    print(f"{k} é igual a {v}")