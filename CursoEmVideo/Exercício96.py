def area(x,y):
    print('-='*20)
    print(f'A áreda de um terreno {x}x{y} é de {x*y}')
    print('-='*20)

print("Controle de terrenos")
print('=='*10)
la = float(input('Largura (m): '))
co = float(input('Comprimento (m): '))

area(la,co)
