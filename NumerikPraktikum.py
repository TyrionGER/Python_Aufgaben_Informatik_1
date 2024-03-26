def quad(a, n, z):
    h = 1
    if n >= 2:
        while h == 1:
            a += 1
            x = quad2(a, n, a)
            y = quad2(a + 1, n, a + 1)
            if x <= z and y >= z:
                h = 0
        return a


def quad2(a, n, erg):
    if n >= 2:
        erg = erg * a
        n -= 1
        return quad2(a, n, erg)
    elif n < 2:
        return erg


def root(a, n, z):
    i = 0
    while i == 0:
        f = quad2(a, n, a)
        if 0.001 >= (z - f) >= -0.001:
            i = 1
        elif f < z:
            a = a + (((z - a) * 0.5) / z)
        elif f > z:
            a = a - (((z - a) * 0.5) / z)
    return a



a = 0
z = float(input("Enter number for root: "))
n = int(input("Enter number for n >= 2: "))
a = quad(a, n, z)
result = root(a, n, z)
print("", round(result, 2))