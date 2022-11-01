# quando se tem o _saldo - se torna  privado

class Conta:
    def __init__(self, saldo = 0):
        self._saldo = saldo

    def depositar(self, valor):
        pass
    
    def sacar(self, valor):
        pass