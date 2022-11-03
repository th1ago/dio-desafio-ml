'''
Atributod de classe e de instancia
Variaveis de instancia 'e unica POR objeto, cada objeto possui uma copia
Variaveis de classe 'e uniaca PARA todo objeto
'''

class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome= nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Thiago", 1)
aluno2 = Estudante("Taigo", 2)
mostrar_valores(aluno1, aluno2)

Estudante.escola = "Python Unimed"
aluno1.matricula = 3
mostrar_valores(aluno1, aluno2)