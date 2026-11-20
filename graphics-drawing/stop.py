import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

RED_COLOR = (255, 0, 0)
WHITE_COLOR = (255, 255, 255)

# Овде напиши своју функцију
# def nacrtaj_stop_znak(x, y, velicina):
#     # Crveni pravougaonik
#     pygame.draw.circle(screen, RED_COLOR, (x, y), velicina)
#     # Beli okvir
#     pygame.draw.circle(screen, WHITE_COLOR, (x, y), velicina, 5)
#     # Tekst "STOP" u sredini
#     text = pygame.font.SysFont("Calibri", 32, bold=True)
#     text_surface = text.render("STOP", True, WHITE_COLOR)
#     text_rect = text_surface.get_rect()
#     text_rect.center = (x, y)
#     screen.blit(text_surface, (text_rect.x, text_rect.y))

def nacrtaj_stop_znak(x, y, velicina):
    # Бела ивица
    pygame.draw.rect(screen, (255, 255, 255),
                   (x - velicina//2 - 5, y - velicina//2 - 5,
                    velicina + 10, velicina + 10))

    # Црвени знак
    pygame.draw.rect(screen, (255, 0, 0),
                   (x - velicina//2, y - velicina//2,
                    velicina, velicina))

    # Текст
    font = pygame.font.SysFont(None, velicina // 3)
    text = font.render("STOP", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, (text_rect.x, text_rect.y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))  # Плаво небо

    # Тестирај функцију
    nacrtaj_stop_znak(150, 200, 80)
    nacrtaj_stop_znak(300, 200, 100)
    nacrtaj_stop_znak(450, 200, 60)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
