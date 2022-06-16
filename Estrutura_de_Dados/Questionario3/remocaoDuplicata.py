
qnt = int(input())
for c in range(qnt):
    parentese,colchetes,chaves = 0,0,0
    ponto_abertura = []
    ponto_fechamento = []
    exp = input()
    for c in range(len(exp)):

        if (exp[c] in '(' and exp[c+1] in '('):
            parentese += 1
            ponto_abertura.append(c+1) 

        if (exp[c] in '[' and exp[c+1] in '['):
            colchetes += 1
            ponto_abertura.append(c+1)

        if (exp[c] in '{' and exp[c+1] in '{'):
            chaves += 1
            ponto_abertura.append(c+1)
           

        if c+1 < len(exp):
            if (exp[c] in ')' and exp[c+1] in ')'):
                parentese += 1
                ponto_fechamento.append(c+1)

            if (exp[c] in ']' and exp[c+1] in ']'):
                colchetes += 1
                ponto_fechamento.append(c+1)

            if (exp[c] in '}' and exp[c+1] in '}'):
                chaves += 1
                ponto_fechamento.append(c+1)


    if chaves >= 2 or colchetes >= 2 or parentese >= 2:
        
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')

"""qnt = int(input())
for c in range(qnt):
    exp = input()
    operacoes = []
    for c in range(len(exp)):
        if exp[c] in '()[]{}*/-+':
            operacoes.append(exp[c])
    for c in range(len(operacoes)):
        if operacoes[c] 
"""