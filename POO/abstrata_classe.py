'''
Definindo classes abstratas
'''

from abc import ABC, abstractmethod

class ControleRemoto():
    pass

    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
    
    def desligar(self):
        print("Desligando TV")

controle = ControleTV()
controle.ligar()
controle.desligar()