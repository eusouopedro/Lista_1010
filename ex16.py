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

    def alimentar(self, f):
        if self.fome >= 0:
            self.fome -= f

    def setSaude(self, s):
        self.saude = s

    def cuidar(self, s):
        if self.saude <=100:
            self.saude += s

    def setIdade(self, i):
        self.idade = i
r = 0
tamagushi = Tamagushi("Fofinho", 40, 30, 3)
while True:
    print(f'Voce tem um Tamagushi, o nome dele eh {tamagushi.getNome()}')
    print('Voce pode brincar com ele(1), alimenta-lo(2), cuidar dele(3) ou sair(4)')
    r = int(input("O que deseja fazer? "))
    if r == 4:
        break
    elif r == 1:
        r = int(input("Por quanto tempo deseja brincar com ele[min]? "))
        if r > 60:
            r = 60
        tamagushi.cuidar(r/2)
        tamagushi.alimentar(r/2)
    elif r == 2:
        r = int(input("Quanto de comida deseja dar a ele? "))
        if r > 60:
            r = 60
        tamagushi.alimentar(r)
    elif r == 3:
        tamagushi.cuidar(50)

    elif r == 0:
        print(f"Voce tem um Tamagushi!!\nO nome dele é {tamagushi.getNome()}, ele tem {tamagushi.getIdade()} anos e esta com {tamagushi.getFome()} de fome, {tamagushi.getSaude()} de saude e {tamagushi.getHumor()} de humor")
    else:
        print("Nao entendi :/")
