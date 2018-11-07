# importamos os modulos necessarios
import pygame

pygame.init() # iniciamos o modulo pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height)) #criando janela

pygame.display.set_caption("Bunker Exile") #nomeando o jogo

#dimencoes do futuro personagem
x = 50
y = 40
widthFigure = 32
heightFigure = 64
vel = 5

screenWidth = width - widthFigure - vel
screenHeigth = height - heightFigure - vel 

isJump = False
jumpCount = 10



run = True

#loop do jogo
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False

    keys =  pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenWidth:
        y += vel
    if keys[pygame.K_SPACE]:
        isJump = True
        

    win.fill((0, 0, 0,))
    pygame.draw.rect(win, (255, 0, 0), (x, y, widthFigure, heightFigure)) #chama o futuro jogador
    pygame.display.update() #atualiza o jogo

pygame.quit()
