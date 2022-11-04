import abc

class ControleRemoto():
    pass

    def ligar(self):
        pass
    
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
    
    def desligando(self):
        print("Desligando TV")