class Tv:
    def __init__(self, volume=0, canal=1):
        self.volume = volume
        self.canal = canal
    
    def trocaCanal(self, c):
        if (canal > 0) and (canal < 100):
            self.canal = c
        else: print("Canal informado invalido")

    def trocaVolume(self, v):
        if (v => 0) and (v <= 100):
            self.volume = v
        else: print("Volume informado invalido")

tv = Tv()
Tv.trocaCanal(54)
