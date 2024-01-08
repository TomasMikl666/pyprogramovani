# Mějme seznam hráčů a jejich nahrané skóre ve hře:
# hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]
# Vypište na obrazovku jméno nejlepšího a nejhoršího hráče podle skóre.

hraci = [("Pavel", 5), ("Honza", 3), ("Jana", 7), ("Milan", 4), ("Michaela", 9)]

nejlepsi_skore = float("-inf")
nejlepsi_hrac = None
nejhorsi_skore = float("inf")
nejhorsi_hrac = None

for jmeno, skore in hraci:
    if skore > nejlepsi_skore:
        nejlepsi_skore = skore
        nejlepsi_hrac = jmeno
    if skore < nejhorsi_skore:
        nejhorsi_skore = skore
        nejhorsi_hrac = jmeno

print(f"Nejlepší hráč: {nejlepsi_hrac} skóre: {nejlepsi_skore}")
print(f"Nejhorší hráč: {nejhorsi_hrac} skóre: {nejhorsi_skore}")
