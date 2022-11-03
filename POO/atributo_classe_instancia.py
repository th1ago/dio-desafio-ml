class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome= nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

aluno1 = Estudante("Thiago", 1)
aluno2 = Estudante("Taigo", 2)

print(aluno1)
print(aluno2)