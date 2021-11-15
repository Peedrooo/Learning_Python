nomes = ('Flavia','Gabriela','Pedro','Geovana','Tell','Ravi','Catarina','Tommy','Arthur','sckote','locky')
for nome in nomes:
    print(f'\n{nome.upper()} possui ', end = '')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(letra,end = ' ')