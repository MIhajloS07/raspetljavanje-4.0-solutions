import pygame

pygame.init()
screen = pygame.display.set_mode((640, 300))
clock = pygame.time.Clock()

# Овде напиши своју функцију
def nacrtaj_lice(x, y, boja_lica):
    # Glava
    pygame.draw.circle(screen, boja_lica, (x, y), 70)
    # Oci
    pygame.draw.circle(screen, (0, 0, 0), (x - 20, y - 15), 5)
    pygame.draw.circle(screen, (0, 0, 0), (x + 20, y - 15), 5)
    # Usta
    pygame.draw.polygon(screen, (0, 0, 0), [(x - 30, y + 10), (x + 30, y + 10), (x, y + 20)])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Тестирај функцију - нацртај три лица
    nacrtaj_lice(150, 200, (255, 255, 0))  # Жуто лице
    nacrtaj_lice(300, 200, (255, 200, 150)) # Беж лице
    nacrtaj_lice(450, 200, (200, 255, 200)) # Светло зелено

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
