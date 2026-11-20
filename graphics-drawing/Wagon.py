import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

def nacrtaj_vagon(x, y, boja_vagona):
    # Telo vagona
    pygame.draw.rect(screen, boja_vagona, (x, y - 25, 70, 25))
    # Tockovi
    pygame.draw.circle(screen, (0, 0, 0), (x + 15, y), 7)
    pygame.draw.circle(screen, (0, 0, 0), (x + 55, y), 7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 250))

    pygame.draw.line(screen, (100, 100, 100), (0, 260), (400, 260), 5)

    # Тест вагона
    nacrtaj_vagon(80, 250, (30, 144, 255))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
