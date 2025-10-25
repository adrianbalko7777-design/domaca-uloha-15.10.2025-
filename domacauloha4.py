#Naprogramuj funkciu, ktorá dané číslo vypíše odzadu

x = int(input('Zadaj cislo: '))
print('Cislo odzadu je:', end=' ')


def vypis_odzadu(cislo):
    if cislo < 0:
        cislo = -cislo
        print('-', end='')
    while cislo != 0:
        cifra = cislo % 10
        print(cifra, end='')
        cislo = cislo // 10

vypis_odzadu(x)
print()