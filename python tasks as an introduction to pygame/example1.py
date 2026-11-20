try:
    # String lozinka
    lozinka = input("Unesi lozinku: ") # unos
    # Promenljiva n sadrzi duzinu stringa lozinka
    n = len(lozinka)
    # Uslov da li je neki karakter lozinke broj i ukoliko je duzina lozinke >= 8
    if any(char.isdigit() for char in lozinka) and n >= 8:
        print("Lozinka je jaka!")
    else:
        print("Lozinka je slaba!")
except ValueError:
    print("Greska u vrednosti!")