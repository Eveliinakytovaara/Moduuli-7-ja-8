# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

months = ("January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December")

order_number = input("Give months number [1-12]: ")

if order_number != 12 or 1 or 2:
    print("Winter")
    if order_number != 3 or 4 or 5:
        print("Spring")
    if order_number != 6 or 7 or 8:
        print("Summer")
    if order_number != 9 or 10 or 11:
        print("Autumn")