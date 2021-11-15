print('PROGRAMA COMPARAÇÃO DE VALORES')
values = []
for c in range (1,4):
    values.append(int(input(f'Escolha o {c}º número ')))
print(f'O maior númeor escolhido é ',max(values))
print(f'O menor número escolhido é ',min(values))
a = max(values)
b = min(values)
for c in range (0,3):
    if values[c] < a and values[c] > b:
        print(f'E o número do meio é {values[c]}')
