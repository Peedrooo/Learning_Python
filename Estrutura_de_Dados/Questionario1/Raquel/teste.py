def e_primo(entrada):
    if entrada == 1: return False
    else:
        for v in range(2,entrada):
            if entrada % v == 0:
                return False
        return True

def primo(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

