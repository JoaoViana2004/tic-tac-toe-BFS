import copy
import random
from Fila import *
from Tabuleiro import *

class Busca_Largura():
    def __init__(self, obj):
        self.fronteira = Fila(10000)
        self.estado_inicial = obj
        self.fronteira.Enfileirar(obj)
    
    def Busca(self):
        topo = self.fronteira.Primeiro()

        self.fronteira.Desenfileirar()
        jogadas_possiveis = topo.Possiveis_Escolhas()
        tabuleiros_possiveis = [copy.deepcopy(topo) for x in range(len(jogadas_possiveis))]
        if(topo.Get_Vez() <0):
            resultados = [tabuleiros_possiveis[x].Jogada_C(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
            historicos = [tabuleiros_possiveis[x].Escreve_Historico(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
        else:
            resultados = [tabuleiros_possiveis[x].Jogada_P(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
            historicos = [tabuleiros_possiveis[x].Escreve_Historico(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]

             
        
        if -1 in resultados:
            jogada = tabuleiros_possiveis[resultados.index(-1)].Get_Historico()[0]
            self.estado_inicial.Jogada_C(jogada[0], jogada[1])

            return self.estado_inicial 

        else:        
            for y in tabuleiros_possiveis:
                    y.Jogada_Verificada()
                    self.fronteira.Enfileirar(y)
        return self.Busca()
        
            

        