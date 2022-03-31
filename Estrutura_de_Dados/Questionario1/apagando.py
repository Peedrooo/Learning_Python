def apagando(sequence):
    cont = 0
    for c in range(len(sequence)):
        if '1' in sequence[c:] and '1' in sequence[:c]:
            if sequence[c] == '0': 
                cont += 1
                
    return cont
         

for c in range(int(input())):
    sequence = input()
    print(apagando(sequence))

