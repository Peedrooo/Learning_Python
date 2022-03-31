numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[1:])

def soma(numeros):
   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + soma(numeros[1:])
