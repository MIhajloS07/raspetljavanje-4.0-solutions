import pygame as pg
from random import randint, uniform
from pygame.math import Vector2
from asteroid import Asteroid
from player import Player
from bullet import Bullet
from constants import *

# Functions
# ----------------------------------------------------------------------------------
# collision between asteroid and player - spaceship
def collision_asteroid_player(asteroid, player) -> bool:
    distancesPA = ((player.p.x - asteroid.p.x) ** 2 + 
                   (player.p.y - asteroid.p.y) ** 2)
    # distancePA 100px => sqrt(10000) = 100
    if distancesPA < (player.R + asteroid.R) ** 2:
        return True
    return False

# collision between asteroid and bullet
def collision_asteroid_bullet(asteroid, bullet) -> bool:
    # Collision bullet with asteroid
    distanceBA = ((bullet.p.x - asteroid.p.x) ** 2 +
                  (bullet.p.y - asteroid.p.y) ** 2)
    if distanceBA < (bullet.R + asteroid.R) ** 2:
        return True
    return False

# bullet distance 
def collision_bullet_startend(bullet) -> bool:
    # Distance between bullet_start and bullet end
    distanceBSBE = ((bullet.p.x - bullet.start.x) ** 2 +
                    (bullet.p.y - bullet.start.y) ** 2)
    if distanceBSBE > bullet.max_distance:
        return True
    return False

# update asteroid - movement
def update_asteroid(asteroid) -> Asteroid:
    asteroid.p += asteroid.v
    if asteroid.p.x - asteroid.R < 0 or asteroid.p.x + asteroid.R > WIDTH:
        asteroid.v.x *= -1 # asteroid_v_x = -asteroid_v_x
    if asteroid.p.y - asteroid.R < 0 or asteroid.p.y + asteroid.R > HEIGHT:
        asteroid.v.y *= -1 # asteroid_v_y = -asteroid_v_y
    return asteroid

# update bullets, asteroid, player
def update() -> None:
    global asteroids, bullets, player, game_over
    for bullet in bullets:
        bullet.p += bullet.v  
    for asteroid in asteroids:
        asteroid = update_asteroid(asteroid)
    # Player (space ship) movement
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.angle -= player.max_v
    if keys[pg.K_RIGHT]:
        player.angle += player.max_v
    if keys[pg.K_UP]:
        acceleration = Vector2(PLAYER_ACCELERATION, 0).rotate(player.angle)
        player.v += acceleration
    if keys[pg.K_a]:
        player.angle -= player.max_v
    if keys[pg.K_d]:
        player.angle += player.max_v    

    # Player slow down slowly
    player.v *= PLAYER_FRICTION

    # max speed to be max_v
    if player.v.length() > player.max_v:
        player.v.scale_to_length(player.max_v)
    
    # update position
    player.p += player.v

    # Player collision with screen max width or height
    player.p.x = max(player.R, min(WIDTH - player.R, player.p.x))
    player.p.y = max(player.R, min(HEIGHT - player.R, player.p.y))

    # variable for current time 
    current_time = pg.time.get_ticks()
    # Checking collision between asteroids and player
    if current_time - player.indestructible_from > INDESTRUCTIBLE_MS:
        for asteroid in asteroids:
            if collision_asteroid_player(asteroid, player):
                player.lives -= 1
                asteroid_hit_sound.play()
                player.indestructible_from = current_time
                player.angle = 0
                player.p = Vector2(-1000, -1000)
                break

    # Checking collision between asteroids and bullet
    asteroids_for_delete = []
    bullets_for_delete = []
    new_asteroids = [] # list for save new mini splited asteroids
    for bullet_index in range(len(bullets)):
        for asteroid_index in range(len(asteroids)):
            asteroid = asteroids[asteroid_index]
            if collision_asteroid_bullet(asteroids[asteroid_index], bullets[bullet_index]):         
                asteroids_for_delete.append(asteroid_index)
                bullets_for_delete.append(bullet_index)
                # Points system
                if asteroid.R >= 10 and asteroid.R < 15:
                    player.points += 12
                elif asteroid.R >= 15 and asteroid.R < 18:
                    player.points += 20
                else:
                    player.points += 30
                
                # split asteroids
                if asteroid.R > 13:
                    parts = split_asteroid(asteroid)
                    new_asteroids.extend(parts)

    asteroid_remains = []
    for asteroid_index in range(len(asteroids)):
        if asteroid_index not in asteroids_for_delete:
            asteroid_remains.append(asteroids[asteroid_index])
    asteroids = asteroid_remains
    asteroids.extend(new_asteroids) # extend asteroids list with new_asteroids -> two mini asteroids splited

    bullets_remains = []
    for bullet_index in range(len(bullets)):
        if bullet_index not in bullets_for_delete:
            bullets_remains.append(bullets[bullet_index])
    bullets = bullets_remains
     
    # Checking collision between bullet start and bullet end
    for bullet in bullets:
        if collision_bullet_startend(bullet):
            bullet.p = Vector2(1000, 1000)
            bullet.v = Vector2(0, 0)
    if player.lives == 0 and not game_over:
        game_over = True
        player.v = Vector2(0, 0)
        return 
    player_near_asteroid = False
    for asteroid in asteroids:
        distance_sq = (player.p.x - asteroid.p.x)**2 + (player.p.y - asteroid.p.y)**2
        if distance_sq < ALERT_DISTANCE**2:
            player_near_asteroid = True
            break
    if player_near_asteroid: player.color = RED_COLOR 
    else: player.color = WHITE_COLOR

# get random size and speed for asteroid and return it
def get_random_asteroid() -> Asteroid:
    asteroid_R = randint(ASTEROID_MIN_R, ASTEROID_MAX_R)
    asteroid_p = Vector2(
        randint(0 + asteroid_R, WIDTH - asteroid_R),
        randint(0 + asteroid_R, HEIGHT - asteroid_R)
    )
    asteroid_v = Vector2(
        uniform(-1, 1) * ASTEROID_MAX_V, 
        uniform(-1, 1) * ASTEROID_MAX_V  
    )
    return Asteroid(
        p = asteroid_p,
        R = asteroid_R,
        max_v = ASTEROID_MAX_V,
        min_v = ASTEROID_MIN_V,
        v = asteroid_v
    )

# game lose screen
def game_lose() -> None:
    global game_over
    if game_over:
        screen.fill((0, 0, 0))
        font = pg.font.SysFont(None, 80)
        fontEnter = pg.font.SysFont(None, 40)
        txtOne = font.render("GAME OVER", True, RED_COLOR)
        txtTwo = font.render(f"Points earned: {player.points}", True, WHITE_COLOR)
        txtEnter = fontEnter.render(f"PRESS ENTER TO PLAY AGAIN", True, GREEN_COLOR)
        screen.blit(txtOne, (WIDTH//2 - txtOne.get_width()//2, HEIGHT//3))
        screen.blit(txtTwo, (WIDTH//2 - txtTwo.get_width()//2, HEIGHT//2))
        screen.blit(txtEnter, (WIDTH//2 - txtEnter.get_width()//2, HEIGHT//1.2))
        bulletSound.stop()
        pg.display.flip()  

# game win screen
def game_win() -> None:
    screen.fill((0, 0, 0))
    font = pg.font.SysFont(None, 80)
    fontEnter = pg.font.SysFont(None, 40)
    txtOne = font.render("GAME WIN", True, GREEN_COLOR)
    txtTwo = font.render(f"Points earned: {player.points}",True, WHITE_COLOR)
    txtEnter = fontEnter.render(f"PRESS ENTER TO PLAY AGAIN", True, RED_COLOR)
    screen.blit(txtOne, (WIDTH//2 - txtOne.get_width()//2, HEIGHT//3))
    screen.blit(txtTwo, (WIDTH//2 - txtTwo.get_width()//2, HEIGHT//2))
    screen.blit(txtEnter, (WIDTH//2 - txtEnter.get_width()//2, HEIGHT//1.2))
    bulletSound.stop()
    pg.display.flip() 

# Split one big asteroid to two small asteroids and return it
def split_asteroid(asteroid) -> Asteroid:
        new_R = asteroid.R // 2 # new R will be 2 times smaller 
        offset = 10 # move asteroid one from another
        # new speed for asteroids using list
        new_speeds = [
            asteroid.v.rotate(randint(ASTEROID_MIN_V + 5, ASTEROID_MAX_V + 5)),
            asteroid.v.rotate(randint(ASTEROID_MIN_V + 5, ASTEROID_MAX_V + 5))
        ]
        return [
            Asteroid(
                p = asteroid.p + Vector2(-offset, -offset),
                R = new_R,
                max_v = ASTEROID_MAX_V,
                min_v = ASTEROID_MIN_V,
                v = new_speeds[0]
            ),
            Asteroid(
                p = asteroid.p + Vector2(offset, offset),
                R = new_R,
                max_v = ASTEROID_MAX_V,
                min_v = ASTEROID_MIN_V,
                v = new_speeds[1]
            )
        ]

def draw_asteroid(asteroid) -> None:
    # Drawing circle for asteroid
    pg.draw.circle(screen, ASTEROID_COLOR, (int(asteroid.p.x), int(asteroid.p.y)), asteroid.R, width=ASTEROID_BORDER_WIDTH)

def draw_player(player) -> None:
    # Drawing circle for space ship (player)
    pg.draw.circle(screen, player.color, (int(player.p.x), int(player.p.y)), player.R)
    end_of_player_aim = Vector2(player.R * 1.1, 0).rotate(player.angle)
    end_of_player_aim += player.p
    pg.draw.line(screen, RED_COLOR, (int(player.p.x), int(player.p.y)), (int(end_of_player_aim.x), int(end_of_player_aim.y)), width=5)

def draw_bullet(bullet) -> None:
    # Drawing circle for bullet 
    pg.draw.circle(screen, RED_COLOR, (int(bullet.p.x), int(bullet.p.y)), bullet.R)

def draw() -> None:
    # filling screen with background color (dark gray)
    screen.fill(BG_COLOR)
    # Drawing all asteroids from list
    for asteroid in asteroids:
        draw_asteroid(asteroid)
    # Drawing circles for bullets
    for bullet in bullets:
        draw_bullet(bullet)
    # Make player indestructible for 3 seconds of start game or when he dies
    current_time = pg.time.get_ticks()
    indestructible = current_time - player.indestructible_from < INDESTRUCTIBLE_MS
    # if player is indestructible, blink (0.1s off, 0.1s on)
    if indestructible and (current_time // 100) % 2 == 1:
        return
    # Drawing space ship (player)
    draw_player(player)

def wait_for_again() -> None:
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    waiting = False

def reset_game() -> None:
    global player, bullets, asteroids, gamewin_sound_played, num_of_asteroids, game_over, gameover_sound_played, high_score
    if player.points > high_score:
        high_score = player.points
    player = Player(
        p=Vector2(WIDTH // 2, HEIGHT // 2),
        v = Vector2(0, 0),
        color=WHITE_COLOR,
        R=PLAYER_R,
        max_v=PLAYER_MAX_V,
        angle=0,
        lives=3,
        points=0,
        last_shot=0,
        indestructible_from=pg.time.get_ticks()
    ) 
    bullets = []
    asteroids = []
    num_of_asteroids = randint(ASTEROIDS_MIN, ASTEROIDS_MAX)
    for _ in range(num_of_asteroids):
        asteroids.append(get_random_asteroid())
    game_over = False
    gamewin_sound_played = False
    gameover_sound_played = False
# ----------------------------------------------------------------------------------

# pg and mixer init
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# Sounds
bulletSound = pg.mixer.Sound('sfx/lasergun.mp3')
asteroid_hit_sound = pg.mixer.Sound('sfx/asteroid_hit.mp3')
explosion_sound = pg.mixer.Sound('sfx/pixel-explosion.mp3')
gamewin_sound = pg.mixer.Sound('sfx/gamewin.mp3')
gamelose_sound = pg.mixer.Sound('sfx/gamelose.mp3')
bulletSound.set_volume(0.7)
asteroid_hit_sound.set_volume(0.6)
explosion_sound.set_volume(0.3)
gamewin_sound.set_volume(0.5)
gamelose_sound.set_volume(0.5)

# Space ship (player) instance
player = Player(
    p=Vector2(WIDTH // 2, HEIGHT // 2), v = Vector2(0, 0), color=WHITE_COLOR, R=PLAYER_R, max_v=PLAYER_MAX_V, angle=0, lives=3, points=0, last_shot=0, indestructible_from=pg.time.get_ticks()
)

# bullet list for save every bullet shot
bullets = []

num_of_asteroids = randint(ASTEROIDS_MIN, ASTEROIDS_MAX)
asteroids = []
for i in range(num_of_asteroids):
    asteroids.append(get_random_asteroid())
print(f"Game starts with {num_of_asteroids} asteroids!")

# variable for store high score
high_score = 0



# bool variables for checking and setting logic value (True/False)
gameover_sound_played = False
gamewin_sound_played = False
game_over = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:      
                current_time = pg.time.get_ticks()
                if current_time - player.last_shot >= PAUSE_MS:
                    new_bullet = Bullet(
                        p = player.p.copy(), # Creating a copy of player_p Vector2 
                        R = BULLET_R,
                        max_v = BULLET_MAX_V, 
                        v = Vector2(BULLET_MAX_V, 0).rotate(player.angle),
                        start = player.p.copy(),
                        max_distance = 230*230
                    )
                    bulletSound.play()
                    bullets.append(new_bullet)
                    player.last_shot = current_time
    if not game_over:
        update()
        draw()
    else:
        if not gameover_sound_played:
            gamelose_sound.play()
            gameover_sound_played = True      
        game_lose()
        wait_for_again()
        reset_game() 
    if len(asteroids) == 0:
        if not gamewin_sound_played:
            gamewin_sound.play()
            gamewin_sound_played = True
        game_win()
        wait_for_again()
        reset_game()     
    pg.display.flip()
    clock.tick(FPS)
    pg.display.set_caption(f"FPS: {round(clock.get_fps(), 2)}   |   lives: {player.lives}   |   points: {player.points}   |   high score: {high_score}")
pg.quit()