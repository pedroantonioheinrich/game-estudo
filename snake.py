import pygame
from time import sleep
from sys import exit
from random import randint


pygame.init() # DÁ INICIO AO PYGAME, É CHAMADO ANTES DE QUALQUER COISA

## DEFINIÇÕES DA TELA
ALTURA = 800
LARGURA = 800
TELA = pygame.display.set_mode((LARGURA, ALTURA)) # CRIA A TELA DE JOGO
pygame.display.set_caption('Snake') # ESCREVE O TITULO NO CANTO SUPERIOR DA JANELA

# CONTROLA O FPS DO JOGO
relogio = pygame.time.Clock() 
FPS = 30 # FRAMES POR SEGUNDO

# CORES
BRANCO = (255,255,255)
PRETO = (0,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
VERMELHO = (255,0,0)
AMARELO = (255,255,0)
CIANO = (0,255,255)
MAGENTA = (255,0,255)
cores = [PRETO, VERDE, AZUL, CIANO, AMARELO, MAGENTA]

# POSIÇÕES DA SNAKE
w_snake = 30  # LARGURA DA SNAKE
h_snake = 30  # ALTURA DA SNAKE
x_snake = (ALTURA / 2) - w_snake
y_snake = (LARGURA / 2) - w_snake
change_direction = False
direction = 'right'

# CORPO DA SNAKE
x_prev_snake = x_snake
y_prev_snake = y_snake


# POSIÇÕES DAS COMIDAS
x_food = randint(50, LARGURA - 50)
y_food = randint(50, ALTURA - 50)
nova_cor = cores[randint(0, len(cores) - 1)]

# PLACAR
pontos = 0
fonte = pygame.font.Font(None, 36) # FONTE SELECIONADA E TAMANHO
fonte1 = pygame.font.Font(None, 36) # FONTE SELECIONADA E TAMANHO




# LOOP PRINCIPAL
while True:
    # CONTROLA A VELOCIDADE DO JOGO
    relogio.tick(FPS) # O LOOP VERIFICA O FPS A CADA ITERAÇÃO
    for evento in pygame.event.get():  # VERIFICA O EVETO DE SAIDA DO JOGO
        if evento.type == pygame.QUIT:
            print("Saindo do jogo...") 
            pygame.quit() # SAIDA DO JOGO
            exit() # SAIDA DO SISTEMA
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                change_direction = True
                direction = 'right'
            elif evento.key == pygame.K_a:
                change_direction = True
                direction = 'left'
            elif evento.key == pygame.K_w:
                change_direction = True
                direction = 'up'
            elif evento.key == pygame.K_s:
                change_direction = True
                direction = 'down'
    
                
            

    # PREENCHER A COR DA TELA
    TELA.fill(VERMELHO) # PREENCHE A COR DA TELA       
    # PRIMEIRO PREENCHE A COR DE BACKGROUND E DEPOIS VEM AS FORMAS GEOMETRICAS 

    # < ----- FORMAS GEOMÉTRICAS----------- >
                    #1 - AONDE VAI SER DESENHADO (TELA)
                    #2 - COR (VERMELHO)
                    #3 - POSIÇÃO (X, Y) DE ONDE ELA VAI APARECER
                    #4 - ALTURA E LARGURA DA FORMA 
    snake = pygame.draw.rect(TELA, BRANCO, (x_snake, y_snake, h_snake,w_snake) )
    
    food = pygame.draw.circle(TELA, nova_cor,(x_food, y_food), 10)
    

    # TODA A LÓGICA MOVIMENTAÇÃO, COLISÕES E ETC... ANTES DE ATUALIZAR A TELA
    # <---- A LOGICA VAI AQUI ---->

    texto1 = fonte1.render("PERDEU...", True, BRANCO) # TEXTO A SER MOSTRADO    
    # POSICIONANDO O TEXTO
    rect_texto1 = texto1.get_rect()
    rect_texto1.center = (400, 400)    

    if x_snake > LARGURA - 30 or x_snake < 0:
        change_direction = False
        x_snake = x_snake
        TELA.blit(texto1, rect_texto1)
        sleep(3)
        break
    elif y_snake > ALTURA - 30 or y_snake < 0:
        change_direction = False
        y_snake = y_snake
        TELA.blit(texto1, rect_texto1)
        sleep(3)
        break
    
    if change_direction != True:
        x_snake = x_snake # QUADRADO ANDA SOZINHO PRA DIREITA
    else:
        if direction == 'right':
            x_snake += 10
        elif direction == 'left':
            x_snake -= 10
        elif direction == 'up':
            y_snake -= 10
        elif direction == 'down':
            y_snake += 10

    # COLISÃO
    if snake.colliderect(food):
        x_food = randint(50, LARGURA - 50)
        y_food = randint(50, ALTURA - 50)   
        if pontos > 10:
            FPS += 5 
        nova_cor = cores[randint(0, len(cores) - 1)]
        print('colidiu com a comida')
        pontos += 1
        print(f"Pontos: {pontos}")

    texto = fonte.render(f"Pontos: {pontos} | Velocidade: {FPS}", True, BRANCO) # TEXTO A SER MOSTRADO    
    # POSICIONANDO O TEXTO
    rect_texto = texto.get_rect()
    rect_texto.center = (600, 50)    
    # DESENHAR O TEXTO NA TELA
    TELA.blit(texto, rect_texto)
                
    

    pygame.display.flip() # ATUALIZA A TELA

    