from Tabuleiro import *

class Pilha():
    def __init__(self, t):
        self.tamanho = t
        self.pilha =[ 0 for x in range(t)]
        self.topo = 0
        self.num_elementos = 0
    
    def Topo(self):
        if(self.Pilha_Vazia()):
            print("Pilha Vazia")
            return None
        return self.pilha[self.topo]
    
    def Empilhar(self, p):
        if(self.Pilha_Cheia()):
            print("Pilha Cheia")
            return None
        self.pilha[self.topo] = p
        self.topo+=1


    def Desempilhar(self):
        temp = self.pilha[self.topo-1]
        self.topo -= 1

        return temp
        

    def Pilha_Cheia(self):
        return self.topo == self.tamanho
    
    def Pilha_Vazia(self):
        return self.topo == 0

    def Print_Pilha(self):
        print("(Embaixo da Pilha) ", end="")
        for x in range(self.topo):
            print(f"{self.pilha[x].Mostrar_Tabuleiro()} -> ", end="")
        print("(Emcima da Pilha)")
