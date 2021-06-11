cl_cadastrados = [{'nome': 'ana', 'cpf': '1000', 'endereco': 'rua xxxx'}, {'nome': 'carlos', 'cpf': '7770', 'endereco': 'Rua aaaa'}]
nome = (input("Digite o nome que deseja buscar: "))   
for i in range(0,len(cl_cadastrados)):
    cl = cl_cadastrados[i]

    if (nome == cl['nome']):
        print(cl["cpf"])
