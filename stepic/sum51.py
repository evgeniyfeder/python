class Buffer:
    part_size = 5
    def __init__(self):
        self.data = []
        self.cur_sum = 0

    def add(self, *a):
        i = 0
        global_ind = len(self.data)
        while i < len(a):
            if global_ind % Buffer.part_size == 0 and len(self.data) != 0:
                print(self.cur_sum)
                self.cur_sum = 0
                self.data.clear()
            self.data.append(a[i])
            self.cur_sum += a[i]
            i += 1
            global_ind += 1
            
    def get_current_part(self):
        print(self.data)
        return self.data

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() 
buf.add(4, 5, 6)
buf.get_current_part() 
buf.add(7, 8, 9, 10) 
buf.get_current_part() 
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) 
buf.get_current_part() 