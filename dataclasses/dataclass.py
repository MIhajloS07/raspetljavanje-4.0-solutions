import pygame as pg
from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Box:
    poz: Vector2      # pozicija boxa
    brzina: Vector2   # brzina boxa
    velicina: Vector2 # velicina boxa
    ugao: float = 0.0   # ugao rotacije

def box_center(box: Box) -> Vector2:
    return box.poz + box.velicina / 2

def rect_points(centar, velicina, ugao_stepeni):
    pol = velicina / 2
    osnovne_tacke = [Vector2(-pol.x, -pol.y),Vector2(pol.x, -pol.y), 
                     Vector2(-pol.x, pol.y),Vector2(pol.x, pol.y)]
    rotirane_tacke = []
    for tacka in osnovne_tacke:
        rotirane_tacke.append(tacka.rotate(ugao_stepeni))
    nove_tacke = []
    for tacka in rotirane_tacke:
        nove_tacke.append(tacka + centar)
    return nove_tacke

def update_box(box: Box, bounds: tuple[int, int]) -> None:
    box.poz += box.brzina
    W, H = bounds
    # sudar sa levim-desnim zidom
    if box.poz.x < 0 or box.poz.x + box.velicina.x > W:
        box.brzina.x *= -1
    # sudar sa gornjim-donjim zidom
    if box.poz.y < 0 or box.poz.y + box.velicina.y > H:
        box.brzina.y *= -1
    
def draw_box(screen, box: Box) -> None:
    pts = rect_points(box_center(box), box.velicina, box.ugao)
    pg.draw.polygon(screen, (255, 0, 0), pts, width=2)

pg.init()
# Const
WIDTH = 800
HEIGHT = 600
FPS = 60
BG_COLOR = (0, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# Box instance
# Prvi nacin, svaku instancu posebno
# box1 = Box(Vector2(100, 100), Vector2(2, 1.5), Vector2(80, 50), 15)
# box2 = Box(Vector2(259, 314), Vector2(3, 2), Vector2(100, 40), 70)
# box3 = Box(Vector2(180, 400), Vector2(1.2, 0.7), Vector2(150, 30), 50)

# Drugi nacin, koriscenjem liste
boxes = [
    Box(Vector2(100, 100), Vector2(2, 1.5),   Vector2(80, 50), 15),
    Box(Vector2(259, 314), Vector2(3, 2),     Vector2(100, 40), 70),
    Box(Vector2(180, 400), Vector2(1.2, 0.7), Vector2(150, 30), 50),
    Box(Vector2(250, 120), Vector2(5, 3),     Vector2(30, 15), 90),
    Box(Vector2(20, 40),   Vector2(2, 7),     Vector2(30, 30), 45)
]

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # update_box(box1, (WIDTH, HEIGHT))
    # update_box(box2, (WIDTH, HEIGHT))
    # update_box(box3, (WIDTH, HEIGHT))

    for box in boxes:
        update_box(box, (WIDTH, HEIGHT))

    screen.fill(BG_COLOR)
    # draw_box(screen, box1)
    # draw_box(screen, box2)
    # draw_box(screen, box3)
    for box in boxes:
        draw_box(screen, box)

    pg.display.flip()
    clock.tick(FPS)
pg.quit()