# funkcia na zistenie poctu cifier
def pocet_cifier(x):
    pocet = 0
    if x == 0:
        return 1
    while x != 0:
        pocet += 1
        x = x // 10
    return pocet

# funkcia, ktora zisti, ci je cislo symetricke
def je_symetricke(cislo):
    n = pocet_cifier(cislo)
    povodne = cislo      # ulozime povodne cislo
    otocene = 0          # sem ulozime cislo odzadu

    # otocime cislo
    while cislo != 0:
        cifra = cislo % 10
        otocene = otocene * 10 + cifra
        cislo = cislo // 10

    # porovname
    if povodne == otocene:
        return True
    else:
        return False

# hlavny program
x = int(input("Zadaj číslo: "))

if je_symetricke(x):
    print("Číslo je symetrické.")
else:
    print("Číslo NIE je symetrické.")
