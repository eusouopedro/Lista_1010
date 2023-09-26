class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome
    
    def getSaude(self):
        return self.saude
    
    def getIdade(self):
        return self.idade

    def getHumor(self):
        return (self.saude+self.fome)

    def setNome(self, n):
        self.nome = n

    def setFome(self, f):
        self.fome = f

    def setSaude(self, s):
        self.saude = s

    def setIdade(self, i):
        self.idade = i
