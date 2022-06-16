def avaliacao(exe,tra):
    nf = 0.4*exe + 0.6*tra
    if exe >= 5 and tra >= 5:
        if nf >= 9:
            return (nf,'SS')
        elif nf >= 7:
            return (nf,'MS')
        elif nf >= 5:
            return (nf,'MM')
        elif nf >= 3:
            return (nf,'MI')
        else:
            return (nf,'II')
    else:
        if nf >= 3:
            return (nf,'MI')
        else:
            return (nf,'II')
        

print(avalicao(5,4))