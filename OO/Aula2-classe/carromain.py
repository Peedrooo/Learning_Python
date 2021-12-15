def main():
    carro1 = Carro('Fusca', 1968, 'Preto',95)
    carro2 = Carro('Brasilia', 2009, 'Azul',120)

    carro1.acelerar(100)
    carro1.freiar(50)
    carro2.acelerar()
    carro2.parar()


class Carro():
    def __init__(self, modelo, ano, cor, vmMAX):
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor
        self.velocidade = 0
        self.vmMAX = vmMAX
    
    def imprime(self):
        if self.velocidade == 0:
            print(f'O carro {self.modelo} do ano {self.ano} está parado')
        elif self.velocidade < self.vmMAX:
            print(f'O carro {self.modelo} esta indo a {self.velocidade} km/h')
        else:
            print(f'O carro {self.modelo} está andando no talo a {self.velocidade} km/h')

    def acelerar(self, aceleracao = 10 ):
        self.velocidade += aceleracao
        self.imprime()

    def freiar(self,frenagem = 5):
        if self.velocidade > frenagem:
            self.velocidade -= frenagem
        else:
            self.velocidade = 0
        self.imprime()
        

    def parar(self):
        self.velocidade = 0
        self.imprime()
    
main()