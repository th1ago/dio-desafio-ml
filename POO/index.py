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

b1 = bike("Vermelha", "caloi", 2022, 300)
b1.buzinar()
b1.parar()
b1.correr()