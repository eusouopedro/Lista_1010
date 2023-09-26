class Bola:
    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.circ = circ
        self.mat = mat
    def trocaCor(self, ncor):
        self.cor = ncor
    def mostraCor(self):
        print(self.cor)
