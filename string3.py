# PRÍKLAD 2: Zisťovanie dĺžky a počítanie znakov
# ============================================================================
"""
Máte vetu: "Python je skvelý programovací jazyk"
Zistite dĺžku vety a koľkokrát sa v nej vyskytuje písmeno 'a'.
Výsledky vypíšte vo formáte: "Dĺžka: X, Počet 'a': Y"
"""

# Vaše riešenie:
veta = "Python je skvelý programovací jazyk"


# zistime dlzku vety (pocet znakov)
dlzka = len(veta)

# spocitame, kolkokrat sa vyskytuje pismeno 'a'
pocet_a = veta.count('a')

# vypiseme vysledok
print("Dĺžka:", dlzka, ", Počet 'a':", pocet_a)
