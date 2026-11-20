import pygame as pg
from pygame.math import Vector2
from dataclasses import dataclass
from random import randint

@dataclass
class RectData:
    x: float = 0.0
    y: float = 0.0
    height: float = 0.0
    width: float = 0.0
    speed_x: float = 10.5

def draw_rect(screen, rect: RectData):
    red_color = randint(0, 255); green_color = randint(0, 255); blue_color = randint(0, 255)
    color = (red_color, green_color, blue_color)
    pg.draw.rect(screen, color, (rect.x, rect.y, rect.width, rect.height))

def change_speed_x(speed_x, rect: RectData):
    rect.speed_x = speed_x
    return rect.speed_x

pg.init()
# Const
HEIGHT = 600
WIDTH = 800
FPS = 60

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# RectData instance
rect1 = RectData(150, 180, 120, 60)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        rect1.x += rect1.speed_x
    if keys[pg.K_LEFT]:
        rect1.x -= rect1.speed_x 

    if rect1.x > WIDTH:
        rect1.x = -rect1.width
    if rect1.x + rect1.width < 0:
        rect1.x = WIDTH

    screen.fill((0, 0, 0))
    draw_rect(screen, rect1)
    change_speed_x(45, rect1)
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
