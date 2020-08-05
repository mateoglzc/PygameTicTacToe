import pygame as pg
import pygame.freetype
import sys
import copy

# Initialize pg
pg.init()
# Create clock for framerate
clock = pg.time.Clock()

# Font
font_s = 30
myfont = pygame.freetype.SysFont('Comic Sans MS', font_s)


# Objects

# Board
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Square dimensions (withd, height)
square_d = (266, 200)

# Colors
white = pg.Color(255, 255, 255)
black = pg.Color(0, 0, 0)
red = pg.Color("red")

# Screen
screen_w = 800
screen_h = 600
screen = pg.display.set_mode((screen_w, screen_h + 100))

turn = 1
error = False


def select_spot(i, j, x_o: str):
    global error
    error = False
    if board[i][j] == "":
        board[i][j] = x_o
    else:
        error = True


def check_if_won(lol, player: str) -> bool:
    board_ = copy.deepcopy(lol)
    win_list = []
    i = 0
    for row in board_:
        counter = 0
        for obj in row:
            if player == obj:
                win_list.append(board_[i].index(obj))
                board_[i][counter] = "i"
            counter += 1
        i += 1
    if win_list.count(0) == 3:
        return True
    if win_list.count(1) == 3:
        return True
    if win_list.count(2) == 3:
        return True
    if 0 in win_list and 1 in win_list and 2 in win_list:
        return True
    else:
        return False


yey = [["X", "O", "O"], ["O", "X", "X"], ["X", "X", "X"]]
check_if_won(yey, "X")

# Game loop
while True:

    error_message = myfont.render("That spot is occupied!", red)
    won_message_x = myfont.render("X's won!", black)
    won_message_o = myfont.render("O's won!", black)

    # Event checker
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if turn == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check the position of the mouse
                pos = pg.mouse.get_pos()
                # Upper Row
                if (0 < pos[0] < 262) and (0 < pos[1] < 196):
                    select_spot(0, 0, "X")
                    turn = 2
                if (270 < pos[0] < 528) and (0 < pos[1] < 196):
                    select_spot(0, 1, "X")
                    turn = 2
                if (532 < pos[0] < 794) and (0 < pos[1] < 196):
                    select_spot(0, 2, "X")
                    turn = 2
                # Middle Row
                if (0 < pos[0] < 262) and (204 < pos[1] < 396):
                    select_spot(1, 0, "X")
                    turn = 2
                if (270 < pos[0] < 528) and (204 < pos[1] < 396):
                    select_spot(1, 1, "X")
                    turn = 2
                if (532 < pos[0] < 794) and (204 < pos[1] < 396):
                    select_spot(1, 2, "X")
                    turn = 2
                # Lower Row
                if (0 < pos[0] < 262) and (404 < pos[1] < 596):
                    select_spot(2, 0, "X")
                    turn = 2
                if (270 < pos[0] < 528) and (404 < pos[1] < 596):
                    select_spot(2, 1, "X")
                    turn = 2
                if (532 < pos[0] < 794) and (404 < pos[1] < 596):
                    select_spot(2, 2, "X")
                    turn = 2
            if event.type == pg.MOUSEBUTTONUP:
                pos = None

        else:
            if event.type == pg.MOUSEBUTTONDOWN:
                # Check the position of the mouse
                pos = pg.mouse.get_pos()
                # Upper Row
                if (0 < pos[0] < 262) and (0 < pos[1] < 196):
                    select_spot(0, 0, "O")
                    turn = 1

                if (270 < pos[0] < 528) and (0 < pos[1] < 196):
                    select_spot(0, 1, "O")
                    turn = 1

                if (532 < pos[0] < 794) and (0 < pos[1] < 196):
                    select_spot(0, 2, "O")
                    turn = 1

                # Middle Row
                if (0 < pos[0] < 262) and (204 < pos[1] < 396):
                    select_spot(1, 0, "O")
                    turn = 1

                if (270 < pos[0] < 528) and (204 < pos[1] < 396):
                    select_spot(1, 1, "O")
                    turn = 1

                if (532 < pos[0] < 794) and (204 < pos[1] < 396):
                    select_spot(1, 2, "O")
                    turn = 1

                # Lower Row
                if (0 < pos[0] < 262) and (404 < pos[1] < 596):
                    select_spot(2, 0, "O")
                    turn = 1

                if (270 < pos[0] < 528) and (404 < pos[1] < 596):
                    select_spot(2, 1, "O")
                    turn = 1

                if (532 < pos[0] < 794) and (404 < pos[1] < 596):
                    select_spot(2, 2, "O")
                    turn = 1

            if event.type == pg.MOUSEBUTTONUP:
                pos = None

    print(board)
    # Display Color
    # Only takes rgb or rgba
    screen.fill((255, 255, 255))

    # Draw

    # line(surface, color, (start_pos) {x,y}, (end_pos) {x,y}, withd=1)
    pg.draw.line(screen, black, (0, screen_h/3), (screen_w, screen_h/3), 4)
    pg.draw.line(screen, black, (0, 2*screen_h/3), (screen_w, 2*screen_h/3), 4)
    pg.draw.line(screen, black, (screen_w/3, 0), (screen_w/3, screen_h), 4)
    pg.draw.line(screen, black, (2*screen_w/3, 0), (2*screen_w/3, screen_h), 4)

    # Crosses and O's
    width_c = square_d[0]/2 - font_s/2
    height_c = square_d[1]/2 - font_s/2

    for i in board:
        w_c = width_c
        for j in i:
            textarea = myfont.render(j, black)
            screen.blit(textarea[0], (w_c, height_c))
            w_c += square_d[0]
        height_c += square_d[1]

    if error:
        screen.blit(
            error_message[0], (screen_w/2 - font_s/2, screen_h +
                               50 - font_s/2))

    # Check if someone won
    if check_if_won(board, "X"):
        screen.blit(won_message_x[0], (screen_w/2 - font_s/2 - 100, screen_h +
                                       50 - font_s/2))
        pg.quit()
        sys.exit()

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
