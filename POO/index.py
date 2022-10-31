class bike:
    #self uma referencia para o objeto, argumento
    #essa 'e a instancia do objeto que foi passado
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Bibi")
    
    def parar(self):
        print("stop")
    
    def correr(self):
        print("run")

    #representacao de classe
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = bike("Vermelha", "caloi", 2022, 300)
print(b1)