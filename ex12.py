class Conta:
    def __init__(self, num, nome, saldo=0, juros=0):
        self.num = num
        self.nome = nome
        self.saldo = saldo
        self.taxajuros = juros/100
    def alterarNome(self, nnome):
        self.nome = nnome
    def saque(self, valor):
        self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor
    def adicionaJuros(self):
        self.saldo = self.saldo*(1+self.taxajuros)


poupanca = Conta(123, "Pedro", 1000, 10)
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
poupanca.adicionaJuros()
print(f'Saldo atual: {poupanca.saldo}')
