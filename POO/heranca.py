from numpy import vectorize


class Veiculo():
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print("ligando o motor")
    
    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        # herdando as caracteristica do pai com o SUPER
        super().__init__(cor, placa, rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Nao'} estou carregado")

moto = Motocicleta("red", "123-abc", 2)
moto.ligar_motor()

truck = Caminhao("preto", "1234-qwe", 8, True)
truck.ligar_motor()
truck.esta_carregado()
