import pygame
import random

class my_game:
    def __init__(self, width = 640, height = 480, cell_size = 10, speed = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        # Устанавливаем карту
        self.set_map()

    def draw_grid(self):
        for y in range(0, self.width, self.cell_size):
            for x in range(0, self.width, self.cell_size):
                pygame.draw.line(self.screen, pygame.Color('black'),
                                 (x, 0), (x, self.height))
            for y in range(0, self.height, self.cell_size):
                pygame.draw.line(self.screen, pygame.Color('black'),
                                 (0, y), (self.width, y))

    def draw_game_map(self):
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.game_map[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
        self.draw_grid()

    def get_neighboards(self, px, py):
        def get_if_exist(self, x, y):
            if 0 <= x < self.cell_width and 0 <= y < self.cell_height:
                return self.game_map[y][x]
            return 0

        num = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                if not (y == 0 and x == 0):
                    num += get_if_exist(self, px + x, py + y)
        return num

    def update_position(self):
        new_map = [[0 for j in range(self.cell_width)] for i in range(self.cell_height)]
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                num = self.get_neighboards(x, y)
                cur = self.game_map[y][x]
                if cur == 1:
                    if num > 3 or num < 2:
                        new_map[y][x] = 0
                    else:
                        new_map[y][x] = 1
                else:
                    if num == 3:
                        new_map[y][x] = 1
                    else:
                        new_map[y][x] = 0
        self.game_map = new_map

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('My game')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_game_map()
            self.update_position()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def set_map(self, randomize = True):
        if randomize:
            self.game_map = [[random.randint(0, 1) for j in range(self.cell_width)] for i in range(self.cell_height)]
        else:
            self.game_map = [[0 for j in range(self.cell_width)] for i in range(self.cell_height)]


if __name__ == '__main__':
    game = my_game(1280, 960, 20, 10000)
    game.run()
