entrada = input("Digite aqui sua espressão para ser validada ")
a = entrada.count("(")
b = entrada.count(")")

if a/b == 1:
    print("Expressão válida")
else:
    print("Expressão invalida")