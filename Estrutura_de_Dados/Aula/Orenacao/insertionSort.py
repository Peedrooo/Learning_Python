def insertion_sort(lista):
    for i in range(1, len(lista)):
        aux = lista[i]
        j = i - 1
        # Mova os elementos da lista [0...i-1], 
        # que são maiores que o elemento comparado, 
        # para uma posição à frente de sua posição atual!
