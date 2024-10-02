from Tabuleiro import *

class Vetor_Ordenado:
    def __init__(self):
        self.vec = []
    
    def Get_Vetor(self):
        return self.Sorteia(self.vec)
    
    def Insere_Vetor(self, element):
        self.vec.append(element)
        self.Sorteia()

        return self.vec
    
    def Get_Menor(self):
        self.Sorteia()
        return self.vec[0]
    
    def Sorteia(self):
        self.vec = sorted(self.vec,key=lambda tab: len(tab.Get_Historico()))
        return self.vec