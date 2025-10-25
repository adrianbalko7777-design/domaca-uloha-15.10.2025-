# uloha - vypis vsetkych delitelov daneho cisla

x = int(input("Zadaj číslo: "))

print("Delitelia čísla", x, "sú:")

# prechadzame vsetky cisla od 1 po x
i = 1
while i <= x:
    if x % i == 0:        # ak je delitelne bez zvysku
        print(i)
    i += 1
