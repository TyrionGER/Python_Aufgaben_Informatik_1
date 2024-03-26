str1 = input("Hier zu verschlüsselndes Wort eingeben: ")
caesar = int(input("Hier Schuessel eingeben: "))

result = ""
for char in str1:
    order = ord(char)
    if order >= ord('A') and order <= ord('Z'):
        order = order + caesar
        if order > ord('Z'):
            order = order - 26
    if order >= ord('a') and order <= ord('z'):
        order = order + caesar
        if order > ord('z'):
            order = order - 26
    result += chr(order)

print(result)
