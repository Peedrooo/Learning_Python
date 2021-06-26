def cont(i,p,f):
    if p < 0:
        p = p*-1
    if i > f:
        while True:
            print(i,end=" ")
            i = i - p 
            if i < f:
                print() 
                break
    elif i < f:
        while True:
            print(i,end=" ")
            i = i + p
            if i > f:
                print()
                break
cont(10,1,5)
cont(10,2,0)



cont(i=int(input("Início ")),p=int(input("Passo ")),f=int(input("Fim ")))
