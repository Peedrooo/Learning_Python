def fibonacci(n):
    chamadas = [] 

    def fibo(n):
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

    return fibo(n+1)

fibonacci(2)
