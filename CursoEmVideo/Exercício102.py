def fact(num,show = False):
    """
    -> Calcula o Fatorial de um número.
    num = O número a ser calculado.
    show (opcional) Mostrar ou não a conta
    Return: Resultado da conta
    """
    resultado = 1
    if num < 0:
        num = num*-1  
    while num > 0:
        resultado *= num
        if show: 
            print(f'{num} ',end = '')
            if num > 1:
                print('x', end = ' ')
            else:
                print('=',end = ' ')
        num -= 1   
    return( f"{resultado}")            

num = int(input('Gostaria de ver o fatorial de qual valor? '))
conta = input("Gostaria de ver a conta ? [S/N] ").strip()[0]

if conta in 'Ss':
    conta = True

print(fact(num,show = conta))
help(fact)