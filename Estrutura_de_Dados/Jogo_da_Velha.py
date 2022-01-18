# função para inciar o jogo           
def iniciar_jogo():
    print('''Bem vindo ao jogo da velha\nO primeiro a jogar é o X\nO jogo acaba quando houver 3 X ou 3 O na mesma linha, coluna ou diagonal\nCaso precise desfazer a jogada, digite "desfazer"\n''')
    vez = 'X'
    # criando tabuleiro
    continuar = True
    while continuar:
        tabuleiro = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
        while True:
            imprimir_tabuleiro(tabuleiro)
            print(f'Vez do jogador {vez}')
            tabuleiro = jogar(vez, tabuleiro) 

            if verificar_vencedor(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print(f'O jogador {vez} venceu!')
                break
            elif verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print('Empate!')
                break
            else:
                vez = alternador_vez(vez)
        continuacao = input('Deseja continuar? (s/n) ')
        if continuacao in 'Nn':
            continuar = False
        



# função para inserir valores no tabuleiro
def jogar(vez, tabuleiro):
    while True:
        coordenada = input('Digite a coordenada no formato "n,n": ')
        global linha
        global coluna

        # Fragmentando coordenada em linha e coluna
        if coordenada == 'desfazer':
            tabuleiro[linha][coluna] = ' '
            imprimir_tabuleiro(tabuleiro)
            vez = alternador_vez(vez)
        try: 
            linha,coluna = (int(i) - 1 for i in coordenada.split(',')) 
            # Verificando se a coordenada está dentro do tabuleiro
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = vez
                return tabuleiro
            else:
                print ('Espaço ocupado, tente novamente')
        except:
            print('Coordenada inválida, tente novamente') 

# alterna vez de jogar
def alternador_vez(vez):   
    if vez == 'X':
        return 'O'
    else:
        return 'X'

# função para imprimir tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for c in tabuleiro:
        print(c)
    print()

# função para verificar se há vencedor
def verificar_vencedor(tabuleiro):
        
    # Verificando colunas e linhas 
    for c in range(3):
        if c[0] == c[1] == c[2] != ' ':
            return True
        elif tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] != ' ':
            return True
            
    # Verificando diagonais          
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return True  
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return True
    else:
        return False

def verificar_empate(tabuleiro):
    for c in tabuleiro:
        if ' ' in c:
            return False
    return True
            
iniciar_jogo()
