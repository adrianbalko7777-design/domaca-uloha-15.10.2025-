# funkcia na zistenie poctu cifier
def pocet_cifier(x):
    pocet = 0
    if x == 0:
        return 1
    while x != 0:
        pocet += 1
        x = x // 10
    return pocet

# funkcia, ktora vrati strednu cifru alebo priemer dvoch strednych
def stredna_cifra(cislo):
    n = pocet_cifier(cislo)    # zistime pocet cifier
    stred = n // 2             # index stredu (pre parny aj neparny pripad)
    a = cislo

    # ak je pocet cifier neparny
    if n % 2 == 1:
        for i in range(n - stred):
            cifra = a % 10
            a = a // 10
        return cifra
    else:
        # ak je pocet cifier parny, berieme dve stredne cifry
        for i in range(n - stred):
            cifra1 = a % 10
            a = a // 10
        cifra2 = a % 10
        priemer = (cifra1 + cifra2) / 2
        return priemer

# hlavny program
x = int(input("Zadaj číslo: "))
vysledok = stredna_cifra(x)
print("Stredná cifra alebo priemer dvoch stredných je:", vysledok)
