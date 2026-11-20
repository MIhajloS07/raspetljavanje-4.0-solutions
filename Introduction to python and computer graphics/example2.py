import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
SAND_COLOR = (221, 207, 156)
GRAY_COLOR = (102, 102, 102)

def nacrtaj_ribicu(x, y, velicina, boja, smer):
    # Telo ribice - elipsa
    pygame.draw.ellipse(screen, boja,
                      (x - velicina, y - velicina//2, velicina*2, velicina))
    # Rep ribice - trougao
    if smer == 'desno':
        # Rep sa desne strane
        points = [(x - velicina, y),
                 (x - velicina - velicina//2, y - velicina//2),
                 (x - velicina - velicina//2, y + velicina//2)]
        # Oko sa desne strane
        pygame.draw.circle(screen, BLACK_COLOR, (x + velicina // 2, y), 8)
    else:
        # Rep sa leve strane
        points = [(x + velicina, y),
                 (x + velicina + velicina//2, y - velicina//2),
                 (x + velicina + velicina//2, y + velicina//2)]
        # Oko sa leve strane
        pygame.draw.circle(screen, BLACK_COLOR, (x - velicina // 2, y), 8)
    pygame.draw.polygon(screen, boja, points)


def nacrtaj_mehuric(x, y, velicina):
    # Mehuric - plavi krug
    pygame.draw.circle(screen, BLUE_COLOR, (x, y), velicina)
    # Mali kruzic kao odsjaj od mehurica
    pygame.draw.circle(screen, WHITE_COLOR, (x - velicina // 2, y - velicina // 3), velicina % 10)

def nacrtaj_algu(x, y, visina):
    # Alga - nekoliko zelenih cik cak preklapajucih pravougaonika
    # leva strana (razlicite nijanse listova)
    pygame.draw.rect(screen, (25, 80, 4), (x, y - 50, 10, visina))
    pygame.draw.rect(screen, (55, 171, 9), (x + 10, y - 30, 10, visina))
    pygame.draw.rect(screen, GREEN_COLOR, (x + 20, y - 10, 10, visina))
    pygame.draw.rect(screen, (94, 168, 64), (x + 30, y + 10, 10, visina))
    # desna strana - malo bude nepravilna kako nebi bile bas simetricne (razlicite nijanse listova)
    pygame.draw.rect(screen, GREEN_COLOR, (x + 60, y - 50, 10, visina))
    pygame.draw.rect(screen, (94, 168, 64), (x + 50, y - 30, 10, visina))
    pygame.draw.rect(screen, (25, 80, 4), (x + 45, y - 10, 10, visina))
    pygame.draw.rect(screen, (55, 171, 9), (x + 40, y + 10, 10, visina))
    # sredisnji list 
    pygame.draw.rect(screen, GREEN_COLOR, (x + 30, y - 30, 10, visina))

def nacrtaj_pesak():
    # Pesak na dnu - zuti/bez pravougaonik
    pygame.draw.rect(screen, SAND_COLOR, (0, HEIGHT / 1.3, WIDTH, HEIGHT // 3))
    # Kamencici u pesku
    pygame.draw.circle(screen, GRAY_COLOR, (30, HEIGHT - 50), 18)
    pygame.draw.circle(screen, GRAY_COLOR, (250, HEIGHT - 80), 13)
    pygame.draw.circle(screen, GRAY_COLOR, (500, HEIGHT - 25), 20)
    pygame.draw.circle(screen, GRAY_COLOR, (690, HEIGHT - 100), 24)
    pygame.draw.circle(screen, GRAY_COLOR, (760, HEIGHT - 15), 10)


def ispitaj_poziciju_ribica(pozicija):
    if pozicija > WIDTH + 300:
        pozicija = -170
    elif pozicija < -170:
        pozicija = WIDTH
    return pozicija

def ispitaj_poziciju_mehura(pozicija):
    if pozicija < -300:
        pozicija = HEIGHT
    return pozicija

# brzina kretanja ribica ( X osa )
brzina_ribice_x_desno = 0
brzina_ribice_x_levo = 0
y_mehur = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Plava pozadina
    screen.fill((0, 100, 150))

    brzina_ribice_x_desno += 3
    brzina_ribice_x_levo -= 2
    y_mehur -=1
    
    # Pozivanje funkcija za ispitivanje pozicije
    brzina_ribice_x_desno = ispitaj_poziciju_ribica(brzina_ribice_x_desno)
    brzina_ribice_x_levo = ispitaj_poziciju_ribica(brzina_ribice_x_levo)
    y_mehur = ispitaj_poziciju_mehura(y_mehur)

    # Iscrtavanje peska
    nacrtaj_pesak()
    # Crtanje mehurica
    nacrtaj_mehuric(39, y_mehur + 50, 25)
    nacrtaj_mehuric(100, y_mehur - 100, 21)
    nacrtaj_mehuric(500, y_mehur + 230, 49)
    nacrtaj_mehuric(720, y_mehur - 89, 35)
    nacrtaj_mehuric(700, y_mehur, 13)
    # Crtanje ribica
    nacrtaj_ribicu(brzina_ribice_x_desno + 100, 150, 50, (255,0,0), "desno")
    nacrtaj_ribicu(brzina_ribice_x_levo + 50, 250, 50, (255,170,0), "levo")
    nacrtaj_ribicu(brzina_ribice_x_levo - 80, 400, 50, (25,0,34), "levo")
    nacrtaj_ribicu(brzina_ribice_x_desno + 200, 30, 50, (34,34,34), "desno")
    nacrtaj_ribicu(brzina_ribice_x_desno - 150, 300, 50, (255,234,90), "desno")
    # Alge
    nacrtaj_algu(50, 500, 20)
    nacrtaj_algu(150, 430, 75)
    nacrtaj_algu(280, 530, 50)
    nacrtaj_algu(390, 520, 38)
    nacrtaj_algu(510, 450, 110)
    nacrtaj_algu(600, 450, 43)

    # Text za prikaz broja slicica u sekundi (FPS)
    text = pygame.font.SysFont("Calibri", 32, bold=False, italic=False)
    text_surface = text.render(f"Fps: {round(clock.get_fps(), 0)}", True, (0, 255, 0))
    screen.blit(text_surface, (50, 50))

    pygame.display.flip()
    clock.tick(60) # 60FPS
pygame.quit()