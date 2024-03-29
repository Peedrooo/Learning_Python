"""
Aula 23:
    try:
        num = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        r = num / num2
    except Exception as erro:
        print(f"Erro {erro.__class__}")
        print(f"Erro {erro.__cause__}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    else:
        print (f'O resultado é {r}')
    finally:
        print("Execução finalizada")

"""

def leiaint():
    while True:
        try:
            num = int(input("Digite um número inteiro "))
        except KeyboardInterrupt:
            num = 1
            print('Entrada de dados interrompida')
        except (TypeError,ValueError):
            print('Erro no tipo de dado inserido')
            continue
        except Exception as erro:
            print(f"Erro desconhecido: {erro.__class__}")
        else:
            return num
            

def leiareal():
    while True:
        try:
            num = float(input("Digite um Real: "))
        except (TypeError,ValueError):
            print('Erro no tipo de dado inserido')
        except (KeyboardInterrupt):
            num = 1
            print('Entrada de dados interrompida')
        except Exception as erro:
            print(f"Erro: {erro.__class__}")
        else:
            return num
            

print(f'O produto dos números digitados resulta em: {leiaint()*leiareal()}')

