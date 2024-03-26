def fibo(start, erg, x, end):
    erg += erg + start
    x = x+1
    if erg < end:
        return fibo(start, erg, x, end)
    else:
        print("Menge an Wiederholungen: ", x)
        return erg

start = int(input("Hier Startzahl eingeben: "))
end = int(input("Hier Endzahl eingeben: "))
erg = 1
x = 1
erg = fibo(start, erg, x, end)
print(erg)