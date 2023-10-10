class Tamagushi:
    def __init__(self, nome, fome, saude, idade, lista):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        lista.append(self)

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
t = -1
lista = []
nomes = ""
t1 = Tamagushi("Fofinho", 40, 30, 3, lista)
t2 = Tamagushi("Coisinha", 10, 50, 2, lista)

for t in lista:
    nomes += t.getNome()+", "

while True:
    print(f'Voce tem {len(lista)} Tamagushis, os nomes deles sao {nomes}')
    r = int(input("Com qual deles voce deseja interagir(escolha o numero dele[0 para sair])? "))
    if r == 0:
        break
    while 1:
        try:
            t = lista[r-1]
            break
        except:
            print("Nao conheco esse tamagushi :(")
            print(f'Voce tem {len(lista)} Tamagushis, os nomes deles sao {nomes}')
            r = int(input("Com qual deles voce deseja interagir(escolha o numero dele)? "))
    print(f"Voce escolheu o {t.getNome()}!")
    
    print('Voce pode brincar com ele(1), alimenta-lo(2), cuidar dele(3) ou sair(4)')
    r = int(input("O que deseja fazer? "))
    if r == 4:
        break
    elif r == 1:
        r = int(input("Por quanto tempo deseja brincar com ele[min]? "))
        if r > 60:
            r = 60
        t.cuidar(r/2)
        t.alimentar(r/2)
    elif r == 2:
        r = int(input("Quanto de comida deseja dar a ele? "))
        if r > 60:
            r = 60
        t.alimentar(r)
    elif r == 3:
        t.cuidar(50)

    elif r == 0:
        print(f"O nome dele é {t.getNome()}, ele tem {t.getIdade()} anos e esta com {t.getFome()} de fome, {t.getSaude()} de saude e {t.getHumor()} de humor")
    
    else:
        print("Nao entendi :/")
