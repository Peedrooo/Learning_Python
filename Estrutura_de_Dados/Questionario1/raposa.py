# Pode escapar ? 
from math import sqrt

qnt_buracos = int(input())
coelho = list(map(float, input().split()))
raposa = list(map(float, input().split()))

coordena_buraco = []
for c in range(qnt_buracos):
    coordena_buraco.append(list(map(float,input().split()))) 


def escapar(coordena_buraco):
    for buraco in coordena_buraco:
        dis_coelho_buraco = sqrt((buraco[0] - coelho[0])**2 + (buraco[1] - coelho[1])**2)
        dis_raposa_buraco = sqrt((buraco[0] - raposa[0])**2 + (buraco[1] - raposa[1])**2)
        if dis_coelho_buraco < dis_raposa_buraco/2:
            return (f"O coelho pode escapar pelo buraco ({ buraco[0]:.3f}, {buraco[1]:.3f}).")
    return(f"O coelho nao pode escapar.")

print(escapar(coordena_buraco))
            





