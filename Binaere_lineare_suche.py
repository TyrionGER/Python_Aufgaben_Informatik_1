def binaere(array, zahl):
    uhalb = 0
    ohalb = len(array)
    while uhalb < ohalb + 1:
        interval = (uhalb + ohalb) // 2
        interval = int(interval)
        if array[interval] == zahl:
            return interval

        elif array[interval] < zahl:
            uhalb = interval + 1
        else:
            ohalb = interval - 1

def lineare(array):
    i = 0
    while i < len(array):
        if (array[i] == zahl):
            return i
        else:
            i = i + 1

array = [10, 15, 25, 30, 31, 42, 52, 60, 75, 100]
zahl = input("Gesuchte Zahl eingeben:  ")
zahl = int(zahl)
choice = input("1 fuer binaere oder 2 für lineare Suche eingeben: ")
index = len(array)
if choice == 1:
    print(binaere(array, zahl) + 1)
else:
    print(lineare(array) + 1)