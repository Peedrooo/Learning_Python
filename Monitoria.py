x = int(input("Escolha uma quantia em real "))

cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
total_de_notas = 0

while 0 < x < 1000000 :

    if x >= 100:
        x = x - 100
        cem += 1
        total_de_notas += 1 
    
    if x >= 50 and x < 100 :
        x = x - 50
        cinq += 1
        total_de_notas += 1 

    if x >= 20 and x < 50:
        x = x - 20
        vinte += 1
        total_de_notas += 1 
    
    if x >= 10 and x < 20:
        x = x-10
        dez += 1
        total_de_notas += 1 
    
    if x >= 5 and x < 10:
        x = x - 5
        cinco += 1
        total_de_notas += 1 

    if x >= 2 and x < 5:
        x = x - 2
        dois += 1
        total_de_notas += 1 

    if x >= 1 and x<2:
        x = x-1
        um += 1
        total_de_notas += 1 
    
print('O total de notas será ',total_de_notas)
print(cem,' nota(s) de R$ 100,00')
print(cinq,' nota(s) de R$ 50,00')
print(vinte,' nota(s) de R$ 20,00')
print(dez,' nota(s) de R$ 10,00')
print(cinco,' nota(s) de R$ 5,00')
print(dois,' nota(s) de R$ 2,00')
print(um,' nota(s) de R$ 1,00')
