d = dict()
n = int(input())

def check_exist(name, l):
    if name not in d:
        d[name] = l
        return False
    return True
   
def add_win(name):
    if check_exist(name, [1, 0, 0]):
        d[name][0] += 1
    return

def add_lose(name):
    if check_exist(name, [0, 0, 1]):
        d[name][2] += 1
    return

def add_mid(name):
    if check_exist(name, [0, 1, 0]):
        d[name][1] += 1
    return


for i in range(n):
    match = input().split(';')
    if match[1] == match[3]:
        add_mid(match[0])
        add_mid(match[2])
        continue        
    lose = 1
    win = 3
    if match[1] > match[3]:
        win = 1
        lose = 3
    add_win(match[win - 1])
    add_lose(match[lose - 1])

for key, value in d.items():
    print(key, end=':')
    print(value[0] + value[1] + value[2], value[0], value[1], value[2], 3 * value[0] + value[1])