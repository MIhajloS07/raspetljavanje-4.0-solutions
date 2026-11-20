try:
    # Unos broja uzastopnih udaraca
    broj_uzastopnih_udaraca = int(input())
    # Basic udarac = 50 damage deal
    osnovna_steta = 50
    comboX = 1 # svaki udarac * 0.5 multiplayer
    # promenljiva koja sabira svaki udarac koji se desi (sa uracunati combo bonus)
    ukupna_steta = 0

    for i in range(broj_uzastopnih_udaraca):
        udarac = osnovna_steta * comboX
        ukupna_steta += udarac
        comboX += 0.5
        # na primer 3 uzastopna udarca:
        # udarac prvi = 50 * 1
        # udarac drugi = 50 * 1.5
        # udarac treci = 50 * 2
        # ukupno udarca = udarac prvi + udarac drugi + udarac treci
    print(f"Ukupna steta je: {ukupna_steta} dmg")
except ValueError:
    print("Greska u vrednosti!")