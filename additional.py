RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]
for i in range(10):
    result[i] = 3 * i


step = round(abs(result[0] - result[9]) / 9, 2)


for i in range(10):
    plot_list[i][0] = step * (9 - i)


for i in range(10):
    for j in range(10):

        if abs(plot_list[i][0] - result[j]) < step / 2:
            plot_list[i][j] = 1

for i in range(10):
    line = ''
    for j in range(10):
        if j == 0:
            line += f'{int(plot_list[i][j])}\t'
        else:
            if plot_list[i][j] == 0:
                line += '-- '
            if plot_list[i][j] == 1:
                line += '!! '
    print(line)

print('0\t 1  2  3  4  5  6  7  8  9')
