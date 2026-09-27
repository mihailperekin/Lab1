from time import sleep
from os import system, name


BLUE = "\033[44m"
RED = "\u001b[41m"
WHITE = "\u001b[47m"
GREEN = "\u001b[42m"
RESET = "\033[0m"
BEGIN = '\x1B[1G'


def multiple_progressbar(num_tasks):
    bar_width = 25
    for task in range(1, num_tasks+1):
        for progress in range(1, bar_width+1):
            bar = '#' * progress + '_' * (bar_width - progress)
            print(f'{BEGIN}Task {task}/{num_tasks} [{bar}] {progress * 4}%', end='', flush=True)
            sleep(0.1)
    print(" Done")


def centr(x, y, x0, y0, r):

    return (x0 - x) ** 2 + (y0 - y) ** 2 <= r**2


def rhombus(x, y, x0, y0, r):
    return abs(x - x0) + abs(y - y0) * 2 <= r


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


def pattern(length, heigh, r, thickness):
    y0 = length // 2
    x1 = (heigh // 2) - r
    x2 = (heigh // 2) + r
    colors = [BLUE, RED, WHITE, GREEN]
    system('cls' if name == 'nt' else 'clear')
    while True:
        for color in colors:
            s = ' '
            for y in range(length):
                for x in range(heigh):
                    left = rhombus(x, y, x1, y0, r) and not rhombus(x, y, x1, y0, r - thickness)
                    right = rhombus(x, y, x2, y0, r) and not rhombus(x, y, x2, y0, r - thickness)

                    if left or right:
                        s += color + "  " + RESET
                    else:
                        s += "  "
                s += "\n"

            print(s, end="", flush=True)

            sleep(1)


def sequence():
    file = open('sequence.txt','r')
    less5 = []
    more5 = []
    total = 0
    for line in file:
        num = float(line)
        if num<-5:
            less5.append(num)
        elif num>-5 and num<0:
            more5.append(num)
        total+=1
    print(f'{BLUE}{' ' * int(len(more5) / 5)}{RESET} {len(more5)/(len(more5) + len(less5)) * 100}%')
    print(f'{RED}{' ' * int(len(less5) / 5)}{RESET} {len(less5)/(len(more5) + len(less5)) * 100}%')
    file.close()


multiple_progressbar(1)
flag_japan(20,30,6) #параметры размеров флага(длина,высота, радиус круга)
multiple_progressbar(2)
sequence()
multiple_progressbar(3)
pattern(10, 28, 6, 3) #параметры узора(длина, высота, радиус, толщина)
