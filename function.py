from time import sleep

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


def rhombus(x, y, x0, y0, r):
    return abs(x - x0) + abs(y - y0) * 2 <= r


def pattern(length, heigh, r, thickness):
    y0 = length // 2
    x1 = (heigh // 2) - r
    x2 = (heigh // 2) + r
    colors = [BLUE, RED, WHITE, GREEN]

    while True:
        for color in colors:
            s = ''

            for y in range(length):
                for x in range(heigh):
                    left = rhombus(x, y, x1, y0, r) and not rhombus(x, y, x1, y0, r - thickness)
                    right = rhombus(x, y, x2, y0, r) and not rhombus(x, y, x2, y0, r - thickness)

                    if left or right:
                        s += color + "  " + RESET
                    else:
                        s += "  "
                s += "\n"

            print(s, end="")
            sleep(1)


multiple_progressbar(1)
pattern(length=10, heigh=28, r=6, thickness=3)
