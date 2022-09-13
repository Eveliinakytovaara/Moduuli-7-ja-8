# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
# kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

maakoodi = input("Enter 2 letter country code, please: ")
sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = '"+maakoodi+"' GROUP BY TYPE"
print(sql)


kursori = yhteys.cursor()
kursori.execute(sql)

tulos= kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")
