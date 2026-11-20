import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

BLACK_COLOR = (0, 0, 0)
# Овде напиши своју функцију
def nacrtaj_balon(x, y, boja_balona, velicina):
    # Krug
    pygame.draw.circle(screen, boja_balona, (x,y), velicina)
    # Linija za konac
    pygame.draw.line(screen, BLACK_COLOR, (x, y + velicina), (x, y + 60), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((200, 230, 255))

    # Тестирај функцију - нацртај неколико балона
    nacrtaj_balon(100, 150, (255, 0, 0), 40)     # Црвени
    nacrtaj_balon(200, 100, (0, 255, 0), 50)     # Зелени
    nacrtaj_balon(300, 180, (0, 0, 255), 35)     # Плави
    nacrtaj_balon(400, 120, (255, 255, 0), 45)   # Жути
    nacrtaj_balon(500, 160, (255, 0, 255), 40)   # Љубичасти

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
