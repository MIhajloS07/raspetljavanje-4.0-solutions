import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

#Boje
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
WHITE_COLOR = (255, 255, 255)

def nacrtaj_zastavu_srbije(x, y, sirina, visina):
    # Prva pruga -> crvena
    pygame.draw.rect(screen, RED_COLOR, (x, y, sirina, visina))
    # Druga pruga -> plava
    pygame.draw.rect(screen, BLUE_COLOR, (x, y + visina, sirina, visina))
    # Treca pruga -> bela
    pygame.draw.rect(screen, WHITE_COLOR, (x, y + visina * 2, sirina, visina))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 200, 200))

    # Различите величине застава
    nacrtaj_zastavu_srbije(50, 50, 200, 120)
    nacrtaj_zastavu_srbije(300, 100, 150, 90)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()