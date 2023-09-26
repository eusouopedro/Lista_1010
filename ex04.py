class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            crescer(0.5)
    def crescer(self, alt):
        self.altura += alt
    def engordar(self, p):
        self.peso += p
    def emagrecer(self, p):
        self.peso -= p
