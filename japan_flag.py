WHITE = "\033[107m"
RED = "\033[41m"
RESET = "\033[0m"


def centr(x, y, x0, y0, r):

    if (x0 - x) ** 2 + (y0 - y) ** 2 <= r**2:
        return True
    else:
        return False


def flag_japan(length, heigh, r):
    y0 = length//2
    x0 = heigh//2
    s = ''
    for y in range(length):
        for x in range(heigh):
            if centr(x, y, x0, y0,r):
                s += RED + "  " + RESET
            else:
                s += WHITE + "  " + RESET
        s += '\n'
    print(s)


flag_japan(20,30,6)