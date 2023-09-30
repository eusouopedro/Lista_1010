class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printPonto(self):
        print(f'O ponto possui coordenadas x = {self.x} e y = {self.y}')
    

class Ret:
    def __init__(self, larg, alt, origem):
        self.larg = larg
        self.alt = alt
        self.x0 = origem.x
        self.y0 = origem.y
    
    def printRet(self):
        print(f'O retangulo possui dimensoes {self.larg}x{self.alt}')
    
    def encontraCentro(self):
        xc = self.x0+(self.larg/2)
        yc = self.y0+(self.alt/2)
        print(f'O centro desse retangulo fica no ponto {xc},{yc}')
        return Ponto(xc,yc)
    def alteraTamanho(self, l, h):
        self.larg = l
        self.alt = h

def pegaInfo():
    l = int(input("Qual a largura do Retangulo? "))
    h = int(input("Qual a altura do Retangulo? "))
    return l, h

x = int(input("Quais os valores de x e y da origem do retangulo? x: "))
y = int(input("y: "))
o = Ponto(x, y)
l, h = pegaInfo()
r = Ret(l, h, o)
centro = 0
resposta = 1

while resposta != 3:
    print("Voce pode: ver o tamanho do retangulo(0), alterar o valor dos lados do Retangulo(1), Encontrar o centro do retangulo(2), sair(3)")
    resposta = int(input("O que deseja fazer? "))
    if resposta == 0:
        r.printRet()
    elif resposta == 1:
        l, h = pegaInfo()
        r.alteraTamanho(l,h)
    elif resposta == 2:
        centro = r.encontraCentro()
    elif resposta != 3:
        print("Nao entendi :/")

