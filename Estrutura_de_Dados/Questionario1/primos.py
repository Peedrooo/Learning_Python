
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

def primos_gemeos(n):
    par1,par2 = 1,3
    gemeos = []
    for c in range(n):
        while True:
            par1 += 2
            par2 += 2
            if primo(par1) and primo(par2):
                if par1 + 2 == par2:
                    gemeos.append(tuple((par1,par2)))
                    break
    return gemeos

