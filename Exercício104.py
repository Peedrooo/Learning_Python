'''
def leaint(texto):
    esc = (input(texto)).strip()
    while len (esc) == 0:
        esc = input("Digite um número inteiro valido ")
    fat = esc[0]
    while fat not in str(list(range(10))) and fat not in str(list(range(0,-10,-1))) or len(esc)==0 or fat in ' ':
        esc = input("Digite um número inteiro valido ")
        while esc in ' ':
            esc = input("Digite um número inteiro valido ")
        fat = esc[0]
    if float(esc) == int(esc):
        return(esc)

'''
def leaint(texto):
    esc = (input(texto)).strip()
    while True:
        if esc.isnumeric() and float(esc) == int(esc):
            return(int(esc))
        else:
            esc = input("Digite um número inteiro válido ").strip()
        
n = leaint("Digite um número inteiro ")
print(f"Voce digitou o valor {n}")

