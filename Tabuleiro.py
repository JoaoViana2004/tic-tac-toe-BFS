class Tabuleiro:
    def __init__(self):
        self.tab = [ [0 for x in range(3)] for y in range(3)]
        self.vez = 1
        self.historico = []
    
    def Jogada_P(self, x,y):
        if(self.tab[x][y] != 0):
            print(f"Jogada Invalida Player: ({x},{y}) ")
            return -1
        self.tab[x][y] = 1

        self.vez *= -1

        return self.Verifica_Vitoria()    

    def Jogada_C(self, x,y):
        if(self.tab[x][y] != 0):
            print(f"Jogada Invalida Computador: ({x},{y}) ")
            return -1
        self.tab[x][y] = -1
        self.vez *= -1


        return self.Verifica_Vitoria()
    
    def Mostrar_Tabuleiro(self):
       for x in self.tab:
           print(x)

    def Limpar_Tabuleiro(self):
        self.tab = [ [0 for x in range(3)] for y in range(3)]

    def Verifica_Vitoria(self):
        if(sum([self.Verifica_Vitoria_Horizontal(x,1) for x in range(3)]) >= 1 or sum([self.Verifica_Vitoria_Vertical(x,1) for x in range(3)]) >= 1 or self.Verifica_Vitoria_Diagonal(1)  ):
            # print("Vitoria do Jogador")
            return 1;
        if(sum([self.Verifica_Vitoria_Horizontal(x,-1) for x in range(3)]) >= 1 or sum([self.Verifica_Vitoria_Vertical(x,-1) for x in range(3)]) >= 1 or self.Verifica_Vitoria_Diagonal(-1)  ):
            # print("Vitoria da Maquina")
            return -1;
        if(self.Tabuleiro_Cheio()):
            # print("Empate")
            return 2
        # print("Jogo Rolando")
        return 0;
          
    def Verifica_Vitoria_Horizontal(self, h, z):
        return sum([self.tab[h][x] for x in range(3)]) == 3*z
    
    def Verifica_Vitoria_Vertical(self, h,z):
        return sum([self.tab[x][h] for x in range(3)]) == 3*z
    
    def Verifica_Vitoria_Diagonal(self, z):
        return sum([self.tab[x][x] for x in range(3)]) == 3*z or (self.tab[0][2] == self.tab[1][1] == self.tab[2][0] == z)
    
    def Tabuleiro_Cheio(self):
        return sum([self.tab[x][y] != 0 for x in range(3) for y in range(3)]) == 9

    def Possiveis_Escolhas(self):
        return [(x,y) for x in range(3) for y in range(3) if self.tab[x][y] == 0]

    def Jogada_Verificada(self):
        self.visitado = True;
    
    def Get_Visitado(self):
        return self.visitado
    
    def Get_Vez(self):
        return self.vez
    
    def Escreve_Historico(self, x, y):
        self.historico.append((x,y))

    def Get_Historico(self):
        return self.historico