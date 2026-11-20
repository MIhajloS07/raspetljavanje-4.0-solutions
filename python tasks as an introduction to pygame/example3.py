import random
try:
    broj_pokusaja = 0
    while True: # dok skejter ne uspe da izvede trik
        # povecavamo broj pokusaja za 1
        broj_pokusaja += 1
        if random.random() < 0.3: # 30% sanse za uspeh
            print(f"Uspeo si posle {broj_pokusaja} pokusaja")
            # izlazak iz besoknacne petlje i kraj programa
            break
except ValueError:
    print("Greska u vrednosti!")