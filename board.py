from sudoku_generator import *
from sudoku_generator import SudokuGenerator as SG
from constants import *
import pygame
from cell import Cell
import cell


def create_button(text, color, position, screen):
    button_font = pygame.font.Font(None, 32)
    button = button_font.render(text, True, BLACK)
    surface = pygame.Surface((button.get_width() + 20, button.get_height() + 20))
    surface.fill(color)
    surface.blit(button, (10, 10))
    rect = button.get_rect(center=position)
    screen.blit(surface, rect)
    return rect  # Returns position of button created


class Board:
    def __init__(self, width,height,screen,difficulty):
        self.width = width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        #self.board = generate_sudoku(9,difficulty)
        self.filled, self.original, self.board = generate_sudoku(9,difficulty)
        self.cells=[
            [Cell(self.board[i][j], i, j, screen) for j in range(9)] for i in range(9)
        ]
        self.filled_cells = [
            [Cell(self.filled[i][j], i, j, screen) for j in range(9)] for i in range(9)
        ]

    def draw(self, screen):

        # Draws the thicker lines that divide the 3x3 board
        for i in range(1, BOARD_ROWS):  # draws the horizontal lines
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH // 3)
        for i in range(1, BOARD_COLS):  # draws the vertical lines
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 100),
                             LINE_WIDTH // 3)

        # Draws the lower line that separates the board to the buttons
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - 100), (WIDTH, HEIGHT - 100), LINE_WIDTH // 3)

        # Draws the thinner lines for each square, delimiting the cells
        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE // 3),
                             (WIDTH, i * SQUARE_SIZE // 3), LINE_WIDTH // 6)
        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE // 3, 0),
                             (i * SQUARE_SIZE // 3, HEIGHT - 100), LINE_WIDTH // 6)

        # creates reset, restart, and exit buttons
        position = [(WIDTH // 4, HEIGHT * 2.55 // 2.8), (WIDTH // 2, HEIGHT * 2.55 // 2.8),
                    (WIDTH * 3 // 4, HEIGHT * 2.55 // 2.8), screen]
        if self.difficulty == 30:
            color = (255, 100, 180)
        elif self.difficulty == 40:
            color = (255, 0, 230)
        else:
            color = (220, 0, 255)
        reset_button = create_button("Reset", color, position[0], screen)
        restart_button = create_button("Restart", color, position[1], screen)
        exit_button = create_button("Exit", color, position[2], screen)

        # draws the numbers into the cells
        for i in self.cells:
            for j in i:
                j.draw(self.screen)

        return [reset_button, restart_button, exit_button]


    def select(self, row, col):
        for i in self.cells:
            for j in i:
                if j.row == row and j.column == col:
                    j.selected = True
                    return j


    def click(self, x, y):
        row = x//67
        col = y//67
        return row, col


    def clear(self,row,col):
        pass



    def sketch(self, value):
        pass
    #do later

    def place_number(self, value):
        pass
    #do later

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.filled[i][j]
                (self.cells[i][j]).value = self.board[i][j]

        self.update_board()
        # self.draw(screen)





    def is_full(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    return False
        return True

    def update_board(self):
        for i in self.cells:
            for j in i:
                self.board[j.row][j.column] = j.value
    def find_empty(self):
        for i in range(0, 9, 1):
            for j in range(0, 9, 1):
                if SG.print_board()[i][j] == 0:
                    print(str(i)+", "+str(j))

        # original - removed
        # filled - locked in
        # board - everything


    def check_board(self):

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.original[i][j]:
                    return False
        return True
        # for row in range(9):
        #     for col in range(9):
        #         cell = self.cells[row][col]
        #         if cell.value == 0:
        #             if cell.sketch_value != self.filled[row][col]:
        #                 return False
        # return True

        # for i in range(9):
        #     for j in range(9):
        #         if self.board[i][j] != self.filled[i][j]:
        #             print(self.board[i][j])
        #             print(self.filled[i][j])
        #             return False
        # return True

        #
        # for i in range(9):
        #     for j in range(9):
        #         if self.board[i][j] != self.filled[i][j]:
        #             return False
        # return True
        #think this needs to pull the valid functions from sudoku_generator
