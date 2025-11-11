# PRÍKLAD 7: Spájanie stringov
# ============================================================================
"""
Máte zoznam slov: ["Python", "je", "super"]
Spojte ich do jednej vety pomocou join() (oddelené medzerami).
Bonus: Spojte ich aj pomocou pomlčky "-".
"""

# Vaše riešenie:
slova = ["Python", "je", "super"]


# spojenie slov do vety pomocou medzery
veta = " ".join(slova)

# spojenie slov pomocou pomlčky
veta_s_pomlckou = "-".join(slova)

# vypis vysledkov
print("Spojené medzerou:", veta)
print("Spojené pomlčkou:", veta_s_pomlckou)
