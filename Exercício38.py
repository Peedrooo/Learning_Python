print('COMPARAÇÃO DE VALORES')
numbers = []
numbers.append(float(input('Digite o primeiro valor ')))
numbers.append(float(input('Digite o segundo valor ')))
if numbers[0] == numbers[1]:
    print('Os números dados acima são iguais')
else:
    print(f'''O maior número é {max(numbers)}
E o menor é {min(numbers)}''')