def ficha(nome = "<Desconhecido>", gol = '0'):
    
    return(f"O jogador: {nome} fez {gol} gols")

while True:
    name = (input("Nome: ")).strip()
    gols = (input('Gols ')).strip()
    if name != '' and gols != '':
        print(ficha(nome = name, gol = gols))
    if name == '' and gols == '':
        print(ficha())
    else:
        if name == '' and len(gols)>0:
            print(ficha(gol = gols))
        if len(name)>0 and len(gols) == 0:
            print(ficha(nome=name))
        