import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

BROWN_COLOR = (141, 111, 100)
GREEN_COLOR = (0, 255, 0)
def nacrtaj_jabuku(x, y, velicina, boja):
    # Krug za telo jabuke
    pygame.draw.circle(screen, boja, (x, y), velicina)
    # Pravougaonik za peteljku
    pygame.draw.rect(screen, BROWN_COLOR, (x - 3, y - velicina - 15, 6, 30))
    # Zeleni listic krug - moze i trougao
    pygame.draw.circle(screen, GREEN_COLOR, (x + 5, y - velicina // 2 - 18), 7)
    # pygame.draw.polygon(screen, (0, 200, 0), [(x+3, y - velicina), (x+3, y - velicina - 15), (x + 8, y - velicina - 15)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Нацртај корпу воћа
    nacrtaj_jabuku(150, 200, 40, (255, 0, 0))      # Црвена
    nacrtaj_jabuku(250, 200, 45, (0, 255, 0))      # Зелена
    nacrtaj_jabuku(350, 200, 35, (255, 215, 0))    # Златна
    nacrtaj_jabuku(450, 200, 50, (255, 100, 100))  # Розе

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
