import pygame as pg
from pygame.math import Vector2
from dataclasses import dataclass
from random import randint

# Konstante
FPS = 60
SCREEN_W = 800
SCREEN_H = 600
BG_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)

@dataclass
class Krug:
    centar: Vector2
    brzina: Vector2
    poluprecnik: int = 0
@dataclass
class Palica:
    velicina: Vector2
    pozicija: Vector2
    brzina: int = 0

"""
Ove klase sadrze dekoraciju @dataclass pa s tim nemaju istu funkciju kao i
opste klase. @dataclass je dekoracija koja ukazuje da klasa koja sledi ima 
nalik na strukturu podataka zapravo, poznato u drugim programskim jezicima 
kao i Struct. Polja joj se definisu kao kljuc: vrednost.
"""

# Funkcije
#----------------------------------------------------------------------------------
def update(krug: Krug, palica: Palica) -> None:
    global broj_poena, game_over
    krug.centar += krug.brzina
    # Kolizije sa zidom (levi-desni)
    if krug.centar.x - krug.poluprecnik < 0 or krug.centar.x + krug.poluprecnik > SCREEN_W:
        krug.brzina.x *= -1 # krug.brzina.x = -krug.brzina.x
        collision_sound.play()
    # Kolizije sa zidom (gornji)
    if krug.centar.y - krug.poluprecnik < 0:
        krug.brzina.y *= -1 # krug.brzina.y = -krug.brzina.y
        collision_sound.play()
    # kolizije kruga sa palicom
    if (krug.centar.y + krug.poluprecnik >= palica.pozicija.y  and
        palica.pozicija.x <= krug.centar.x <= palica.pozicija.x + palica.velicina.x):
        krug.brzina.y *= -1 # krug.brzina.y = -krug.brzina.y
        krug.brzina *= ubrzanje
        broj_poena += 1
        collision_sound.play()
    # Ukoliko palica udari u donji deo ekrana
    if krug.centar.y + krug.poluprecnik > SCREEN_H:
        collision_sound.stop()
        game_over = True
        gameover_sound.play()
    # Kolizija palice sa levim-desnim delom ekrana
    if palica.pozicija.x < 0:
        palica.pozicija.x = 0
    if palica.pozicija.x + palica.velicina.x > SCREEN_W:
        palica.pozicija.x = SCREEN_W - palica.velicina.x
    # Logika pomeranja palice levo-desno po ekranu uz pomoc strelica (K_KEFT, K_RIGHT)
    tasteri = pg.key.get_pressed()
    if tasteri[pg.K_LEFT]:
        palica.pozicija.x -= palica.brzina 
    if tasteri[pg.K_RIGHT]:
        palica.pozicija.x += palica.brzina 
    # Ogranicavanje maksimalne brzine
    max_brzina = 12
    if krug.brzina.length() > max_brzina:
        krug.brzina.scale_to_length(max_brzina)    
"""
Ova funkcija update(krug, palica) nam odredjuje koliziju odnosno sta se desava pri sudaru
kruga sa palicom ili nekim drugim delom ekrana. Obicno se tu koristi logika levog-desno i 
gornjeg-donjeg dela ekrana. Ukoliko se desi kolizija na x osi, brzina x ose odredjene 
instance se mnozi sa -1 i to okrece znak brzine i time brzina ide u suprotnom smeru sto 
daje efekat reflekcije. Pored toga, kao dodatak ima i collision_sound koji se desi 
uvek prilikom kolizije nekog objekta sa krajem ekrana ili palice. Ova ista logika se 
primenjuje i za y osu odnosno gornji-donji deo ekrana. Pored kolizije, vrsi se azuriranje 
pozicije boxa, jer brzina utice na poziciju samog objekta. Uvek kada se ova funkcija pozove 
u while petlji, pozicija se promeni za datu brzinu objekta.
"""

def draw(screen, krug: Krug, palica: Palica) -> None:
    pg.draw.circle(screen, boja_kruga, (int(krug.centar.x), int(krug.centar.y)), krug.poluprecnik)
    pg.draw.rect(screen, boja_palice, (int(palica.pozicija.x), int(palica.pozicija.y), 
                                       int(palica.velicina.x), int(palica.velicina.y)))
"""
Ova funkcija draw(screen, krug) nam odredjuje temena uz pomoc promenljive points koja poziva funkciju 
rect_points koja odredjuje 4 temena i vraca nam zarotirane tacke odnosno svako teme se uz pomoc petlje
rotira za dat ugao. Uz pomoc promenljive points, crtamo mnogougao koriscenjem polygon() metode iz pg 
modula, gde uvek kada se crta mnogougao ima drugu boju (random). Na kraju, ukoliko isDebug bool 
promenljiva ima True logicku vrednost, onda iscrtavamo krug gde se koristi box_center() funkcija koja 
odredjuje centar za svaku nasu instancu kao i bounding-box odnosno granice tog naseg cetvorougla
"""

def reset(palica: Palica) -> None:
    global broj_poena
    broj_poena = 0
    palica.pozicija.x = SCREEN_W / 2.5
    krug.centar = Vector2(100, 120)
    krug.brzina = Vector2(2, 1.5)
"""
Ova funkcija reset(palica) vrsi resetovanje svih vrednosti promenljivih koje uticu na samu igru.
broj poena se resetuje na 0, kao i pozicija palice i loptice (kruga).
"""

def gameOver_screen() -> None:
    global broj_poena, rekodni_broj_poena
    if broj_poena > rekodni_broj_poena:
        rekodni_broj_poena = broj_poena
    # pozadina
    screen.fill(RED_COLOR)
    # Font
    font = pg.font.SysFont("Segoe UI", 27, bold=True, italic=False)
    # Text za font
    text_enter = font.render("Pritisni taster ENTER da igras ponovo :)", True, WHITE_COLOR)
    # Text za high-score
    text_rekord = font.render(f"Legendarni score: {rekodni_broj_poena}", True, BLUE_COLOR)
    if broj_poena < 10:
        text = font.render(f"IZGUBIO SI, BROJ POENA je {broj_poena} | PROBAJ PONOVO", True, WHITE_COLOR)
    elif broj_poena > 10 and broj_poena < 25:
        text = font.render(f"IZGUBIO SI, BROJ POENA je {broj_poena} | ODLICAN NAPREDAK", True, WHITE_COLOR)
    else:
        text = font.render(f"IZGUBIO SI, BROJ POENA je {broj_poena} | FANTASTICAN SCORE", True, WHITE_COLOR)
    screen.blit(text, (70, 100))
    screen.blit(text_enter, (133, 310))
    screen.blit(text_rekord, (240, 400))
"""
Ova funkcija gameOver_screen() vrsi iscrtavanje ekrana kao kraj igre ukoliko korisnik ne uspe da 
odbije lopticu palicom. Postoji tekst za informacije o broju poena, rekordnom broju, kao i uslovi
koji na osnovu broja poena iscrtavaju poseban tekst.
"""
#----------------------------------------------------------------------------------

# Inicijalizacija pygame-a kao i pygame mixera za sound-effecte
pg.init()
pg.mixer.init()
collision_sound = pg.mixer.Sound("sounds/collision.mp3")
gameover_sound = pg.mixer.Sound("sounds/gameoverSFX.mp3")
# postavljanje velicine ekrana i vreme za FPS
screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
clock = pg.time.Clock()

boja_kruga = WHITE_COLOR
boja_palice = WHITE_COLOR
# promenljiva koja cuva broj poena koje korisnik postigne u toku igre
broj_poena = 0
# promenljiva koja cuva vrednost ubrzanja
ubrzanje = 1.1
# blabla
rekodni_broj_poena = 0
# promenljiva koja cuva stanje True/False u zavisnosti od toga da li je korisnik izgubio ili ne
game_over = False
# Instanca klase Krug (objekat krug)
krug = Krug(Vector2(100, 120), Vector2(2, 1.5), 10)
# Instanca klase Palica (objekat palica)
palica = Palica(Vector2(140, 25), Vector2(SCREEN_W / 2.5, SCREEN_H - 25), 7)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                boja_kruga = (randint(0, 255), randint(0, 255), randint(0, 255))
                boja_palice = (randint(0, 255), randint(0, 255), randint(0, 255))
            if event.key == pg.K_RETURN and game_over:
                reset(palica)
                gameover_sound.stop()
                game_over = False

    screen.fill(BG_COLOR)
    if not game_over:
        update(krug, palica)
        draw(screen, krug, palica)
    else:
        gameOver_screen()
    # U naslovu prozora dodatak broj poena i FPS counter
    pg.display.set_caption(f"Broj poena: {broj_poena}  |  FPS: {round(clock.get_fps(), 0)}  |  Pritisni taster SPACE za promenu boje palice i loptice")
    pg.display.flip()
    clock.tick(FPS)
pg.quit()