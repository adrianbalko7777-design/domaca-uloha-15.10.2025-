# PRÍKLAD 5: Práca s medzerami
# ============================================================================
"""
Máte string: "   Python   "
Odstráňte medzery na začiatku, na konci a na oboch stranách.
Vypíšte všetky tri varianty (každú v apostrofoch aby boli vidieť medzery).
"""

# Vaše riešenie:
text = "   Python   "

# PRÍKLAD 5: Práca s medzerami
# ============================================================================

# pôvodný text
text = "   Python   "

# odstránenie medzier zľava
zlava = text.lstrip()

# odstránenie medzier sprava
sprava = text.rstrip()

# odstránenie medzier z oboch strán
obes = text.strip()

# výpis výsledkov (v apostrofoch, aby bolo vidieť medzery)
print("Pôvodný text: '" + text + "'")
print("Bez medzier zľava: '" + zlava + "'")
print("Bez medzier sprava: '" + sprava + "'")
print("Bez medzier z oboch strán: '" + obes + "'")
