'''
Metodos de classe estao ligado a classe e nao ao objeto.
Pois recebem um param que aponta para a classe e nao para a instancia do objeto 
'''

class Pessoa:
    def __init__(self, pessoa, idade):
        self.pessoa = pessoa
        self.idade = idade

    # transformar em metodo de classe
    # agora utiliza cls
    @classmethod
    def criar_data_born(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    # nao precisa de contexto de classe 
    # e nem da instancia do objeto
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_data_born(1988, 1, 1, "Thiago")
print(p)