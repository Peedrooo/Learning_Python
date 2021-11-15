'''
from time import sleep
def maior(*x):
    if len(x)>0:
        sleep(0.5)
        print('-='*20, flush = True)
        print("Analisando valores informados ")
        for c in range(len(x)):
            print(x[c],end = ' ')
        print(f'Foram informado {len(x)} valores ao todo')
        print(f"O maior valor informado foi {max(x)}")
    else:
        sleep(0.5)
        print('-='*20, flush = True)
        print('NENHUM VALOR INFORMADO')
'''
def maior(* valores):
    qnt = len(valores)
    if qnt > 0:
        for c in valores:
            print(c, end = ' ')
        print(f"Foram informados {qnt} ao todo")
        print(f"Sendo o maior {max(valores)}")
    else:
        print("NENHUM VALOR INFORMADO")

    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior()