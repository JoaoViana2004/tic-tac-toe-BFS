import pygame
import sys
from Fila import *
from Pilha import *
from Tabuleiro import *
from Busca_Largura import *

# Inicialização do Pygame
pygame.init()

# Configurações da janela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jogo da Velha')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Fonte
FONT_SIZE = 100
SMALL_FONT_SIZE = 50
font = pygame.font.SysFont(None, FONT_SIZE)
small_font = pygame.font.SysFont(None, SMALL_FONT_SIZE)

# Tabuleiro
tab = Tabuleiro()
tabs = [Tabuleiro(), Tabuleiro()]

# Função para desenhar o tabuleiro
def draw_board(board):
    screen.fill(GRAY)
    x_i, y_i = 50, 100
    tamanho, grossura = 500, 5

    pygame.draw.rect(screen, WHITE, (x_i, y_i, tamanho, tamanho))

    # Desenhar linhas do tabuleiro
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (x_i + i * tamanho // 3, y_i), (x_i + i * tamanho // 3, y_i + tamanho), grossura)
        pygame.draw.line(screen, BLACK, (x_i, y_i + i * tamanho // 3), (x_i + tamanho, y_i + i * tamanho // 3), grossura)

    # Desenhar X e O
    offset = (tamanho // 3) // 3
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                text = font.render('X', True, BLACK)
                screen.blit(text, (x_i + col * tamanho // 3 + offset, y_i + offset + row * tamanho // 3))
            elif board[row][col] == -1:
                text = font.render('O', True, BLACK)
                screen.blit(text, (x_i + col * tamanho // 3 + offset, y_i + offset + row * tamanho // 3))

# Função para desenhar o tabuleiro objetivo
def draw_objective_board(board):
    x_offset, y_offset, board_size = 600, 50, 150

    pygame.draw.rect(screen, WHITE, (x_offset, y_offset, board_size, board_size))

    # Desenhar linhas do tabuleiro
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (x_offset + i * board_size // 3, y_offset), (x_offset + i * board_size // 3, y_offset + board_size), 5)
        pygame.draw.line(screen, BLACK, (x_offset, y_offset + i * board_size // 3), (x_offset + board_size, y_offset + i * board_size // 3), 5)

    # Desenhar X e O
    offset = 10
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                text = small_font.render('X', True, BLACK)
                screen.blit(text, (x_offset + col * board_size // 3 + offset, y_offset + offset + row * board_size // 3))
            elif board[row][col] == -1:
                text = small_font.render('O', True, BLACK)
                screen.blit(text, (x_offset + col * board_size // 3 + offset, y_offset + offset + row * board_size // 3))

# Função para fazer um movimento
def make_move(board, row, col, player):
    if board.Jogada_P(row, col) != "Invalido":
        return True
    return False

# Estado inicial do tabuleiro
initial_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
objective_board = [[-1, 1, 0], [0, -1, 1], [0, 1, -1]]

# Loop principal do jogo
running = True
current_player = 1  # X começa

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_player == 1:  # Movimento do jogador (X)
                x, y = event.pos
                row, col = y // 200, x // 200
                if row < 3 and col < 3:  # Verificar se o clique está dentro do tabuleiro
                    if make_move(tab, row, col, current_player):
                        current_player = -1  # Alternar para O (máquina)
                        print("Vez da Maquina")
            elif current_player == -1:
                tabs = Busca_Largura(tab).Busca()
                tab = tabs[0]
                tabs[1].Mostrar_Tabuleiro()
                current_player = 1  # Alternar para X (Jogador)
                print("Vez do player")

    draw_board(tab.Get_tab())
    draw_objective_board(tabs[1].Get_tab())
    pygame.display.flip()


pygame.quit()
sys.exit()
