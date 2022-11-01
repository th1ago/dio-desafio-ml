from numpy import vectorize


class Veiculo():
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print("ligando o motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("red", "123-abc", 2)
print(moto)
moto.ligar_motor()