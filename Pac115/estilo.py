def linha():
    print('--'*15)

def azul(x):
    return('\033[1;34m'+x+'\033[m ')

def vermelho(x):
    return('\033[1;31m'+x+'\033[m')

def verde(x):
    return('\033[1;32m'+x+'\033[m')

def amarelo(x):
    return('\033[1;33m'+x+'\033[m')

def cabeçalho(x):
    linha()
    print("{:^30}".format(x))
    linha()

def item(x,y):
    return (amarelo(x),'-',azul(y))

def menu(lista):
    for e,c in enumerate (lista):
        e+=1
        print(amarelo(str(e)),'-',azul(c))