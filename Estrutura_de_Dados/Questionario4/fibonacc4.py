# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯


# Um, dois, três Fibonaccis...




def Fib(n):
    chamadas = [] 

    def fibonacci(n):
        if n == 1:
            chamadas.append(n)
            return 0
        elif n == 2:
            chamadas.append(n)
            return 1
        else: 
            chamadas.append(n)
            # print(chamadas) 
            return fibonacci(n-1) + fibonacci(n-2)

    print(f'Fib({n}) = {fibonacci(n+1)} ({len(chamadas)} chamadas)')

Fib(int(input()))


    



