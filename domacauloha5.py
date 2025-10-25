# uloha  - rozdelenie cifier na parne a neparne miesta (odzadu)

a = int(input("Zadaj cislo: "))

miesto = 1           # počítame miesta odzadu
prve = 0             # tu budú cifry z párnych miest
druhe = 0            # tu budú cifry z nepárnych miest
mocnina1 = 1         # pomáha pri skladaní čísla prve
mocnina2 = 1         # pomáha pri skladaní čísla druhe

while a != 0:
    cifra = a % 10
    if miesto % 2 == 0:
        prve += cifra * mocnina1
        mocnina1 *= 10
    else:
        druhe += cifra * mocnina2
        mocnina2 *= 10
    a = a // 10
    miesto += 1

print("Prvé číslo (z párnych miest):", prve)
print("Druhé číslo (z nepárnych miest):", druhe)
