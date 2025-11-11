# PRÍKLAD 9: Kontrola začiatku a konca stringu
# ============================================================================
"""
Máte názov súboru: "dokument.pdf"
Skontrolujte, či sa končí príponou .pdf.
Skontrolujte, či sa začína slovom "dokument".
Vypíšte výsledky oboch kontrol.
"""

# Vaše riešenie:
nazov = "dokument.pdf"

# skontrolujeme, či sa končí na '.pdf'
koniec = nazov.endswith(".pdf")

# skontrolujeme, či sa začína na 'dokument'
zaciatok = nazov.startswith("dokument")

# vypíšeme výsledky
print("Končí na '.pdf':", koniec)
print("Začína na 'dokument':", zaciatok)
