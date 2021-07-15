from Pac115 import validacao,estilo
from time import sleep
cadastros = {}
while True:
    estilo.linha()
    print("{:^30}".format('MENU PRINCIPAL'))
    estilo.linha()
    print(estilo.amarelo("1"),'-',estilo.azul("Ver pessoas cadastradas"))
    print(estilo.amarelo("2"),'-',estilo.azul("Cadastrar nova Pessoa"))
    print(estilo.amarelo("3"),'-',estilo.azul("Sair do Sistema"))
    esc = validacao.leiaint3(estilo.verde("Sua opção: "))
    if esc == 1:
        estilo.linha()
        print("{:^30}".format('Pessoas Cadastradas'))
        estilo.linha()
        for k,v in cadastros.items():
            print ("{:25}".format(k),v)
        sleep(2)

    elif esc == 2:
        estilo.linha()
        print("{:^30}".format('Novo Cadastro'))
        estilo.linha()
        ind = input("Nome: ")
        idad = validacao.leiaint("Idade: ")
        cadastros[ind] = idad
        print(f"Novo registro {ind} adicionado.")
    else:
        print("Sistema finalizado, volte sempre :)")
        estilo.linha()
        break

