import copy
from Fila import *
from Pilha import *
from Tabuleiro import *
from Busca_Largura import *
from busca_Ganho_perda import *

def Automatiza(lista, tab):
    contlinha = 0
    contcoluna = 0
    for linha in lista:
        contcoluna = 0
        for coluna in linha:
            if(coluna == 1):
                tab.Jogada_P(contlinha, contcoluna)
            elif(coluna == -1):
                tab.Jogada_C(contlinha, contcoluna)
            
            contcoluna += 1
        contlinha += 1


def heuristica(tabuleiro):
    pontos = 0
    if tabuleiro.Verifica_Vitoria() == 1:
        return -5000
    if tabuleiro.Verifica_Vitoria() == -1:
        return 50000000000000000000000000000000000
    tabuleiros_possiveis_1 = [copy.deepcopy(tabuleiro).Jogada_C(jogada[0], jogada[1], True)[1] for jogada in tabuleiro.Possiveis_Escolhas()]
    tabuleiros_possiveis_2 = [copy.deepcopy(y).Jogada_P(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_1 for jogada in y.Possiveis_Escolhas() ]
    tabuleiros_possiveis_3 = [copy.deepcopy(y).Jogada_C(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_2 for jogada in y.Possiveis_Escolhas()]
    tabuleiros_possiveis_4 = [copy.deepcopy(y).Jogada_P(jogada[0], jogada[1], True)[1] for y in tabuleiros_possiveis_3 for jogada in y.Possiveis_Escolhas()]

    pontos += Tira_heuristica(tabuleiro)
    pontos += sum([Tira_heuristica(x) for x in tabuleiros_possiveis_1])
    pontos += sum([Tira_heuristica(x) for x in tabuleiros_possiveis_2])
    pontos += sum([Tira_heuristica(x) for x in tabuleiros_possiveis_3])
    pontos += sum([Tira_heuristica(x) for x in tabuleiros_possiveis_4])

    return pontos;
def Tira_heuristica(tabuleiro):
    tab = tabuleiro.Get_tab()
    pontos = 0
    listas = []

    #Verificação Linhas   
    listas.append([sum(linha) for linha in tab])                                #Verificação Horizontal
    listas.append( [ sum([tab[x][y] for x in range(3)]) for y in range(3)])     #Verificação Vertical
    listas.append([ sum(tab[x][x] for x in range(3))])                          #Verificação Diagonal P.
    listas.append([ sum(tab[x][2 - x] for x in range(3))])                      #Verificação Diagonal 

    for lista in listas:
        pontos += -100*lista.count(3)
        pontos += -50*lista.count(2)
        pontos += 100*lista.count(-3)
        pontos += 50*lista.count(-2)

    return pontos
    
    


tab_1 = [[-1, 1, -1],
[-1, 1, 1],
[1, -1, -1]]

tab_2 = [[-1,0,0],
         [0,-1,0],
         [-1,0,0]]

tab_3 = [[-1,0,-1],
         [0,0,0],
         [-1,1,1]]

tab_4 = [[-1,0,0],
         [0,0,0],
         [-1,0,-1]]

tab_5 = [[-1, 0, 1],
[0, -1, 0],
[0, 0, 1]]

tab1 = Tabuleiro()
tab2 = Tabuleiro()
tab3 = Tabuleiro()
tab4 = Tabuleiro()
tab5 = Tabuleiro()

Automatiza(tab_1, tab1)
Automatiza(tab_2, tab2)
Automatiza(tab_3, tab3)
Automatiza(tab_4, tab4)
Automatiza(tab_5, tab5)
# tab2.Mostrar_Tabuleiro()
b = busca_Ganho_perda(tab2)

# tabuleiros_possiveis = [tab1,tab2,tab3,tab4,tab5]
tabuleiros_possiveis = [copy.deepcopy(tab5).Jogada_C(jogada[0], jogada[1], True)[1] for jogada in tab5.Possiveis_Escolhas()]

resultados = [0,0,0,0,0]
testes_heuristica_implementada = [b.heuristica(x)  for x in tabuleiros_possiveis]
testes_nova_heuristica = [heuristica(c) for c in tabuleiros_possiveis]

print("Melhor (implementado): ",testes_heuristica_implementada[testes_heuristica_implementada.index(max(testes_heuristica_implementada))])
[tabuleiros_possiveis[testes_heuristica_implementada.index(max(testes_heuristica_implementada))]][0].Mostrar_Tabuleiro()
# print("Pior:")
# [tabuleiros_possiveis[testes_heuristica_implementada.index(min(testes_heuristica_implementada))]][0].Mostrar_Tabuleiro()


print('-============-')
print("Melhor (Nova Implementacao): ",testes_nova_heuristica[testes_nova_heuristica.index(max(testes_nova_heuristica))])
[tabuleiros_possiveis[testes_nova_heuristica.index(max(testes_nova_heuristica))]][0].Mostrar_Tabuleiro()

# print("Pior:")
# [tabuleiros_possiveis[testes_nova_heuristica.index(min(testes_nova_heuristica))]][0].Mostrar_Tabuleiro()


# print(testes_heuristica_implementada)
