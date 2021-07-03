# Este exercício será feito com uso da extensão copilot (GitHub)
def notas(*nota,sit = False):
    boletin = {}
    notas = []
    for i in nota:
        notas.append(i)
    boletin['Notas'] = notas
    boletin['Media'] = (sum(notas)/len(notas))
    boletin['Maior'] = max(notas)
    boletin['Menor'] = min(notas)
    if sit == True:
        boletin['Situação'] = 'Boa' if boletin['Media'] >= 7  else 'Ruin'
    return boletin

resp = notas(5,6,7,8)
print(resp)