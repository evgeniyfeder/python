def get_data(x, y, n, data):
    return int(data[(y + n) % n][(x + n) % n])

table = []
str = input()
n = 0
while str != 'end':
    table.append(str.split())
    n += 1
    str = input()

if n == 1:
    print(4 * int(table[0][0]))
else:
    for y in range(n):
        for x in range(n):
            print(get_data(x + 1, y, n, table) + 
                  get_data(x - 1, y, n, table) +
                  get_data(x, y + 1, n, table) +
                  get_data(x, y - 1, n, table), end = ' ')
        print()
        

    