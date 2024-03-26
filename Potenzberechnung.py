def potenz(x, zahl, erg):
    erg = erg * zahl
    x -= 1
    if x > 1:
        return potenz(x, zahl, erg)
    else:
        return erg

zahl = int(input("Hier Zahl eingeben: "))
x = int(input("Hier Exponent eingeben: "))
if x <=1:
    erg = zahl
else:
    erg = potenz(x, zahl, zahl)
print(erg)