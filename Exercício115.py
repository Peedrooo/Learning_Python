from Pac115 import validacao,estilo
from time import sleep
cadastros = {}
while True:
    estilo.cabeçalho('MENU PRINCIPAL')
    menu = (["Pessoas Cadastradas","Cadastrar nova Pessoa","Sair do programa"])
    estilo.menu(menu)
    esc = validacao.leiainte(estilo.verde("Sua opção: "),3)
    if esc == 1:
        estilo.cabeçalho('Pessoas Cadastradas')
        for k,v in cadastros.items():
            print ("{:25}".format(k),v)
        sleep(2)

    elif esc == 2:
        estilo.cabeçalho("Novo Cadastro")
        ind = input("Nome: ")
        idad = validacao.leiaint("Idade: ")
        cadastros[ind] = idad
        print(f"Novo registro {ind} adicionado.")
    else:
        print("Sistema finalizado, volte sempre :)")
        estilo.linha()
        break
