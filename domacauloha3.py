#Naprogramuj funkciu, ktorá vráti počet cifier daného celého čísla

x = int(input('Zadaj cele cislo: '))
vysledok = pocet_cifier(x)


def pocet_cifier(cislo):
    pocet = 0                 # inicializacia pocitadla
    if cislo == 0:            # ak je cislo nula, ma jednu cifru
        return 1
    if cislo < 0:             # ak je cislo zaporne, spravime z neho kladne
        cislo = -cislo
    while cislo != 0:         # opakujeme, kym cislo nie je 0
        pocet += 1
        cislo = cislo // 10   # odstranime poslednu cifru
    return pocet              # vratime pocet cifier


x = int(input('Zadaj cele cislo: '))
vysledok = pocet_cifier(x)
print('Pocet cifier v cisle', x, 'je', vysledok)
