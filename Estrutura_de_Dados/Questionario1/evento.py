def separador(tempo):
    tempo = tempo.replace(' ',':').split(':')
    tempo = list(map(int,tempo))
    dias = tempo[0]
    horas,minutos,segundos = tempo[1:]

    return dias*86400+horas*3600+minutos*60+segundos

def evento(tempo1,tempo2):
    duracao_total = separador(tempo2) - separador(tempo1)
    if duracao_total <= 0:
        return 'Data inválida!'

    dias = duracao_total // 86400
    duracao_total %= 86400

    horas = duracao_total // 3600
    duracao_total %= 3600

    minutos = duracao_total // 60
    duracao_total %= 60

    segundos = duracao_total

    return f'{dias} dia(s) \n{horas} hora(s) \n{minutos} minuto(s) \n{segundos} segundo(s)'
           
print(evento(input(),input()))
    