class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def getNome(self):
        return self.nome
    def getSalario(self):
        return self.salario
    def aumentarSalario(self, aumento):
        self.salario = self.salario*(1+aumento/100)

ze = Funcionario("Ze Lele", 1000)

print(ze.getNome())
print(ze.getSalario())
ze.aumentarSalario(10)
print(ze.getSalario())
