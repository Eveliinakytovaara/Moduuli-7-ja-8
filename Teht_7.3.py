
def choose():
    print("1 Add")
    print("2 Search")
    print("0 End")
    choose = -1
    while choose < 0 or valinta >2:
        choose= int(input("Choose number: "))
        return choose




def addNew(airports):
    ICAO = input("Airpots ICAO-code: ")
    name = input ("Airports name: ")
    airports[ICAO] = name



def search(airports):
    ICAO = input("Airports name")
    if ICAO in airports:
        print(airports[ICAO])
    else:
        print("Unknown ICAO-code")



airports = {}
valinta = choose()
while valinta !=0:
    if valinta == 1:
        addNew(airports)
    elif valinta == 2:
        search(airports)
    valinta = choose()