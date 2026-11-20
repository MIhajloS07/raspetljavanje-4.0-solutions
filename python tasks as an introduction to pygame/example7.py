# lista lavirint koja sadrzi redove i kolone (matrica 5x5) -> kvadratna
lavirint = []

for i in range(5):
    while True:
        red = input().strip()
        if len(red) != 5:
            print("Red mora imati tacno 5 karaktera!")
            continue
        if red.count('.') < 2:
            print("Red mora imati bar 2 puta ('.')!")
            continue
        lavirint.append(list(red))
        break

print("Lavirint:")
broj_puteva = 0
for i in range(5):
    for j in range(5):
        if lavirint[i][j] == '.':
            broj_puteva += 1
        print(lavirint[i][j], end=" ")
    print()
print("Broj puteva:", broj_puteva)
