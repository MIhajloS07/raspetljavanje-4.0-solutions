import pygame as pg
from pygame.math import Vector2

pg.init()

# konstante
WIDTH = 800
HEIGHT = 600
FPS = 60
RED_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock() 

poz = Vector2(WIDTH // 2, HEIGHT // 2)
brzina = Vector2(2, 1.5)
velicina = Vector2(120, 60)
ugao = 270
brzina_rotacije = 1

def update():
    global poz, brzina, ugao
    poz += brzina
    if poz.x - velicina.x/2 < 0 or poz.x + velicina.x/2 > WIDTH:
        brzina.x *= -1
    if poz.y - velicina.y/2 < 0 or poz.y + velicina.y/2 > HEIGHT:
        brzina.y *= -1
    ugao += brzina_rotacije

def draw():
    screen.fill(BLACK_COLOR)
    centar  = poz
    pol = velicina / 2
    osnovne_tacke = [
        Vector2(-pol.x, -pol.y),  # gornje levo
        Vector2(pol.x, -pol.y),   # gornje desno
        Vector2(pol.x, pol.y),    # donje desno
        Vector2(-pol.x, pol.y)   # donje levo
    ]
    rotirane_tacke = []
    for tacka in osnovne_tacke:
        rotirane_tacke.append(tacka.rotate(ugao))
    nove_tacke = []
    for tacka in rotirane_tacke:
        nove_tacke.append(tacka + centar)
    pg.draw.polygon(screen, RED_COLOR, nove_tacke, width=2)

    # Crtanje tacke u centru
    pg.draw.circle(screen, BLACK_COLOR, (int(centar.x), int(centar.y)), 6)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    update()
    draw()
    pg.display.flip()
    clock.tick(FPS) # 60 FPS - 60 puta se while petlja izvrsava u sekundi
pg.quit()
