class Ret:
    def __init__(self, base, alt):
        self.base = base
        self.alt = alt
    
    def setLados(self, nbase, nalt):
        self.base = nbase
        self.alt = nalt
    
    def getLados(self):
        return self.base, self.alt

    def calcArea(self):
        return (self.base*self.alt)

    def calcPerim(self):
        return(2*self.base+2*self.alt)

print("Para calcular a quantidade de pisos e rodapés necessários informe:")
b = int(input("O comprimento do local: "))
h = int(input("A largura do local: "))
local = Ret(b, h)
print(f'Serao necessarios {local.calcArea()}m2 de piso e {local.calcPerim()}m de rodape')
