import pygame

pygame.init()
WIDTH = 900 # Visina 
HEIGHT = 600 # Sirina
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Boje
BLACK_COLOR = (0, 0, 0) # crna boja (torka)
WHITE_COLOR = (255, 255, 255) # bela boja (torka)
GREEN_COLOR = (0, 255, 0) # zelena boja (torka)
RED_COLOR = (255, 0, 0) # crvena boja (torka)
BLUE_COLOR = (0, 0, 255) # plava boja (torka)
DARK_GRAY_COLOR = (49, 49, 49) # tamno siva boja (torka)
GRAY_COLOR = (165, 164, 164) # siva boja (torka)
LIGHT_GRAY_COLOR = (206, 206, 206) # svetlo siva boja (torka)

def nacrtaj_kucu(x, y, sirina, visina, boja_zidova, boja_krova):
    # Zidovi kuce
    pygame.draw.rect(screen, boja_zidova, (x, y, sirina, visina))
    # Krov - trougao
    points = [(x - 20, y), (x + sirina // 2, y - 40), (x + sirina + 20, y)]
    pygame.draw.polygon(screen, boja_krova, points)
    # Vrata
    pygame.draw.rect(screen, (101, 67, 33),
                    (x + sirina // 2 - 10, y + visina / 2.1, 30, 40))
    # Prozori
    pygame.draw.rect(screen, (135, 206, 250),
                    (x + 10, y + 20, 30, 30))
    pygame.draw.rect(screen, (135, 206, 250),
                    (x + sirina - 40, y + 20, 30, 30))
    # Tvoj kod - doraditi kucu   
    # Veliki prozor
    # Telo prozora
    pygame.draw.rect(screen, WHITE_COLOR, (x + sirina // 6, y + 100, sirina / 1.5, visina // 5))
    # Roletna
    pygame.draw.rect(screen, DARK_GRAY_COLOR, (x + sirina // 6, y + 100, sirina / 1.5, visina // 10 - 9))
    # Okvir
    pygame.draw.rect(screen, BLACK_COLOR, (x + sirina // 6, y + 100, sirina / 1.5, visina // 5), 5)
    
def nacrtaj_drvo(x, y, visina_stabla, boja_krosnje):
    # Stablo
    pygame.draw.rect(screen, (101, 67, 33),
                    (x - 10, y, 20, visina_stabla))
    # Krosnja - tri kruga
    pygame.draw.circle(screen, GREEN_COLOR, (x - 50, y), 50) # jedna krosnja levo u odnosu na stablo
    pygame.draw.circle(screen, GREEN_COLOR, (x, y - 50), 50) # jedna krosnja iznad u odnosu na stablo
    pygame.draw.circle(screen, GREEN_COLOR, (x + 50, y), 50) # jedna krosnja desno u odnosu na stablo

def nacrtaj_put(y_pozicija, sirina_puta):
    # Asfalt
    pygame.draw.rect(screen, (50, 50, 50),
                    (0, y_pozicija, 900, sirina_puta))
    # Bele linije
    razmak = 50
    duzina_crte = 30
    razmak_izmedju = 20
    for i in range(20):
        start_x = razmak + i * (duzina_crte + razmak_izmedju)
        end_x = start_x + duzina_crte
        # Iscrtavanje isprekidane linije 
        pygame.draw.line(screen, WHITE_COLOR, (start_x, y_pozicija + 50), (end_x, y_pozicija + 50), 6)

def nacrtaj_automobil(x, y, boja):
    # Karoserija
    pygame.draw.rect(screen, boja, (x, y, 80, 30))
    # Kabina
    pygame.draw.rect(screen, boja, (x + 20, y - 20, 40, 20))
    # Tockovi
    pygame.draw.circle(screen, BLACK_COLOR, (x + 17, y + 30), 12)
    pygame.draw.circle(screen, BLACK_COLOR, (x + 60, y + 30), 12)
    # Felne na tockovima
    pygame.draw.circle(screen, LIGHT_GRAY_COLOR, (x + 17, y + 30), 5)
    pygame.draw.circle(screen, LIGHT_GRAY_COLOR, (x + 60, y + 30), 5)
    # Prozori kod kabine
    pygame.draw.rect(screen, LIGHT_GRAY_COLOR, (x + 25, y - 15, 30, 15))

# Promenljiva za kretanje oblaka (X osa)
oblak_x = 0

def nacrtaj_oblak(x, y):
    # Prvi deo oblaka
    pygame.draw.circle(screen, WHITE_COLOR, (x, y), 50)
    # Drugi deo oblaka
    pygame.draw.circle(screen, WHITE_COLOR, (x + 50, y), 50)
    # Treci deo oblaka
    pygame.draw.circle(screen, WHITE_COLOR, (x, y - 50), 50)
    # Cetvrti deo oblaka
    pygame.draw.circle(screen, WHITE_COLOR, (x + 100, y), 50)

# Trenutna pozicija vozila na x osi (Funkcionalnost kretanja vozila levo-desno)
trenutna_pozicija_vozila_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Ukoliko je tip eventa pritisnut kao dugme na tastaturi
        elif event.type == pygame.KEYDOWN:
            # Ukoliko je pritisnut A taster na tastaturi pomeri vozilo za 10 unazad
            if event.key == pygame.K_a:
                trenutna_pozicija_vozila_x -= 20
            # Ukoliko je pritisnut D taster na tastaturi pomeri vozilo za 10 unapred
            if event.key == pygame.K_d:
                trenutna_pozicija_vozila_x += 20

    if trenutna_pozicija_vozila_x > WIDTH:
        trenutna_pozicija_vozila_x = -80 # Sirina automobila
    if trenutna_pozicija_vozila_x < -80:
        trenutna_pozicija_vozila_x = WIDTH

    # pozicija X za oblak se u svakoj iteraciji petlje povecava za 5
    oblak_x += 2
    if oblak_x > WIDTH + 100:
        oblak_x = -150

    # Plava boja neba
    screen.fill((0, 200, 255))
    
    # Dodatak srpske zastave
    # Prva pruga -> crvena
    pygame.draw.rect(screen, RED_COLOR, (800, 350, 70, 20))
    # Druga pruga -> plava
    pygame.draw.rect(screen, BLUE_COLOR, (800, 370, 70, 20))
    # Treca pruga -> bela
    pygame.draw.rect(screen, WHITE_COLOR, (800, 390, 70, 20))
    # Stub za zastavu
    pygame.draw.line(screen, LIGHT_GRAY_COLOR, (803, 410), (803, 500), 8)
    
    # Poziv funkcija
    nacrtaj_kucu(200, 250, 200, 450, (0, 255, 255), (255, 0 ,0))
    nacrtaj_drvo(600, 400, 250, (0, 255, 0))
    nacrtaj_put(500, 600)
    nacrtaj_oblak(oblak_x, 100)
    nacrtaj_automobil(trenutna_pozicija_vozila_x, 500, (255, 255, 9))

    # Text za prikaz broja slicica u sekundi (FPS)
    text = pygame.font.SysFont("Calibri", 32, bold=False, italic=False)
    text_surface = text.render(f"Fps: {round(clock.get_fps(), 0)}", True, (0, 255, 0))

    screen.blit(text_surface, (50, 50))
    pygame.display.flip()
    clock.tick(60) # 60FPS
pygame.quit()