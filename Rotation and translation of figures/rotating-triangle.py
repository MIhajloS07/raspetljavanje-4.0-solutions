import pygame as pg
from pygame.math import Vector2

pg.init()
# const
SCREEN_W = 800
SCREEN_H = 600
FPS = 60

screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
clock = pg.time.Clock()

poz = Vector2(SCREEN_W // 2, SCREEN_H // 2)
velicina = Vector2(100, 100)
brzina = Vector2(2, 1.5)
ugao = 45
brzina_rotacije = 1

def update():
    global poz, brzina, ugao
    poz += brzina
    if poz.x - velicina.x/2 < 0 or poz.x + velicina.x > SCREEN_W:
        brzina.x = -brzina.x
    if poz.y - velicina.y/2 < 0 or poz.y + velicina.y > SCREEN_H:
        brzina.y = -brzina.y
    ugao += brzina_rotacije

def draw():
    screen.fill((0, 0, 0))
    centar = poz
    pol = velicina / 2
    osnovne_tacke = [
        Vector2(-pol.x, -pol.y), # gore levo
        Vector2(pol.x, -pol.y),  # gore desno
        Vector2(velicina.x // 2, pol.y),  # dole levo
        # Vector2(+pol.x, pol.y)   # dole desno
    ]

    rotirane_tacke = []
    for tacka in osnovne_tacke:
        rotirane_tacke.append(tacka.rotate(ugao))
    nove_tacke = []
    for tacka in rotirane_tacke:
        nove_tacke.append(tacka + centar)
    pg.draw.polygon(screen, (255, 190, 0), nove_tacke, width=3)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    update()
    draw()

    pg.display.flip()
    clock.tick(FPS)
pg.quit()