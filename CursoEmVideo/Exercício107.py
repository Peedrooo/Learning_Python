from utilidadesCeV.moeda import moeda
valor = float(input("Digite um valor "))
print(f"Valor aumentado {moeda.aumentar(valor)}")
print(f"Valor reduzido {moeda.diminuir(valor)}")
print(f"Metade do valor {moeda.metade(valor)}")
print(f"Dobro do valor {moeda.dobro(valor)}")
