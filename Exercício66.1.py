escolha = soma = escolha = cont = 0
print('Para parar digite [999]')
while True:
    cont +=1
    escolha = int(input('Escolha um número '))
    if escolha == 999:
        break
    soma += escolha 

print(f"A soma dos {cont} números selecionados foi: {soma}" )
