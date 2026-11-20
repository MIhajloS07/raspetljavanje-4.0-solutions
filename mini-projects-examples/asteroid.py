import pygame as pg
from random import randint, uniform

pg.init()
# Consts
WIDTH = 800
HEIGHT = 600
FPS = 60
BG_COLOR = (18, 18, 18)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0 ,0)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# Funkcije
# ----------------------------------
def update() -> None:
    global asteroid_x, asteroid_y, asteroid_v_x, asteroid_v_y, player_x, player_y, player_R, bullet_x, bullet_y, bullet_v_x, bullet_v_y, player_color
    asteroid_x += asteroid_v_x
    asteroid_y += asteroid_v_y
    bullet_x += bullet_v_x
    bullet_y += bullet_v_y
    # Collision with screen max width or height
    if asteroid_x - asteroid_R < 0 or asteroid_x + asteroid_R > WIDTH:
        asteroid_v_x *= -1 # asteroid_v_x = -asteroid_v_x
    if asteroid_y - asteroid_R < 0 or asteroid_y + asteroid_R > HEIGHT:
        asteroid_v_y *= -1 # asteroid_v_y = -asteroid_v_y
    # Player (space ship) movement
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_x -= 1
    if keys[pg.K_RIGHT]:
        player_x += 1
    if keys[pg.K_UP]:
        player_y -= 1
    if keys[pg.K_DOWN]:
        player_y += 1
    # Player collision with screen max width or height
    player_x = max(player_R, min(WIDTH - player_R, player_x))
    player_y = max(player_R, min(HEIGHT - player_R, player_y))

    # Collision bullet with asteroid
    distanceBA = ((bullet_x - asteroid_x) ** 2 + (bullet_y - asteroid_y) ** 2)
    # Collision player with asteroid
    distancePA = ((player_x - asteroid_x) ** 2 + (player_y - asteroid_y) ** 2)
    if distanceBA < (bullet_R + asteroid_R) ** 2:
        asteroid_x = 1000
        asteroid_y = 1000
        asteroid_v_x = 0 
        asteroid_v_y = 0 
        bullet_x = -1000
        bullet_y = -1000
        bullet_v_x = 0 
        bullet_v_y = 0 
    if distancePA < (player_R + asteroid_R) ** 2:
        print("Sudar detektovan!")
        player_x = -1000
        player_y = -1000
    if distancePA <= 3000: player_color = RED_COLOR
    else: player_color = WHITE_COLOR
    print(distancePA)

def draw() -> None:
    # filling screen with background color (dark gray)
    screen.fill(BG_COLOR)
    # Drawing circle for asteroid
    pg.draw.circle(screen, WHITE_COLOR, (int(asteroid_x), int(asteroid_y)), asteroid_R, width=2)
    # Drawing circle for space ship (player)
    pg.draw.circle(screen, player_color, (int(player_x), int(player_y)), player_R)
    # Drawing circle for bullet 
    pg.draw.circle(screen, RED_COLOR, (int(bullet_x), int(bullet_y)), bullet_R)
    # Drawing crosshair
    pg.draw.line(screen, RED_COLOR, (int(player_x), int(player_y)), (int(player_x + player_R * 1.1), int(player_y)), width=5)
# ----------------------------------

# Asteroid
# for integers
# asteroid_v_x = randint(-5, 5)
# asteroid_v_y = randint(-5, 5) 
# for decimal numbers from -5 to 5
asteroid_R = randint(7, 16)
asteroid_x = randint(0 + asteroid_R, WIDTH - asteroid_R)
asteroid_y = randint(0 + asteroid_R, HEIGHT - asteroid_R)

# bullet
bullet_x = 1000
bullet_y = 1000
bullet_R = 5
bullet_max_v = 10
bullet_v_x = 0
bullet_v_y = 0

while True:
    asteroid_max_v = randint(3, 7) 
    asteroid_min_v = 2
    asteroid_v_x = uniform(-1, 1) * asteroid_max_v
    asteroid_v_y = uniform(-1, 1) * asteroid_max_v  
    if abs(asteroid_v_x) + abs(asteroid_v_y) > asteroid_min_v: break

# Space ship
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_R = 10

# Player color
player_color = WHITE_COLOR

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                bullet_x = player_x
                bullet_y = player_y
                bullet_v_x = bullet_max_v
                bullet_v_y = 0      
    update()
    draw()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()