choice = int(input("Menge an zeichen eingeben (minimum 10, maximum 20): "))
Werteliste = []
if choice > 10 or choice < 20:
    for i in range(0, choice):
        Wert = int(input("Wert für liste eingeben: "))
        Werteliste.append(Wert)
    print(f"Die Werteliste ist: {Werteliste}")
    for i in range(0, choice - 1):
        if Werteliste[i] > Werteliste[i + 1]:
            print(f"Der Wert an Stelle " + str(i) + " ist größer als der Wert an stelle "+ str(i+1))
        elif Werteliste[i] < Werteliste[i + 1]:
            print(f"Der Wert an Stelle " + str(i) + " ist kleiner als der Wert an stelle "+ str(i+1))
        else:
            print(f"Die Werte an Stelle " + str(i) + " und " + str(i+1) + " sind gleich")
        if Werteliste[i + 1] == Werteliste[i] * 4:
            print(f"Der Wert an Stelle " + str(i + 1) +" ist das Vierfache des Wertes an Stelle " + str(i))