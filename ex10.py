class BombaDeCombustivel:
    def __init__(self,tipoCombustivel, valorLitro, qntCombustivel):
        self.tipo = tipoCombustivel
        self.valor = valorLitro
        self.qnt = qntCombustivel

    def abastecerValor(self, valor):
        q = valor/self.valor
        self.qnt -= q
        print(f'Foram abastecidos {q}L de {self.tipoCombustivel}')

    def abastecerLitro(self, litro):
        p = litro*self.valor
        self.qnt -= litro
        print(f'Foram abastecidos {p} de {self.tipoCombustivel}')

    def alterarValor(self, valor):
        self.valor = valor

    def alterarCombustivel(self, tipo):
        self.tipo = tipo

    def alterarQuantidade(self, qnt):
        self.qnt = qnt
