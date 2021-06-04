from random import randint
from time import sleep

def linha():
    print('--'*20)
    return()


linha()
titulo=('MEGA SENA')
print(f"{titulo:^40}")
linha()

qnt = int(input("Quanto palpites gostaria ? "))

lista = []

for c in range(qnt):
    lista.append([])


print(f"-=-=-=  SORTEANDO {qnt} JOGOS  -=-=-=" )


for c in range(qnt):
    for d in range(6):
        num = randint(0,60)
        while num in lista[c]:
            num = randint(0,60)
        lista[c].append(num)
    print(f'JOGO {c+1}: {lista[c]}')
    sleep(1)

print(f"-=-=-=-= < BOA SORTE > -=-=-=-= ")





