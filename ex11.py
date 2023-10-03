class Carro:
    def __init__(self, consumo, tanque=0):
        self.consumo = consumo
        self.tanque = tanque

    def obterGasolina(self):
        return self.tanque

    def abastecer(self, qnt):
        self.tanque += qnt

    def andar(self, dist):
        if self.tanque>(dist/self.consumo):
            self.tanque -= (dist/self.consumo)
            print(f'O carro andou {dist}km')
        else:
            print("Combustivel insuficiente")

