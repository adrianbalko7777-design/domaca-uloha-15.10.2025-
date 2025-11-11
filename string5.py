# PRÍKLAD 4: Rozdeľovanie stringov
# ============================================================================
"""
Máte email: "jan.novak@example.com"
Rozdeľte ho na používateľské meno a doménu pomocou split().
Vypíšte vo formáte: "Používateľ: XXX, Doména: YYY"
"""

# Vaše riešenie:
email = "jan.novak@example.com"



# rozdelime email podla znaku '@'
casti = email.split("@")

# prva cast je pouzivatel, druha je domena
pouzivatel = casti[0]
domena = casti[1]

# vypis vysledku
print("Používateľ:", pouzivatel, ", Doména:", domena)
