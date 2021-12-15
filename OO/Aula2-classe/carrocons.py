class Carro():
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor

carro_avo = Carro('Strada', 2010, 'Branca')
meu_carro = Carro('Fusca', 1968, 'Preto')
carro_avo.cor
meu_carro.cor = 'Vermelho'
meu_carro.cor