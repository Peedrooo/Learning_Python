import moeda
valor = float(input("Digite um valor "))
print(f"Valor aumentado de {valor} é {moeda.moeda(moeda.aumentar(valor))}")
print(f"Valor reduzido de {valor} é {moeda.moeda(moeda.diminuir(valor))}")
print(f"Metade do valor de {valor} é {moeda.moeda(moeda.metade(valor))}")
print(f"Dobro do valor de {valor} é {moeda.moeda(moeda.dobro(valor))}")
