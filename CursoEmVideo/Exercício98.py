from time import sleep

def linha():
    print('-='*20)

def cont(i,p,f):
    if p < 0:
        p = p*-1
    elif p == 0:
        p = 1
    if i > f:
        linha()
        while True:
            print(i,end=" ",flush = True)
            sleep(0.25)
            i = i - p 
            if i < f:
                print() 
                linha()
                break
    elif i < f:
        linha()
        while True:
            print(i,end=" ",flush = True)
            sleep(0.25)            
            i = i + p
            if i > f:
                print()
                linha()
                break
cont(1,1,10)
cont(10,2,0)
cont(i=int(input("Início ")),p=int(input("Passo ")),f=int(input("Fim ")))
