from Pac115.estilo import cabeçalho
def arquivoex(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Erro ao Criar arquivo")


def lerarquivo(nome):
    try:
        a = open(nome,"rt")
    except:
        print('Erro ao ler arquivo')
    else:     
        (cabeçalho("Pesoas cadastradas"))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na hora de escrever os dados')
    finally:
        a.close()
