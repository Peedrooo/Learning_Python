from Pac115.estilo import vermelho
def leiaint3(x):
    while True:
        try:
            var = int(input(x))
        except:
            print(vermelho('Valor inválido'))
        else:
            if var in range(1,4):
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




    