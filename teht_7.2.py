# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä. Kunkin nimen syöttämisen jälkeen
# ohjelma tulostaa, joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi
# kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

names = {"Milla", "Paavo", "Helmi"}
print(names)
names.add("Eerik")
if "Eerik" in names:
    print("Already on the list")
else:
    print("New name added to the list")
print(names)
names.add("Aaro")
if "Aaro" in names:
    print("Already on the list")
else:
    print("New name added to the list")
print(names)



