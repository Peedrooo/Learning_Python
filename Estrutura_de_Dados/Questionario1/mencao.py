# funcao mencao
def avaliacao(ex,tra):
    nota = ex*0.4+ tra*0.6
    if nota >= 9:
        mencao = 'SS'
    elif nota >= 7:
        mencao = 'MS'
    elif nota >= 5:
        mencao = 'MM'
    elif nota >= 3:
        mencao = 'MI'
    elif nota > 0:
        mencao = 'II'
    else:
        mencao = 'SR'
    return tuple ((nota, mencao))

print(avaliacao(1, 2))
