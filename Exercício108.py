import moeda
valor = float(input("Digite um valor "))
print(f"Valor aumentado de {moeda.moeda(valor)} é {moeda.moeda(moeda.aumentar(valor))}")
print(f"Valor reduzido de {moeda.moeda(valor)} é {moeda.moeda(moeda.diminuir(valor))}")
print(f"Metade do valor de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}")
print(f"Dobro do valor de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}")
