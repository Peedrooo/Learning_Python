from Pac115 import validacao,estilo
from Pac115.arquivo import *
from time import sleep

arq = 'Database.txt'
if not arquivoex(arq):    
    criararquivo(arq)


while True:
    estilo.cabeçalho('MENU PRINCIPAL')
    menu = (["Pessoas Cadastradas","Cadastrar nova Pessoa","Sair do programa"])
    estilo.menu(menu)

    esc = validacao.leiainte(estilo.verde("Sua opção: "),3)
    if esc == 1:
        lerarquivo(arq)
        sleep(2)

    elif esc == 2:
        estilo.cabeçalho("Novo Cadastro")
        nome = str(input("Nome: "))
        idade = validacao.leiaint("Idade: ")
        cadastrar(arq, nome, idade)

        
    else:
        print("Sistema finalizado, volte sempre :)")
        estilo.linha()
        break
