# Унос 8 карактера ('X' или '-')
pozicije = [] 
for znak in range(0, 8): # 0 - 7 0,1,2,3,4,5,6,7
    znak = input().strip()
    pozicije.append(znak)
# od 0 do 4-1
for _ in range(0, 4):
    # dodajemo "" izmedju svakog elementa u listi i to se primenjuje za svaki element u listi pozicije
    print("".join(str(znak) for znak in pozicije), end = " ")
