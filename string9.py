# PRÍKLAD 8: Hľadanie pozície podreťazca
# ============================================================================
"""
V stringu "Programovanie v Pythone je zábavné"
Nájdite pozíciu slova "Python" pomocou find() a index().
Vypíšte obe pozície.
Bonus: Skúste nájsť slovo "Java" pomocou find() - čo sa stane?
"""

# Vaše riešenie:
text = "Programovanie v Pythone je zábavné"


# hľadanie pozície slova "Python" pomocou find()
pozicia_find = text.find("Python")

# hľadanie pozície slova "Python" pomocou index()
pozicia_index = text.index("Python")

# vypíšeme pozície
print("Pozícia (find):", pozicia_find)
print("Pozícia (index):", pozicia_index)

# BONUS – hľadáme slovo "Java"
pozicia_java = text.find("Java")
print("Pozícia slova 'Java' (find):", pozicia_java)
