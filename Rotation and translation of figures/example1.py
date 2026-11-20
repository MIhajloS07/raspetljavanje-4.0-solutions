import pygame as pg
from pygame.math import Vector2
from random import randint, uniform
from dataclasses import dataclass, field

# Konstante
FPS = 60
SCREEN_W = 800
SCREEN_H = 600
BG_COLOR = (0, 0, 0)

@dataclass
class Box:
    pozicija: Vector2 = field(default_factory=lambda: Vector2(randint(0, SCREEN_W - 50), randint(0, SCREEN_H - 50)))
    brzina: Vector2  = field(default_factory=lambda: Vector2(uniform(0.5, 4.5), uniform(0.5, 4.5)))
    velicina: Vector2 = field(default_factory=lambda: Vector2(randint(20, 120), randint(20, 120))) 
    rotacija: int = field(default_factory=lambda: randint(0, 270)) # od 0 do 270 stepeni pocetna rotacija
    boja: tuple = field(default_factory=lambda: (randint(0, 255), randint(0, 255), randint(0, 255))) # RGB 

"""
Ova klasa predstavlja sadrzi dekoraciju @dataclass pa s tim nema istu funkciju kao i
opsta klasa. @dataclass je dekoracija koja ukazuje da klasa koja sledi ima nalik na 
strukturu podataka zapravo, poznato u drugim programskim jezicima kao i Struct. Polja
joj se definisu kao kljuc: vrednost. Kako bi koristili random, moramo koristiti field i
default_factory=lambda kako bi se to random primenilo na svaku instancu te klase Box, jer 
u suprotnom bi se odnosila samo jedna random vrednost za sve instance sto nije prema uslovima
zadatka. Drugi nacin za ovo je da se koristi posebna metoda koju definise python __post_init__(self).
"""

# Funkcije
#----------------------------------------------------------------------------------
def box_center(box: Box) -> Vector2:
    return box.pozicija + box.velicina / 2
"""
Ova funkcija box_center(box) nam sluzi za odredjivanje sredisnje tacke na nasem
objektu tipa Box. Kao povratnu vrednost imamo Vector2 gde se vraca zbir pozicije
naseg konkretnog objekta i velicine naseg konkretnog objekta kada se podeli sa 2.
Bitno! -> deljenje kao racunska operacija ima prednost u odnosu na sabiranje.
"""

def rect_points(centar, velicina, rotacija):
    pol = velicina / 2
    osnovne_tacke = [
        Vector2(-pol.x, -pol.y), # gornji levi 
        Vector2(pol.x, -pol.y), # gornji desni 
        Vector2(pol.x, pol.y), # donji desni 
        Vector2(-pol.x, pol.y) # donji levi 
    ]
    rotirane_tacke = []
    for tacka in osnovne_tacke:
        rotirane_tacke.append(tacka.rotate(rotacija))
    nove_tacke = []
    for tacka in rotirane_tacke:
        nove_tacke.append(tacka + centar)
    return nove_tacke
"""
Ova funkcija rect_points(centar, velicina, rotacija) nam odredjuje polozaj tacaka objekta.
Prvo se odredjuje polozaj, zatim imamo listu osnovnih tacaka, gde koristimo Vector2 klasu
(x, y) gde se odredjuju cetiri temena za nas objekat jer zelimo da to bude neki cetvorougao.
Nakon toga, kreiramo listu rotirane_tacke gde se uz pomoc for petlje iterira kroz listu 
osnovne_tacke i za svaku tacku se dodaje u novoj listi rotirate_tacke rotirana tacka za 
dati broj stepeni (rotacija). Posle toga imamo jos jednu kreiranu listu nove_tacke gde ce
uz pomoc for petlje da se iterira kroz listu rotirane_tacke i u novoj listi nove_tacke dodati
tacka kao tacka + centar. Na kraju vracamo tu listu tacaka.
"""

def update(box: Box, bounds: tuple[int, int]) -> None:
    # menjanje pozicije tako sto se na poziciji dodaje brzina objekta
    box.pozicija += box.brzina
    Width, Height = bounds
    # Kolizije - sudari
    # Sudar sa levim-desnim zidom
    if box.pozicija.x < 0 or box.pozicija.x + box.velicina.x > Width: 
        box.brzina.x *= -1 # brzina.x = -brzina.x
        collision_sound.play() # pokrecemo sound-effect kada se desi udar objekta sa zidom
    # Sudar sa gornjim-donjim zidom
    if box.pozicija.y < 0 or box.pozicija.y + box.velicina.y > Height:
        box.brzina.y *= -1 # brzina.y = -brzina.y
        collision_sound.play() # pokrecemo sound-effect kada se desi udar objekta sa zidom
"""
Ova funkcija update(box, bounds[int, int]) nam odredjuje koliziju odnosno sta se desava pri sudaru
odredjenog objekta sa nekim delom ekrana. Obicno se tu koristi logika levog-desno i gornjeg-donjeg
dela ekrana. Ukoliko se desi kolizija na x osi, brzina x ose odredjene instance se mnozi sa -1 i to
okrece znak brzine i time brzina ide u kontra smeru sto daje efekat reflekcije. Pored toga, kao dodatak
ima i collision_sound koji se desi uvek prilikom kolizije nekog objekta sa krajem ekrana. Ova ista logika
se primenjuje i za y osu odnosno gornji-donji deo ekrana. Pored kolizije, vrsi se azuriranje pozicije boxa,
jer brzina utice na poziciju samog objekta. Uvek kada se ova funkcija pozove u while petlji, pozicija se 
promeni za datu brzinu objekta.
"""

def draw(screen, box: Box):
    points = rect_points(box_center(box), box.velicina, box.rotacija)
    pg.draw.polygon(screen, box.boja, points, width=2)
"""
Ova funkcija draw(screen, box) nam odredjuje temena uz pomoc promenljive points koja poziva funkciju 
rect_points koja odredjuje 4 temena i vraca nam zarotirane tacke odnosno svako teme se uz pomoc petlje
rotira za dat ugao. Uz pomoc promenljive points, crtamo mnogougao koriscenjem polygon() metode iz pg 
modula, gde uvek kada se crta mnogougao ima drugu boju (random). 
"""
#----------------------------------------------------------------------------------

# Inicijalizacija pygame-a kao i pygame mixera za sound-effecte
pg.init()
pg.mixer.init()
# postavljanje velicine ekrana i vreme za FPS
screen = pg.display.set_mode((SCREEN_W, SCREEN_H))
clock = pg.time.Clock()

# Box objekti -> instance (lista objekta)
# 5 instanci, sve unutar njih se random postavlja
boxes = [Box() for _ in range(5)] 
"""
prakticnije u listi koristiti "ugradjenu for petlju" nego Box(), Box(), Box(), Box(), Box()
"""
collision_sound = pg.mixer.Sound("sounds/collision.mp3")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Iteracija kroz listu boxes i poziva se funkcija update i draw za svaki objekat
    for box in boxes:
        update(box, (SCREEN_W, SCREEN_H))
        draw(screen, box)
        box.rotacija += 1

    # U naslovu prozora dodatak FPS counter
    pg.display.set_caption(f"FPS: {round(clock.get_fps(), 0)}")
    pg.display.flip()
    clock.tick(FPS)
pg.quit()