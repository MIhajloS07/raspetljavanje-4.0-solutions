import pygame
from datetime import datetime

pygame.init()
HEIGHT = 700
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Boje
LIGHT_BROWN_COLOR = (141, 111, 100)
DARK_BROWN_COLOR = (66, 49, 42)
BROWN_COLOR = (141, 111, 86)
BEIDGE_COLOR = (179, 151, 127)
GREEN_CARPET_COLOR = (137, 170, 107)
BLUE_GRAY_COLOR = (226, 234, 244)
LIGHT_GRAY_COLOR = (156, 152, 144)
WHITE_COLOR = (255, 255 ,255)
BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)

# Trenutni datum
trenutni_datum = datetime.now().date()

# Definisanje fonta -> Arial, 24 velicna slova
font_arial = pygame.font.SysFont('Segoe UI', 50)
font_calibri = pygame.font.SysFont('Calibri', 22)
text_surface_name = font_arial.render("MIHAJLO", True, BLACK_COLOR, BLUE_GRAY_COLOR)
text_surface_date = font_calibri.render(str(trenutni_datum), True, WHITE_COLOR)

# Funkcije
def nacrtaj_pod():
    # Crtanje poda
    pygame.draw.rect(screen, LIGHT_BROWN_COLOR, (0, HEIGHT / 1.48 + 30, WIDTH, HEIGHT // 10))
    pygame.draw.rect(screen, BROWN_COLOR, (0, HEIGHT / 1.3 + 30, WIDTH, HEIGHT // 10))
    pygame.draw.rect(screen, BEIDGE_COLOR, (0, HEIGHT / 1.15 + 30, WIDTH, HEIGHT // 10))

    # Tepih
    pygame.draw.rect(screen, GREEN_CARPET_COLOR, (WIDTH // 3.8, HEIGHT / 1.4 + 30, WIDTH // 2, HEIGHT // 5))
    # Okvir oko tepiha
    pygame.draw.rect(screen, BLUE_GRAY_COLOR, (WIDTH // 3.8, HEIGHT / 1.4 + 30, WIDTH // 2, HEIGHT // 5), 5)
    # Crtanje detalja na tepihu
    # Prvi krug
    pygame.draw.circle(screen, BLACK_COLOR, (WIDTH // 2.85, HEIGHT / 1.15), 20)
    # Jos jedan krug unutar prvog kruga
    pygame.draw.circle(screen, LIGHT_BROWN_COLOR, (WIDTH // 2.85, HEIGHT / 1.15), 7)
    # Drugi krug
    pygame.draw.circle(screen, BLACK_COLOR, (WIDTH // 2, HEIGHT / 1.15), 10)
    # Dodavanje okvira oko drugog kruga
    pygame.draw.circle(screen, BLUE_COLOR, (WIDTH // 2, HEIGHT / 1.15), 15, 5)
    # Treci krug
    pygame.draw.circle(screen, BLACK_COLOR, (WIDTH // 1.5, HEIGHT / 1.15), 20)
    # Jos jedan krug unutar treceg kruga
    pygame.draw.circle(screen, LIGHT_BROWN_COLOR, (WIDTH // 1.5, HEIGHT / 1.15), 7)    

def nacrtaj_vrata(sirina, visina):
    # Crtanje vrata
    pygame.draw.rect(screen, DARK_BROWN_COLOR, (WIDTH // 15, HEIGHT // 2.55, sirina, visina))
    # Crtanje kvake za vrata
    pygame.draw.circle(screen, BROWN_COLOR, (WIDTH // 15 + sirina - 20, HEIGHT // 1.8), 6)

def nacrtaj_krevet(sirina, visina):
    # Crtanje gornjeg dela kreveta
    pygame.draw.rect(screen, BROWN_COLOR, (WIDTH // 4.2, HEIGHT // 1.8, sirina, visina))
    # Crtanje donjeg dela kreveta
    pygame.draw.rect(screen, BEIDGE_COLOR, (WIDTH // 4.6, HEIGHT // 1.82 + visina, sirina + 32, visina))
    # Crtanje leve stranica kreveta
    pygame.draw.rect(screen, DARK_BROWN_COLOR, (WIDTH // 4.6, HEIGHT // 1.95 + visina, sirina // 5, visina + 30))
    # Crtanje desne stranica kreveta
    pygame.draw.rect(screen, DARK_BROWN_COLOR, (WIDTH // 2.3, HEIGHT // 1.95 + visina, sirina // 5, visina + 30))

def nacrtaj_mali_sto():
    # Gornja stranica stola
    pygame.draw.line(screen, BLACK_COLOR, (245, HEIGHT // 1.5), (370, HEIGHT // 1.5), 3)
    # Leva nogara stola
    pygame.draw.rect(screen, BLACK_COLOR, (245, 465, 20, 80))
    # Desna nogara stola
    pygame.draw.rect(screen, BLACK_COLOR, (350, 465, 20, 80))

def digitalni_kalendar(x, y):
    # Digitalni kalendar na zidu
    pygame.draw.rect(screen, BLUE_COLOR, (x, y, x // 2.3, y // 4))
    # Okvir za digitalni kalendar
    pygame.draw.rect(screen, WHITE_COLOR, (x, y, x // 2.3, y // 4), 3)
    # Tekst koji ce se ispisati na x: 265 i y: 440
    screen.blit(text_surface_date, (x + 5, y + 5))

def nacrtaj_orman():
    # Crtanje ormana
    pygame.draw.rect(screen, LIGHT_GRAY_COLOR, (WIDTH // 3 + 150, HEIGHT // 2 - 146, 350, 300))
    # crtanje rucica -> dva kruga
    pygame.draw.circle(screen, BLACK_COLOR, (WIDTH // 3 + 300, HEIGHT // 2 + 40), 9)
    pygame.draw.circle(screen, BLACK_COLOR, (WIDTH // 3 + 330, HEIGHT // 2 + 40), 9)

def slika_sa_imenom():
    # slika
    pygame.draw.rect(screen, BLUE_GRAY_COLOR, (460, 30, 320, 130))
    # Okvir za sliku
    pygame.draw.rect(screen, DARK_BROWN_COLOR, (460, 30, 320, 130), 10)
    # Tekst
    screen.blit(text_surface_name, (520, 60))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Crtanje sobe:
    # Boja zida -> svetlije plava
    screen.fill((105, 151, 208))

    # Pozivanje funkcija za iscrtavanje:
    nacrtaj_pod()
    nacrtaj_vrata(100,230)
    nacrtaj_krevet(200, 60)
    nacrtaj_mali_sto()
    digitalni_kalendar(265, 200)
    nacrtaj_orman()
    slika_sa_imenom()
    pygame.display.flip()

    clock.tick(60) # 60FPS
pygame.quit()