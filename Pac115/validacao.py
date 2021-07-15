from Pac115.estilo import vermelho
def leiainte(x,y):
    while True:
        try:
            var = int(input(x))
        except:
            print(vermelho('Valor inválido'))
        else:
            if var in range(1,y+1):
                return var
            else:
                print(vermelho("Opção inválida"))

def leiaint(x):
    while True:
        try:
            var = int(input(x))
        except:
            print(vermelho('Valor inválido'))
        else:
            return var
