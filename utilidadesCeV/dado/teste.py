def leiadinheiro():
    valor = (input("Digite o valor a ser sacado: "))
    while valor.isnumeric() == False:
        if ',' in valor and valor.count(',') == 1:
            valor = valor.replace(',','')
        elif '.' in valor and valor.count('.') == 1:
            valor = valor.replace('.','')
        if valor.isnumeric():
            break
        valor = input(f'"{valor}" Corresponde à um valor inválido, digite novamente ')
    valor = float(valor)
    return valor


    