from Tabuleiro import *

class Fila():
    def __init__(self, t):
        self.tamanho = t
        self.fila =[ 0 for x in range(t)]
        self.inicio = 0
        self.final = -1
        self.num_elementos = 0
    
    def Primeiro(self):
        if(self.num_elementos == 0):
            print("Fila Vazia")
            return None
        return self.fila[self.inicio]
    
    def Enfileirar(self, p):
        if(self.tamanho == self.num_elementos):
            print("Fila Cheia")
            return None
        self.final+=1
        self.fila[self.final] = p

        if(self.final == self.tamanho - 1):
            self.final = -1

        self.num_elementos +=1 

    def Desenfileirar(self):
        if(self.Fila_Vazia()):
            print("Fila Vazia")
            return None
        temp = self.fila[self.inicio]
        self.inicio += 1
        if(self.inicio == self.tamanho):
            self.inicio = 0

        self.num_elementos -=1 
        return temp
        

    def Fila_Cheia(self):
        return self.num_elementos == self.tamanho
    
    def Fila_Vazia(self):
        return self.num_elementos == 0

    def Print_Fila(self):
        ini = self.inicio
        cont = 0
        print("\n(Inicio da Fila)", end="")
        while(cont != self.num_elementos):
            print(f" <-", end ="") 
            self.fila[ini].Mostrar_Tabuleiro()
            print(" ", end="")
            ini += 1
            cont +=1
            if(ini == self.tamanho):
                ini = 0


        print(" (Fim da Fila)")
