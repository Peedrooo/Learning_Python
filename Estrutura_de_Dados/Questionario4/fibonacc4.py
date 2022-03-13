# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯


# Um, dois, três Fibonaccis...
def fibonacci(n,cont=0):
    cont += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1,cont)[0] + fibonacci(n-2,cont)[0])

def Fib(n):
    a,b = fibonacci(n)
    print(a,b)
Fib(10)
    



