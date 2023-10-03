class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def getNome(self):
        return self.nome
    def getSalario(self):
        return self.salario

ze = Funcionario("Ze Lele", 1000)

print(ze.getNome())
print(ze.getSalario())
