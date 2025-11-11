# PRÍKLAD 6: Overovanie obsahu stringu
# ============================================================================
"""
Napíšte program, ktorý overí, či string obsahuje iba číslice.
Otestujte na týchto stringoch: "12345", "123abc", "3.14"
Pre každý vypíšte, či je číselný alebo nie.
"""

# Vaše riešenie:
test1 = "12345"
test2 = "123abc"
test3 = "3.14"


# funkcia, ktorá vypíše, či je string číselný
def over_string(text):
    if text.isdigit():
        print(text, "→ obsahuje iba číslice")
    else:
        print(text, "→ neobsahuje iba číslice")

# otestujeme všetky tri
over_string(test1)
over_string(test2)
over_string(test3)
