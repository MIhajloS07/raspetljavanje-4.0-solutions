import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()

# Ovde napisi svoju funkciju
def nacrtaj_kucu(x, y):
    # Crtanje kuce
    pygame.draw.rect(screen, (40, 35, 0), (x, y, 120 , 100))
    # Koordinate za polygon -> crtanje krova
    points = [(x, y-30), (x-30, y), (x+30, y)]
    pygame.draw.polygon(screen, (253, 188, 7), points)
    # Crtanje vrata
    pygame.draw.rect(screen, (31, 31, 28), (x + 40, y + 60, 40 , 40))   
                     
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Testiraj funkciju - nacrtaj dve kuce
    nacrtaj_kucu(100, 200)
    nacrtaj_kucu(300, 300)

    # Azuriraj prozor
    pygame.display.flip()

    # Ogranici na 60 FPS
    clock.tick(60)

pygame.quit()

