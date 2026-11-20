# biblioteka time kao dodatak
from time import sleep
try:
    odbrojavanje = int(input())
    for broj in range(odbrojavanje, 0, -1):
        if broj > 0:
            print(broj)
            sleep(1)
    print("LANSIRANJE - SpaceX")
except ValueError:
    print("Greska u vrednosti!")
