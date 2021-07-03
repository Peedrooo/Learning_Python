# Este exercício será feito com uso da extensão copilot (GitHub)
def notas(*nota,sit = False):
    """
    :param nota: Uma ou mais notas
    :param sit: Se a situação da aula foi boa média ou razoável
    :return: Retorna um dicionário com informações das notas e a situação da mesma
    """
    boletin = {}
    notas = []
    for i in nota:
        notas.append(i)
    boletin['Total'] = len(notas)
    boletin['Media'] = (sum(notas)/len(notas))
    boletin['Maior'] = max(notas)
    boletin['Menor'] = min(notas)
    if sit:
        if boletin['Media'] >= 7:
            boletin['Situação'] = 'Boa'  
        elif boletin['Media'] >= 5:
            boletin['Situação'] = 'Razoável'
        else:
            boletin['Situação'] = 'Ruim'
    return boletin

resp = notas(3.5,5,3.5, sit = True)
print(resp)