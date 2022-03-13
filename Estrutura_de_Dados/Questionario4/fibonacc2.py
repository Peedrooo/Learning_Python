# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,⋯
# Lista de Fibonacci com recursão 

'''lista = []
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
'''


'''def fibonacci(n):
    arr = [0,1]
    if n < 2:
        return [0] or [1]
    else:
        while(len(arr)<n):
            arr.append(0)
        if(n ==0 or n==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,n):
                arr[i]=arr[i-1]+arr[i-2]
            return(arr)'''

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    lista = [0,1]
    p1 = 0
    p2 = 1
    cont = 3
    while cont <= n:
        t3 = p1 + p2
        lista.append(t3)
        p1 = p2
        p2 = t3
        cont += 1
    return lista


print(fibonacci(2))
