# uloha - Collatzova postupnost
# pravidla:
# ak je cislo parne -> vydel 2
# ak je cislo neparne -> vynasob 3 a pripocitaj 1
# postupnost konci, ked sa dostaneme na 1

x = int(input("Zadaj číslo: "))

print("Collatzova postupnosť pre číslo", x, ":")

while x != 1:
    print(x, end=" -> ")   # vypis cislo a sipku
    if x % 2 == 0:         # ak je parne
        x = x // 2
    else:                  # ak je neparne
        x = 3 * x + 1

print(1)   # nakoniec vypiseme jednotku
