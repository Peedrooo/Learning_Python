print('PROGRAMA ANÁLISE DE NOME')
name = input('Digite seu nome completo ').strip().upper().split()
print('O nome',' '.join(name),'possui Silva em sua extensão?', 'SILVA' in name)
