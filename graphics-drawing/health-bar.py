import pygame

pygame.init()
screen = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()
screen.fill((20, 20, 40))  # tamna pozadina

# Ovde napisi svoj kod
ukupno_zdravlje = 100
steta = int(input())
preostalo_zdravlje = ukupno_zdravlje - steta # izracunaj preostalo zdravlje
procenat = max(0, preostalo_zdravlje) / ukupno_zdravlje
sirina_ispune = int(300 * procenat)
# Nacrtaj okvir i ispunu prema odnosu preostalo_zdravlje / ukupno_zdravlje
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

if procenat > 0.6: 
    pygame.draw.rect(screen, GREEN, (100, 200, 300, 50), 3)
    pygame.draw.rect(screen, GREEN, (100, 200, sirina_ispune, 50))
elif procenat > 0.2:
    pygame.draw.rect(screen, ORANGE, (100, 200, 300, 50), 3)
    pygame.draw.rect(screen, ORANGE, (100, 200, sirina_ispune, 50)) 
else:
    pygame.draw.rect(screen, RED, (100, 200, 300, 50), 3)
    pygame.draw.rect(screen, RED, (100, 200, sirina_ispune, 50)) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()  # Ažuriraj ekran
pygame.quit()