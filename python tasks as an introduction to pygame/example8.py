import random
try:
    # Moguci tipovi soba
    tipovi_soba = ["mracna kripta", "osvetljena dvorana", "tajna komora"]
    blago = ["zlato", "mac", "stit", "nista"]
    broj_soba = int(input("Unesi broj soba: "))
    for soba in range(broj_soba):
        print(f"Soba broj: {soba + 1}")
        # iz liste tipovi_soba se bira random tip sobe
        print(f"Tip sobe: {random.choice(tipovi_soba)}")
        # iz liste blago se bira random blago
        print(f"Blago: {random.choice(blago)}") 
        # neprijatelji -> uvek se generise random broj izmedju 0 i 5 za neprijatelje u sobi
        print(f"Broj neprijatelja: {random.randint(0, 5)}")
        # # posle svake sobe printuje se novi red radi preglednosti
        print()
except ValueError:
    print("Greska u vrednosti!")