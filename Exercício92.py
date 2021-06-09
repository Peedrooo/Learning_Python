from datetime import date
cad = {}
cad["Nome"] = input("Nome: ")
cad["Idade"] = int(date.today().year) - (int(input("Ano de nascimento: ")))
a = int(input("Carteira de Trabalho (0 se não têm) "))
if a != 0:
    cad["ctps"] = a
    cad["Aposentadoria"] = int(input("Ano de contratação ")) - int(date.today().year) + 35 + cad ["idade"]
    cad["Salário R$"] = float(input("Salário: R$ "))

for k, i in cad.items():
    print(f"{k}: {i}")
