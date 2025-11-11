# PRÍKLAD 10: Formátovanie stringov
# ============================================================================
"""
Vytvorte vizitku s týmito údajmi:
Meno: "Anna Kováčová", Vek: 25, Mesto: "Bratislava"

Použijte f-stringy na vytvorenie pekne formátovaného výstupu.
Vizitka by mala vyzerať takto:

========================================
Meno: Anna Kováčová
Vek: 25 rokov
Mesto: Bratislava
========================================
"""

# Vaše riešenie:
meno = "Anna Kováčová"
vek = 25
mesto = "Bratislava"

# vytvorenie vizitky pomocou f-stringov
print("========================================")
print(f"Meno: {meno}")
print(f"Vek: {vek} rokov")
print(f"Mesto: {mesto}")
print("========================================")
