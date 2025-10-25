# uloha pocet parnych cifier v zadanom cisle

x = int(input('Zadaj cislo: '))
vysledok = pocet_parnych(x)


def pocet_parnych(cislo):
    pocet = 0               # inicializacia pocitadla
    while cislo != 0:       # opakujeme, kym cislo nie je 0
        cifra = cislo % 10  # zistime poslednu cifru
        if cifra % 2 == 0:  # skontrolujeme, ci je parna
            pocet += 1
        cislo = cislo // 10 # odstranime poslednu cifru
    return pocet            # vratime pocet parnych cifier

print('Pocet parnych cifier v cisle', x, 'je', vysledok)