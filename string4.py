# PRÍKLAD 3: Hľadanie a nahrádzanie
# ============================================================================
"""
Máte string: "Učím sa Java. Java je záživná."
Nahraďte všetky výskyty "Java" slovom "Python".
Vypíšte pôvodný aj nový text.
"""

# Vaše riešenie:


# Pôvodný text
text = "Učím sa Java. Java je záživná."

# nahradime 'Java' slovom 'Python'
novy_text = text.replace("Java", "Python")
novy_text = text.replace("záživná", "záživny")

# vypiseme povodny aj novy text
print("Pôvodný text:", text)
print("Nový text:", novy_text)
