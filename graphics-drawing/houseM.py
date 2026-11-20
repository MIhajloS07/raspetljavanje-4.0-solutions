import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

BLACK_COLOR = (0, 0, 0)
def nacrtaj_kucu(x, y, sirina, visina, boja_zidova, boja_krova):
    # Pravougaonik za zidove
    pygame.draw.rect(screen, boja_zidova, (x, y, sirina, visina))
    # Trougao za krov
    points = [(x - 20, y), (x + sirina // 2, y - 40), (x + sirina + 20, y)]
    pygame.draw.polygon(screen, boja_krova, points)
    # Pravougaonik za vrata
    pygame.draw.rect(screen, boja_krova, (x + sirina / 2, y + visina / 2, sirina // 3, visina // 2))
    # Dva prozora
    pygame.draw.rect(screen, BLACK_COLOR, (x + 15, y + 7, sirina / 4, visina / 3))
    pygame.draw.rect(screen, BLACK_COLOR, (x + sirina / 1.5, y + 7, sirina / 4, visina / 3))
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))  # Небо

    # Тестирај функцију
    nacrtaj_kucu(100, 100, 120, 100, (255, 228, 196), (139, 69, 19))
    nacrtaj_kucu(300, 180, 150, 120, (255, 255, 200), (200, 0, 0))
    nacrtaj_kucu(500, 220, 100, 80, (200, 200, 255), (100, 100, 100))

    # Трава
    pygame.draw.rect(screen, (0, 200, 0), (0, 400, 800, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()