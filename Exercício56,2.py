print('PROGRAMA COMPLETO')
cadastro1 = []
nome = []
idade = []
sexo = []


# Laço que acrescenta informações dos usuários
idadeH = [0]
novinha = 0
velhinho = []

for c in range(0,4):
    nome.append(input('Nome: ').strip().title())
    idade.append(int(input('Idade: ')))
    print('MASCULINO OU FEMININO')
    sexo.append(str(input('Sexo: ').strip().upper()[0]))

    #Diferenciando idade de homem e de mulher
    if sexo[c] == 'M':
        if idade[c] > max((idadeH)):
            idadeH.append(idade[c])
            velhinho.append(nome[c])

    elif sexo[c] == 'F':
        #Contando o número de mulhers abaixo de 20 anos
        if idade[c] < 20:
             novinha += 1



# RESPOSTAS
print(f'A idade média dos cadastros é de {sum(idade)/len(idade):.2f}')

print(f'O homem mais velho é o Sr {velhinho[len(velhinho)-1]}')
print(f'Existem {novinha} mulheres abaixo de 20 anos')
