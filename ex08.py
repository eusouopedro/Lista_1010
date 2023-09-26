class Macaco:
    def __init__(self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho
    def comer(self, comida):
        (self.bucho).append(comida)
    def verBucho(self):
        for comida in self.bucho:
            print(comida)
    def digerir(self):
        (self.bucho).pop(0)

maucaco = Macaco("maucaco")
george = Macaco("George")

george.comer(maucaco)

george.verBucho()
