from Fila import *
from Pilha import *
from Tabuleiro import *
from Busca_Largura import *

tab = Tabuleiro()


while True:
    if(tab.Verifica_Vitoria() != 0):
        print(f"Status do Jogo: {tab.Verifica_Vitoria()}\n")
        break
    tab.Mostrar_Tabuleiro()
    x = int(input("\nDefina sua Jogada em Linha (0,2): "))
    y = int(input("Defina sua Jogada em Coluna (0,2): "))

    tab.Jogada_P(x,y)

    tab = Busca_Largura(tab).Busca()

tab.Mostrar_Tabuleiro()




