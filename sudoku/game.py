import data
from pprint import pprint


class game:
    def __init__(self, input_file):
        self.grid = data.data(input_file)
        pprint(self.grid.digits)

    def find_next_empty(self, begin_coord):
        exit_flag = False
        res = (-1, -1)
        for y in range(begin_coord[1], self.grid.n):
            if y == begin_coord[1]:
                begin_x = begin_coord[0]
            else:
                begin_x = 0

            for x in range(begin_x, self.grid.n):
                if self.grid.digits[y][x] == '.':
                    res = (x, y)
                    exit_flag = True
                    break
            if exit_flag:
                break
        return res

    def get_existed_numbers(self, cur_coord):
        row, col, block = (self.grid.get_row(cur_coord),
                           self.grid.get_col(cur_coord),
                           self.grid.get_block(cur_coord))

        res = []
        for i in range(1, self.grid.max_number + 1):
            cur = str(i)
            if not (cur in row or cur in col or cur in block):
                res.append(cur)
        return res

    def solve(self, cur_coord):
        next = self.find_next_empty(cur_coord)

        if next == (-1, -1):
            pprint(self.grid.digits)
            return

        can_num = self.get_existed_numbers(next)

        for i in can_num:
            self.grid.digits[next[1]][next[0]] = str(i)
            self.solve(next)
            self.grid.digits[next[1]][next[0]] = '.'

g = game("a.txt")
g.solve((0,0))

