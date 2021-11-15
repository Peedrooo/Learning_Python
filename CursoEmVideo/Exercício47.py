print('NÚMEROS PARES NO LAÇO')
for c in range (1,51):
    if c%2 == 0:
        print(c, end=' ')

print('\nOutra maneira mais leve')
for c in range (2,51,2):
    print(c, end=' ')