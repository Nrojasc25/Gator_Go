import pygame
import sys
from board import Board
from board import create_button
from cell import *
from constants import *
from sudoku_generator import *


def game_start_screen():
    # displays background color, title, and text for mode selection
    screen.fill(BG_COLOR)

    title_font = pygame.font.Font(None, 64)
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    mode_font = pygame.font.Font(None, 32)
    mode_text = mode_font.render("Select Game Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mode_text, mode_rect)

    # creates easy, medium, and hard buttons, uses create_button function located in board.py (not a class function)
    position = [(WIDTH // 4, HEIGHT * 3 // 4), (WIDTH // 2, HEIGHT * 3 // 4), (WIDTH * 3 // 4, HEIGHT * 3 // 4)]
    easy_button = create_button("Easy", (255, 100, 180), position[0], screen)
    medium_button = create_button("Medium", (255, 0, 230), position[1], screen)
    hard_button = create_button("Hard", (220, 0, 255), position[2], screen)

    # switches to board with difficulty based on button clicked
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    difficulty = 30
                elif medium_button.collidepoint(event.pos):
                    difficulty = 40
                elif hard_button.collidepoint(event.pos):
                    difficulty = 50

                else:  # if you click anywhere else, do nothing
                    break

                board = Board(2, 2, screen, difficulty)
                main(board)

        pygame.display.update()


def game_over_screen():
    loss_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(BG_COLOR)

    loss_surface = loss_title_font.render("Game Over :(", True, LINE_COLOR)
    loss_rectangle = loss_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(loss_surface, loss_rectangle)

    restart_text = button_font.render("Restart", True, BG_COLOR)

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))
    # screen.blit places the restart button on the screen
    screen.blit(restart_surface, restart_rectangle)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if restart_rectangle.collidepoint(event.pos):
                game_start_screen()


    pygame.display.update()

    while True:
        # This for loop accounts for the options to quit and restart the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    game_start_screen()
        pygame.display.update()

def check_if_win(screen):
    win_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(BG_COLOR)

    win_surface = win_title_font.render("Game Won!", True, LINE_COLOR)
    win_rectangle = win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(win_surface, win_rectangle)
    # Creates exit button and creates its space on the screen
    exit_text = button_font.render("Exit", True, BG_COLOR)

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
        pygame.display.update()

def main(board):#main menu screen

    # clears the screen
    screen.fill(BG_COLOR)
    # draws the board using the draw() function from Board.py
    board_buttons = board.draw(screen)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # clears the screen every time the user touches anything (for cell highlight purposes)
                screen.fill(BG_COLOR)
                # draws the board using the draw() function from Board.py
                board.draw(screen)

                # gets the coordinates where the user is clicking
                x, y = event.pos

                # this parameter serves to determine if the user is clicking inside the board
                # this will return the clicked cell's position in the board.
                if y < 600:
                    for i in range(1, 10):
                        if i * CELL_SIZE > x > i - 1 * CELL_SIZE:
                            col = i - 1
                            break
                    for j in range(1, 10):
                        if j * CELL_SIZE > y > j - 1 * CELL_SIZE:
                            row = j - 1
                            break

                    # selects the cell
                    selected_cell = board.select(row, col)
                    #selected_cell.touch=True


                    # draws the outline of the square in blue
                    #if selected_cell.touch==True:


                    pygame.draw.rect(screen, BLUE,
                                         (selected_cell.column * CELL_SIZE, selected_cell.row * CELL_SIZE, CELL_SIZE, CELL_SIZE), width=4)
                    # selected_cell.draw(screen)
                    pygame.display.update()

                # board_buttons = [reset_button, restart_button, exit_button]

                if board_buttons[0].collidepoint(event.pos):
                    # sets all cell sketched_value to 0 (this will prevent them from being drawn again)
                    board.reset_to_original()
                    board.draw(screen)
                    pygame.display.update()


                    for i in range(0, len(board.cells)):
                        for j in range(0, len(board.cells[0])):
                            board.cells[i][j].sketch_value = 0
                    main(board)  # starts a new game with the current board

                if board_buttons[1].collidepoint(event.pos):
                    game_start_screen()  # goes back to the main menu

                if board_buttons[2].collidepoint(event.pos):
                    sys.exit()  # exits the program
                else:
                    break

            # if cell has been selected, the number can be drawn, else nothing happens
            try:
                e=0
                if event.type == pygame.KEYDOWN:
                    selected = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5,
                                pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9}

                    if event.key in selected:
                        if selected_cell.value == 0:  # checks if the cell's value can be modified
                            selected_cell.sketch_value = selected[event.key]

                            # deletes the sketched value if the user attempts to write something else -->
                            # sets screen to white, redraws board, re-highlights selected cell, and redraws the sketched value
                            screen.fill(BG_COLOR)
                            board.draw(screen)
                            pygame.draw.rect(screen, BLUE,
                                             (
                                                 selected_cell.column * CELL_SIZE, selected_cell.row * CELL_SIZE,
                                                 CELL_SIZE,
                                                 CELL_SIZE), width=4)

                            selected_cell.draw(screen)

                            # i = 0
                            # for row in range(9):
                            #     for col in range(9):
                            #         cell = board.cells[row][col]
                            #         if cell.sketch_value and not cell.value == 0 or not cell.sketch_value and cell.value == 0:
                            #             i = 1
                            #
                            # if i == 0:
                            #     if board.check_board():
                            #         check_if_win(screen)
                            #     else:
                            #         game_over_screen(screen)

                            pygame.display.update()
                    if event.key==pygame.K_RETURN and selected_cell.sketch_value!=0:
                        selected_cell.value = selected_cell.sketch_value
                        board.board[row].pop(col)
                        board.board[row].insert(col,selected_cell.value)
                        for i in board.board:

                            print(i)

                        print("1", board.original)
                        print("2", board.board)
                        print("3", board.filled)
                        for event in pygame.event.get():
                            if board_buttons[0].collidepoint(event.pos):
                            # sets all cell_values to 0 (this will prevent them from being drawn again)
                                board.reset_to_original()
                            #
                            #     for i in range(0, len(board.cells)):
                            #         for j in range(0, len(board.cells[0])):
                            #             board.cells[i][j].set_cell_value = 0
                            #     board.draw(screen)
                            #
                            # main(board)  # starts a new game with the current board
                        screen.fill(BG_COLOR)
                        board.draw(screen)
                        pygame.display.update()

                    if event.key == pygame.K_BACKSPACE and board.filled[row][col]==0 and selected_cell.value != 0:
                        selected_cell.value = 0
                        screen.fill(BG_COLOR)
                        board.draw(screen)
                        pygame.display.update()


                    if event.key == pygame.K_BACKSPACE and board.filled[row][col]==0 and selected_cell.sketch_value != 0:
                        selected_cell.sketch_value = 0
                        screen.fill(BG_COLOR)
                        board.draw(screen)
                        pygame.display.update()



                        # i = 0
                        # for row in range(9):
                        #     for col in range(9):
                        #         cell = board.cells[row][col]
                        #         if cell.sketch_value and not cell.value == 0 or not cell.sketch_value and cell.value == 0:
                        #             i = 1
                        #
                        # if i == 0:
                        #
                        #     screen.fill(BG_COLOR)  # replaced by win/lose screen

                        pygame.display.update()

            except UnboundLocalError:
                pass

            pygame.display.update()

            if board.is_full():
                if board.check_board():
                    check_if_win(screen)
                else:
                    game_over_screen()
                game_over = True

    i = 0
    for row in range(9):
        for col in range(9):
            cell = board.cells[row][col]
            if cell.sketch_value and not cell.value == 0 or not cell.sketch_value and cell.value == 0:
                i = 1

    if i == 0:
        if board.check_board():
            check_if_win(screen)
        else:
            game_over_screen()

    pygame.display.update()

    #
    # pygame.init()
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption("SUDOKU")
    # game_over_font = pygame.font.Font(None, GAME_OVER_FONT)
    # game_over = False
    #
    # rem = game_start_screen(screen)
    #
    # #Creates instance of board class in order to call board methods.
    # cb = Board(2, 2, screen, rem)
    # screen.fill(BG_COLOR)
    #
    # reset_rect, restart_rect, exit_rect = cb.draw(screen)
    #
    # #Creates instance of cell class in order to call cell methods
    # # c = Cell(1, 8, 0, screen)
    # #Start screen where the Easy, Medium and Hard buttons are placed
    # e=0
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
    #             x, y = event.pos
    #             col, row = cb.click(x, y)
    #             # This if statement accounts for the reset, restart, and quit implementations
    #             if reset_rect.collidepoint(x, y):
    #                 cb.reset_to_original()
    #             if exit_rect.collidepoint(x, y):
    #                 pygame.quit()
    #             if restart_rect.collidepoint(x, y):
    #                 main()
    #
    #
    #             if 0 <= row <= 8 and 0 <= col <= 8:
    #                 if cb.original[int(row)][int(col)] == 0:
    #                     current_cell = cb.select(row, col)
    #                     selected = True
    #                     cb.draw(screen)
    #
    #             pygame.display.update()
    #         # if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
    #         #     e=1
    #         #     x, y = event.pos
    #         #     row = int(y//67.5)
    #         #     col = int(x//67.5)
    #         #     screen.fill(BG_COLOR)
    #
    #             # current_cell=b.select(x,y)
    #             # reset_rect, restart_rect, exit_rect = b.draw(screen)
    #
    #             # TA said to remove this:
    #             # for j in range(9):
    #             #     for i in range(9):
    #             #         value = cb.original[i][j]
    #             #         c = Cell(value, i, j, screen)

    #
    #
    #             if row<9 and col<9:
    #                 pygame.draw.rect(screen, BLUE, pygame.Rect(col*67,row*67,SQUARE_SIZE//3,SQUARE_SIZE//3),5)
    #         pygame.display.update()
    #
    #         if cb.is_full():
    #             if cb.check_board():
    #                 check_if_win(screen)
    #             else:
    #                 game_over_screen()
    #             game_over = True
    #             selected = False
    #
    #
    #             #
    #             # if restart_rect.collidepoint(event.pos):
    #             #     main()
    #             # if exit_rect.collidepoint(event.pos):
    #             #     sys.exit()
    #             #
    #             # if restart_rect.collidepoint(event.pos):
    #             #     game_start_screen()
    #             # if exit_rect.collidepoint(event.pos):
    #             #     sys.exit()
    #
    #
    #         # for event in pygame.event.get():
    #         #
    #         #     if event.type == pygame.KEYDOWN:
    #         #         if event.key == pygame.K_1 and e==1:
    #         #             print('m')
    #         #             if row < 9 and col < 9:
    #         #                 if current_cell == 0:
    #         #                     cb.select(row, col).set_value(1)
    #         #
    #         #                     d = Cell(1, row, col, screen)
    #         #                     d.draw(screen)
    #         #                     print(1)
    #                 #current_cell.set_sketched_value(1)
    #
    #             if event.key == pygame.K_1 and e == 1:
    #                   current_cell.set_sketched_value(1)
    #
    #         pygame.display.update()
    #             # if event.key == pygame.K_3 and e == 1:
    #             #     current_cell.set_sketched_value(3)
    #             # if event.key == pygame.K_4 and e == 1:
    #             #     current_cell.set_sketched_value(4)
    #             # if event.key == pygame.K_5 and e == 1:
    #             #     current_cell.set_sketched_value(5)
    #             # if event.key == pygame.K_6 and e == 1:
    #             #     current_cell.set_sketched_value(6)
    #             # if event.key == pygame.K_7 and e == 1:
    #             #     current_cell.set_sketched_value(7)
    #             # if event.key == pygame.K_8 and e == 1:
    #             #     current_cell.set_sketched_value(8)
    #             # if event.key == pygame.K_9 and e == 1:
    #             #     current_cell.set_sketched_value(9)
    #
    #                     # This statement checks for the win condition if the board is full






    #
    #
    #     pygame.display.update()
    #
    # #
    # while True:
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             c.touch = True
    #             x, y = event.pos
    #             row = y // SQUARE_SIZE
    #             col = x // SQUARE_SIZE
    #             print(event)
    #             screen.fill(BG_COLOR)
    #             b = Board(2, 2, screen, 1)
    #             b.draw()
    #             screen.blit(reset_surface, reset_rect)
    #             screen.blit(restart_surface, restart_rect)
    #             screen.blit(exit_surface, exit_rect)
    #
    #             for j in range(9):
    #                 for i in range(9):
    #                     value = z[i][j]
    #
    #                     c = Cell(value, i, j, screen)
    #                     c.draw()
    #             pygame.draw.rect(c.screen, BLUE,
    #                              pygame.Rect(x, y,
    #                                          SQUARE_SIZE // 3, SQUARE_SIZE // 3), 2)
    #
    #             # pygame.draw.line(screen, (0,0,255), (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), LINE_WIDTH // 3)
    #             # column, row, width, height
    #
    #             pygame.display.update()
    #
    #
    #             c.touch=False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("SUDOKU")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # this automatically passes the screen to all functions

    game_start_screen()