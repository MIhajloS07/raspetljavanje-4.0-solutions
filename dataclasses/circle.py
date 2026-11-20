import pygame as pg
from pygame.math import Vector2
from dataclasses import dataclass

@dataclass
class Krug:
    centar: Vector2
    brzina: Vector2
    brzina_rotacije: int = 0
    poluprecnik: float = 0.0
    ugao: int = 0
    
def nacrtaj_krug(screen, krug: Krug):
    pg.draw.circle(screen, (0, 0, 255), (int(krug.centar.x), int(krug.centar.y)), krug.poluprecnik, width=2)
    
    # linija za svaku liniju za poluprecnik (0°, 90°, 180°, 270°)
    stepeni = [
        krug.centar + Vector2(krug.poluprecnik, 0).rotate(0),
        krug.centar + Vector2(krug.poluprecnik, 0).rotate(90),
        krug.centar + Vector2(krug.poluprecnik, 0).rotate(180),
        krug.centar + Vector2(krug.poluprecnik, 0).rotate(270),
    ]
    for stepen in stepeni:
        pg.draw.line(screen, (255, 0 ,0), (int(krug.centar.x), int(krug.centar.y)), (int(stepeni.x), int(stepeni.y)), width=3)
        pg.draw.circle(screen, (255, 100, 100), (int(stepeni.x), int(stepeni.y)), 6)

def kolizije_kruga(krug: Krug):
    if krug.centar.x - krug.poluprecnik < 0 or krug.centar.x + krug.poluprecnik > SCREEN_W:
        krug.brzina.x *= -1
    if krug.centar.y - krug.poluprecnik < 0 or krug.centar.y + krug.poluprecnik > SCREEN_H:
        krug.brzina.y *= -1

pg.init()
# const
SCREEN_W = 800
SCREEN_H = 600
FPS = 60
screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
clock = pg.time.Clock()

# Krug
# centar = Vector2(150, 200)
# brzina = Vector2(3, -2)
# poluprecnik = 40
# ugao = 0
# brzina_rotacije = -5
# pocetna linija
# linija = Vector2(poluprecnik, 0)
# # rotacija
# linija_rotirana = linija.rotate(ugao)
# # centar dodajemo
# kraj = centar = linija_rotirana
krugovi = [
    Krug(Vector2(150, 200), Vector2(3, -2), 4, 35, 38),
    Krug(Vector2(170, 260), Vector2(-3, 2), 5, 45, 23),
    Krug(Vector2(150, 390), Vector2(6, 4), 6, 55, 76),
    Krug(Vector2(60, 120), Vector2(10, -12), 7, 15, 45)
]

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # centar += brzina
    # ugao += brzina_rotacije
    # levo desno
    # if centar.x - poluprecnik < 0 or centar.x + poluprecnik > SCREEN_W:
    #     brzina.x *= -1
    # if centar.y - poluprecnik < 0 or centar.y + poluprecnik > SCREEN_H:
    #     brzina.y *= -1
    screen.fill((0, 0, 0))
    for krug in krugovi:
        krug.centar += krug.brzina
        krug.ugao += krug.brzina_rotacije
        nacrtaj_krug(screen, krug)
        kolizije_kruga(krug)
    pg.key.get_pressed()
    # Crtanje
    # pg.draw.circle(screen, (0, 0, 255), (int(centar.x), int(centar.y)), poluprecnik, width=2)
    # kraj = centar + Vector2(poluprecnik, 0).rotate(ugao)
    # pg.draw.line(screen, (255, 0 ,0), (int(centar.x), int(centar.y)), (int(kraj.x), int(kraj.y)), width=3)
    # pg.draw.circle(screen, (255, 100, 100), (int(kraj.x), int(kraj.y)), 6)
    pg.display.flip()
    clock.tick(FPS)
pg.quit()