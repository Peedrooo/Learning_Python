# Add
def add(X):
    processo = []
    for c in range(X):
        comando, parametro = input().split(maxsplit = 1)
        processo.insert(0,[comando, parametro])
    solicitacoes.insert(0, processo)

# Process
def process():
    # print(solicitacoes)
    try:
        if len(solicitacoes[-1]) > 1 :
            comando, parametro = solicitacoes[-1].pop()
            solicitacoes.insert(0, solicitacoes.pop())
            # print(solicitacoes)

        else:
            comando, parametro = solicitacoes.pop().pop()
            # print(solicitacoes)
        
        if comando == 'merge':
            merge(parametro)
        elif comando == 'crypto':
            crypto(parametro)
        elif comando == 'deYodafy':
            deYodafy(parametro)
        else:
            print('comando inválido')
    except:
        pass

# Halt
def halt():
        # print(solicitacoes)
        comandos = 0
        qnt_solicitacoes = len(solicitacoes)
        cont = qnt_solicitacoes
        # ultimoProcesso = -1
        while cont > 0:
            comandos += len(solicitacoes[cont-1])
            cont -= 1 
        print(f"{qnt_solicitacoes} processo(s) e {int(comandos)} comando(s) órfão(s).")


# Crypto
def crypto(S):
    resultado = []
    cont = 0
    historico = 0
    valores = ''

    for indice in range(len(S)): # Percorrendo sinais 
        if S[indice] == "+":
            for i in range(cont + 1, historico, -1): # Incrementando resultado para indice = +
                resultado.append(i)
            cont += 1
            historico = cont
        else:
            cont += 1
    if S[-1] == "-":
        for i in range(cont + 1, historico, -1): # Incrementando resultado para indice = -
            resultado.append(i)
    else:
        resultado.append(cont + 1)
    
    for elemento in range(len(resultado)):    # Reunindo valores do resultado
        valores += str(resultado[elemento])

    print(valores)

# DeYodafy
def deYodafy(w):
    sinal = w[-1]
    recorte = (w[:len(w)-1]).split()    
    inversao = recorte[::-1] 
    fala = ' '.join(inversao)+sinal
    print(fala)


# Merge
def merge(I):
    from copy import deepcopy

    # Tratando entrada
    I = I.replace("]", "")
    I = I.replace("[", "")
    I = I.replace(", ", ",")
    pontos = I.split()

    coordenadas = []
    for indice in pontos:
        coordenadas.append(list(map(int, indice.split(","))))

    lista = []
    mudanca = True

    while mudanca:
        mudanca = False
        while len(coordenadas)>0:
            cont = 0 
            for intervalo in lista:
                if (intervalo[1] >= coordenadas[0][0] and intervalo[0] <= coordenadas[0][0]):
                    lista[cont] = [min(coordenadas[0][0], intervalo[0]), max(coordenadas[0][1], intervalo[1])]
                    coordenadas.pop(0)
                    mudanca = True
                    break
                elif (intervalo[0] <= coordenadas[0][1] and intervalo[0] >= coordenadas[0][0]):
                    lista[cont] = [min(coordenadas[0][0], intervalo[0]), max(coordenadas[0][1], intervalo[1])]
                    coordenadas.pop(0)
                    mudanca = True
                    break
                cont += 1
            else:
                lista.append(coordenadas.pop(0))
        coordenadas = deepcopy(lista)
        lista.clear()

    coordenadas.sort(key = lambda x : x[0])
    
    print(*coordenadas)
    



# Main
solicitacoes = []
while True:
    solicitacao = input().split(maxsplit = 2)
    if solicitacao[0] == 'halt':
        halt()
        break
    else:
        if solicitacao[0] == 'add':
            add(int(solicitacao[1]))
        elif solicitacao[0] == 'process':
            process()
        elif solicitacao[0] == 'merge':
            merge(solicitacao[1])
        else:
            print('Solicitação inválida')
            

