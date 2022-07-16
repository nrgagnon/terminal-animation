import time
from libraries.terminal_colors import WHITE, BLUE, YELLOW, RED, GREEN, CYAN, MAGENTA, BLACK, CYAN_BG, YELLOW_BG, WHITE_BG, BLACK_BG, BLUE_BG
from libraries.animation_core import print_char_at, hide_cursor, show_cursor

WIDTH = 200 
HEIGHT = 70 
PADDING = 10

def paint_background(color, screen_width, screen_height):
    for row in range(0, screen_height):
        print(color + screen_width * " ", flush = True)

class Cloud:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid = ["000000001110000", "000000111111110", "000000111111111", "001111111111111", "111111111111111", "000000000001110"]

    def draw(self, current_row, current_col):
        new_row = self.row
        new_col = self.col
        for string in self.grid:
            for num in string:
                char, color = ("@", WHITE) if int(num) == 1 else (" ", CYAN_BG)
                current_row, current_col = print_char_at(char, color, current_row, current_col, new_row, new_col)
                new_col += 1
            new_row += 1
            new_col = self.col
        print_char_at("X", RED, new_row, new_col, new_row, new_col)
        return new_row, new_col

    def animate(self, current_row, current_col):
        for i in range(0, 1):
            self.col += 1
            current_row, current_col = self.draw(current_row, current_col)
            time.sleep(0.1)
        return current_row, current_col

colors = [WHITE, BLUE, YELLOW, RED, GREEN, CYAN, MAGENTA, BLACK]
index = 0
hide_cursor()
paint_background(CYAN_BG, 240, 66)

row, col = HEIGHT, WIDTH
c1 = Cloud(10, 20)
row, col = c1.draw(row, col)
row, col = print_char_at("O", GREEN, row, col, row-1, col)
c1.draw(row, col)

time.sleep(5)

print_char_at("\n", BLACK_BG + WHITE, row, col, HEIGHT, WIDTH)
show_cursor()
