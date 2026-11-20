try:
    cena_struje = 50; # 50$
    dnevno_BTC = 0.0001; # 0.0001BTC dnevno zaradjujemo
    vrednost_BTC = int(input())
    broj_dana_rudarenja = int(input())
    ukupno_struja = cena_struje * broj_dana_rudarenja
    ukupno_zarada = dnevno_BTC * vrednost_BTC * broj_dana_rudarenja
    ukupno = ukupno_zarada - ukupno_struja
    # Ukoliko je ukupnan profit veci od 0
    if ukupno > 0:
        print(f"Ukupan profit: {round(ukupno ,2)}$")
    # Ako nema profita:
    else:
        print(f"Gubitak je: {round(ukupno ,2)}$")
except ValueError:
    print("Greska u vrednosti!")