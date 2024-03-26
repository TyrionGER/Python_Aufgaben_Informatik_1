def aufg1(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    print(sum)


def aufg2(array):
    sum = 0
    sum2 = 0
    for i in range(len(array)):
        sum += array[i]
    avg = sum / len(array)
    print(avg)
    for i in range(len(array)):
        helper = array[i] - avg
        sum2 += helper ** 2
    vari = sum2 / len(array)
    stdabw = vari ** 0.5
    print(round(stdabw, 2))


choice2 = int(input("type 1 for Aufgabe 1 type 2 for Aufgabe 2: "))
choice1 = int(input("choose length of the array: "))
array = []
for i in range(choice1):
    nmbr = int(input("input number for array: "))
    array.append(nmbr)
if 1 == choice2:
    aufg1(array)
elif 2 == choice2:
    aufg2(array)
else:
    print("restart Program and try again")
