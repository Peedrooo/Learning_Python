tempo = int(input('Quanto tempo o carro foi alugado? '))
km = float(input('Quanto km vc rodou? '))
alugueltempo = tempo*60
aluguemkm = km*0.15
print(f'O custo do aluguel foi de {alugueltempo + aluguemkm:.2f}, \nvisto que o tempo corresponde ao custo foi de {alugueltempo} e o de kilometragem foi de {aluguemkm}')