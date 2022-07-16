def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def move_cursor_forward(amount):
    print(end = "\x1b[" + str(amount) + "C", flush = True)

def move_cursor_backward(amount):
    print(end = amount * "\b", flush = True)

def move_cursor_up(amount):
    print(end = amount * "\033[F", flush = True)

def move_cursor_down(amount):
    print(end = amount * "\n", flush = True)

def print_char_at(char, color, current_row, current_column, new_row, new_column):
    if current_row < new_row:
        move_cursor_down(new_row - current_row)
        move_cursor_forward(current_column - 1)
    elif new_row < current_row:
        move_cursor_up(current_row - new_row)
        move_cursor_forward(current_column - 1)
    if current_column < new_column:
        move_cursor_forward(new_column - current_column)
    elif new_column < current_column:
        move_cursor_backward(current_column - new_column)
    print(color + char, end = "\b", flush = True)
    return new_row, new_column
