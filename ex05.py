class Conta:
    def __init__(self, num, nome, saldo=0):
        self.num = num
        self.nome = nome
        self.saldo = saldo
    def alterarNome(self, nnome):
        self.nome = nnome
    def saque(self, valor):
        self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor
  