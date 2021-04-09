print('PROGRAMA BASES NUMÉRICAS')
num = int(input('Qual o número deseja converter? '))
escolha = int(input('''Escolha uma base numérica para conversão
[1] --> Binário
[2] --> Octal
[3] --> Hexadecimal ''').strip())
if escolha == 1:
    print(f'O número {num} em binário será: {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} em octal será: {oct(num)[2:]}')
elif escolha == 3:
    print(f'O número {num} em hexadeciamal será: {hex(num)[2:]}')
else:
    print('Opção inválida')