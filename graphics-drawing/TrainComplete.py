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

def nacrtaj_vagon(x, y, boja_vagona):
    # Telo vagona
    pygame.draw.rect(screen, boja_vagona, (x, y - 25, 70, 25))
    # Tockovi
    pygame.draw.circle(screen, (0, 0, 0), (x + 15, y), 7)
    pygame.draw.circle(screen, (0, 0, 0), (x + 55, y), 7)

def nacrtaj_voz(x, y, broj_vagona, boja_lokomotive):
    # Твој код овде
    # Позвати горње две функције и сложити композицију
    nacrtaj_lokomotivu(x, y, boja_lokomotive)
    razmak = 10
    sirina_lokomotive = 80
    sirina_vagona = 70

    start_vagoni = x + sirina_lokomotive + razmak
    for i in range(broj_vagona):
        vx = start_vagoni + i * (sirina_vagona + razmak)
        nacrtaj_vagon(vx, y, boja_lokomotive)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 250))

    pygame.draw.line(screen, (100, 100, 100), (0, 260), (400, 260), 5)

    # Пример позива
    nacrtaj_voz(60, 250, 3, (255, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()