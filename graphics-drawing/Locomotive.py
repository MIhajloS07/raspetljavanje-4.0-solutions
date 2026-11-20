import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

BLACK_COLOR = (0, 0, 0)
def nacrtaj_lokomotivu(x, y, boja_lokomotive):
    # Telo lokomotive
    pygame.draw.rect(screen, boja_lokomotive, (x, y - 30, 80, 30))
    # Kabina
    pygame.draw.rect(screen, BLACK_COLOR, (x + 50, y - 45, 30, 15))
    # Dimnjak
    pygame.draw.rect(screen, BLACK_COLOR, (x + 10, y - 50, 10, 20))
    # Tockovi
    pygame.draw.circle(screen, BLACK_COLOR, (x + 15, y), 8)
    pygame.draw.circle(screen, BLACK_COLOR, (x + 60, y), 8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 250))  # Небо

    # Шине (видљиве у висини екрана)
    pygame.draw.line(screen, (100, 100, 100), (0, 260), (400, 260), 5)

    # Тест локомотиве
    nacrtaj_lokomotivu(80, 250, (255, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()