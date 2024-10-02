import copy
import random
from Fila import *
from Tabuleiro import *

class busca_Ganho_perda():
    def __init__(self, obj):
        self.fronteira = Fila(100000)
        self.estado_inicial = obj
        self.fronteira.Enfileirar(obj)
        

    # Função Heuristica

    #Esta funciona pegando 2 camadas de jogo no futuro e tirando a heuristica das mesmas, a fimde procurar a melhor ou pior situação
    #Visto que caso seja a rodada do player, a situação com menor heurística será considerada como a melhor jogada do mesmo
    #Caso seja rodada do Computador, a melhor heuritica será a melhor jogada do mesmo

    def heuristica(self, tabuleiro):
        pontos = 0
        if tabuleiro.Verifica_Vitoria() == 1:
            return -5000  #Valor de Retorno caso o jogo esteja Perdido
        if tabuleiro.Verifica_Vitoria() == -1:
            return 50000000000000000000000000000000000 #Valor de Retorno caso o jogo esteja Ganho
        tabuleiros_possiveis_1 = [copy.deepcopy(tabuleiro).Jogada_C(jogada[0], jogada[1], True)[1] for jogada in tabuleiro.Possiveis_Escolhas()]
        tabuleiros_possiveis_2 = [copy.deepcopy(y).Jogada_P(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_1 for jogada in y.Possiveis_Escolhas() ]
        tabuleiros_possiveis_3 = [copy.deepcopy(y).Jogada_C(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_2 for jogada in y.Possiveis_Escolhas()]
        tabuleiros_possiveis_4 = [copy.deepcopy(y).Jogada_P(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_3 for jogada in y.Possiveis_Escolhas()]

        pontos += self.Tira_heuristica(tabuleiro)
        pontos += sum([self.Tira_heuristica(x) for x in tabuleiros_possiveis_1])
        pontos += sum([self.Tira_heuristica(x) for x in tabuleiros_possiveis_2])
        pontos += sum([self.Tira_heuristica(x) for x in tabuleiros_possiveis_3])
        pontos += sum([self.Tira_heuristica(x) for x in tabuleiros_possiveis_4])

        return pontos;

    def Tira_heuristica(self, tabuleiro):
        tab = tabuleiro.Get_tab()
        pontos = 0
        listas = []

        #Verificação Linhas   
        listas.append([sum(linha) for linha in tab])                                #Verificação Horizontal
        listas.append( [ sum([tab[x][y] for x in range(3)]) for y in range(3)])     #Verificação Vertical
        listas.append([ sum(tab[x][x] for x in range(3))])                          #Verificação Diagonal P.
        listas.append([ sum(tab[x][2 - x] for x in range(3))])                      #Verificação Diagonal 


        #Caso haja o numero 2 ou -2 , significa que em alguma somatória houve a sitiação: [1,0,1] ou [-1,0,-1], assim representando duas ocorrencias de jogadas na mesma linha podendo ter uma terceira (Que significaria vitoria do mesmo)
        #Caso haja o numero 3, significa que a somatória inteira é do meso numero, ou seja, alguem venceu o joog, por isso um peso maior
        for lista in listas:
            pontos += -100*lista.count(3)
            pontos += -50*lista.count(2)
            pontos += 100*lista.count(-3)
            pontos += 50*lista.count(-2)

        return pontos
        
    
    def Busca(self):
        topo = self.fronteira.Primeiro() #Resquicios da classe de FILA
        self.fronteira.Desenfileirar()

        jogadas_possiveis = topo.Possiveis_Escolhas()
        tabuleiros_possiveis = [copy.deepcopy(topo) for x in range(len(jogadas_possiveis))]
        if(tabuleiros_possiveis == [] or topo.Verifica_Vitoria == -1):  #Caso acabe as jogadas, ou o computador vença
            jogada = topo.Get_Historico()[0]
            self.estado_inicial.Jogada_C(jogada[0], jogada[1])

            return (self.estado_inicial, topo)
        if(topo.Get_Vez() <0): #Vez <0: Rodado do Computador, Vez>0 Rodada do Player
            resultados = [tabuleiros_possiveis[x].Jogada_C(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
            historicos = [tabuleiros_possiveis[x].Escreve_Historico(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
            pontuacoes = [self.heuristica(x) for x in tabuleiros_possiveis]

            self.fronteira.Enfileirar(tabuleiros_possiveis[pontuacoes.index(max(pontuacoes))])

        else:
            resultados = [tabuleiros_possiveis[x].Jogada_P(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))]
            historicos = [tabuleiros_possiveis[x].Escreve_Historico(jogadas_possiveis[x][0],jogadas_possiveis[x][1]) for x in range(len(jogadas_possiveis))] 
            pontuacoes = [self.heuristica(x)  for x in tabuleiros_possiveis]


            self.fronteira.Enfileirar(tabuleiros_possiveis[pontuacoes.index(min(pontuacoes))])

        return self.Busca()