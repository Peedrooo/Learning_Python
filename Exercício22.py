print('PROGRAMA MANIPULAÇÃO DE NOME')
nome = str(input("Digite seu nome completo ")).strip()
print('Nome apenas com letras maiúsculas',nome.upper())     
print('Nome apenas com letras minusculas',nome.lower())
print('Número de letras do nome', len(nome) - nome.count(' '))
print('Número de letras do primeiro nome', len(nome.split()[0]))




'''n = len(nome.split())
numero = 0
for x in range (0,n):
    numero += len(nome.split()[x])

print('Número de letras sem espaços:',numero)'''

print('Número de letras do primeiro nome', len(nome.split()[0]))
