from utilidadesCeV.moeda import moeda
valor = float(input("Digite um valor "))
print(f"Valor aumentado de {moeda.moeda(valor)} é {moeda.aumentar(valor,True)}")
print(f"Valor reduzido de {moeda.moeda(valor)} é {moeda.diminuir(valor)}")
print(f"Metade do valor de {moeda.moeda(valor)} é {moeda.metade(valor)}")
print(f"Dobro do valor de {moeda.moeda(valor)} é {moeda.dobro(valor)}")
