from Fila import *
from Pilha import *
from Tabuleiro import *
from Busca_Largura import *
from busca_Ganho_perda import *

tab = Tabuleiro()
comeco = int(input("Quem começa ?\n(1) - Player\n(2) - PC\nSua escolha: "))
tab.Mostrar_Tabuleiro()
print("=========")
if(comeco == 2):
    tab.Set_Vez(-1)
    while tab.Verifica_Vitoria() == 0:
        tab = busca_Ganho_perda(tab).Busca()[0]
        tab.Mostrar_Tabuleiro()
        if(tab.Verifica_Vitoria() != 0):
            break
        x = int(input("\nDefina sua Jogada em Linha (0,2): "))
        y = int(input("Defina sua Jogada em Coluna (0,2): "))
        tab.Jogada_P(x,y)
        tab.Mostrar_Tabuleiro()
        print()
else:
    tab.Set_Vez(1)
    while tab.Verifica_Vitoria() == 0:
        x = int(input("\nDefina sua Jogada em Linha (0,2): "))
        y = int(input("Defina sua Jogada em Coluna (0,2): "))
        tab.Jogada_P(x,y)
        tab.Mostrar_Tabuleiro()
        if(tab.Verifica_Vitoria() != 0):
            break
        
        tab = busca_Ganho_perda(tab).Busca()[0]
        tab.Mostrar_Tabuleiro()
        print()



print("Status do Jogo: ", tab.Verifica_Vitoria())




