# uloha Naprogramuj funkciu, ktorá vráti ciferný súčet prirodzeného čísla

def ciferny_sucet(cislo):
    sucet = 0
    while cislo > 0:
        sucet += cislo % 10   # pripočíta poslednú cifru
        cislo //= 10          # odstráni poslednú cifru
    return sucet

n = int(input("Zadaj prirodzene cislo: "))
print("Ciferny sucet cisla", n, "je", ciferny_sucet(n))
