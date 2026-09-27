BLUE = "\033[44m"
RED = "\u001b[41m"
WHITE = "\u001b[47m"
GREEN = "\u001b[42m"
RESET = "\033[0m"
BEGIN = '\x1B[1G'

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

sequence()