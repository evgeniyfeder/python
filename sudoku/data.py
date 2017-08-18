from math import sqrt


class data:
    def __init__(self, filename):
        self.n = len(self.digits)
        self.digits = [i for i in open(filename).read() if i in '123456789.']
        self.group()

    # Read from file module
    def group(self):
        res = []
        for i in range(self.n):
            cur = []
            for j in range(self.n):
                cur.append(self.digits[i * self.n + j])
            res.append(cur)
        return res

    # Read with table module
    def get_row(self, pos):
        res = []
        for i in range(self.n):
            res.append(self.digits[pos[0]][i])
        return res

    def get_col(self, pos):
        res = []
        for i in range(self.n):
            res.append(self.digits[i][pos[1]])
        return res

    def get_block(self, pos):
        res = []
        block_size = int(sqrt(self.n))

        begin_x = (pos[0] / block_size) * block_size
        begin_y = (pos[1] / block_size) * block_size
        end_x = (pos[0] / block_size + 1) * block_size
        end_y = (pos[1] / block_size + 1) * block_size

        for y in range(begin_y, end_y):
            row = []
            for x in range(begin_x, end_x):
                row.append(self.digits[y][x])
            res.append(row)
        return res
