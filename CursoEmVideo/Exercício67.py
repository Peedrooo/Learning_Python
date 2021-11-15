escolha = tab = 0
while True:
    escolha = int(input('Quer ver a tabuáda de qual valor? '))
    if escolha < 0:
        break
    while tab < 10:
        tab+=1
        print(f'{escolha} x {tab} = {escolha*tab}')
    tab = 0
    print('--'*20)
print("PROGRAMA FINALIZADO")