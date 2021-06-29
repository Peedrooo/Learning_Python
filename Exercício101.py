from datetime import date

def voto(ano):
    global idade 
    idade = date.today().year - ano
    if 15 < idade < 18 or 65 < idade:
        return("Opcional")
    elif 18 <= idade < 65:
        return("Obrigatório")
    else:
        return("Negado")

while True:
    Nasc = int(input('Ano de nascimento: '))
    Resultado = voto(Nasc)
    print(f"Com {idade} anos o voto é: {Resultado}")
