import pygame

UWU = [
    (1, 6), (1, 7), (1, 8), (2, 8), (3, 6), (3, 7), (3, 8),
    (5, 6), (5, 7), (5, 8), (6, 8), (7, 6), (7, 7), (7, 8), (8, 8), (9, 6), (9, 7), (9, 8),
    (11, 6), (11, 7), (11, 8), (12, 8), (13, 6), (13, 7), (13, 8)
]


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if (y, x) in UWU:
                    self.board[x][y] = 1
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        col = ['pink', 'white']
        for j in range(self.width):
            for i in range(self.height):
                pygame.draw.rect(screen, pygame.Color(col[self.board[i][j]]),
                                 (self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                                  self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_y < 0 or cell_x >= self.width or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell):
        self.board[cell[1]][cell[0]] += 1
        if self.board[cell[1]][cell[0]] > 1:
            self.board[cell[1]][cell[0]] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    board = Board(15, 15)
    running = True
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()

    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()  # смена кадра
        # изменение игрового мира
        # ...
        # временная задержка
        clock.tick(fps)

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()
