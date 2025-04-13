import constants
import pygame
from constants import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.sketch_value = 0
        self.value = value
        self.row = row
        self.column = col
       # self.screen = screen #maybe something else, not so sure yet?
        self.touch = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self,value):
        self.sketch_value = value

    def draw(self, screen):

        # Draws the number into the cell (unless the number is 0 for the initial board)
        if self.value != 0:
            num_font = pygame.font.SysFont('arial', 30)
            num_surface = num_font.render(str(self.value), True, BLACK)
            num_rect = num_surface.get_rect(center=(self.column * CELL_SIZE + CELL_SIZE // 2,
                                                    self.row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(num_surface, num_rect)
        elif self.sketch_value != 0:
            num_font = pygame.font.SysFont('arial', 30)
            num_surface = num_font.render(str(self.sketch_value), True, BLUE)
            num_rect = num_surface.get_rect(center=(self.column * CELL_SIZE + CELL_SIZE // 3,
                                                    self.row * CELL_SIZE + CELL_SIZE // 3))
            screen.blit(num_surface, num_rect)


    # def highlight_cell(self, screen):
    #     # Draw blue square if self.touch is True
    #     if self.touch:
    #         print(self.value)
    #         pygame.draw.rect(screen, BLUE, (self.column * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE), width = 4)
    #
        # BLACK=(0,0,0)
        # WHITE=(255,255,255)
        # RED=(255,0,0)
        # GREEN=(0,255,0)
        # BLUE=(0,0,255)
        # num_font = pygame.font.SysFont('arial', 30)
        # #drawing the surface of each number
        # n1_num=num_font.render("1", True, BLACK)
        # n2_num=num_font.render("2", True, BLACK)
        # n3_num=num_font.render("3", True, BLACK)
        # n4_num=num_font.render("4", True, BLACK)
        # n5_num=num_font.render("5", True, BLACK)
        # n6_num=num_font.render("6", True, BLACK)
        # n7_num=num_font.render("7", True, BLACK)
        # n8_num=num_font.render("8", True, BLACK)
        # n9_num=num_font.render("9", True, BLACK)
        #
        #
        # sketched_value1 = num_font.render("1", True, BLUE)
        # # sketched_value2 = num_font.render("2", True, BLUE)
        # # sketched_value3 = num_font.render("3", True, BLUE)
        # # sketched_value4 = num_font.render("4", True, BLUE)
        # # sketched_value5 = num_font.render("5", True, BLUE)
        # # sketched_value6 = num_font.render("6", True, BLUE)
        # # sketched_value7 = num_font.render("7", True, BLUE)
        # # sketched_value8 = num_font.render("8", True, BLUE)
        # # sketched_value9 = num_font.render("9", True, BLUE)
        # #
        # # saved_value1 = num_font.render("1", True, BLACK)
        # # saved_value2 = num_font.render("2", True, BLACK)
        # # saved_value3 = num_font.render("3", True, BLACK)
        # # saved_value4 = num_font.render("4", True, BLACK)
        # # saved_value5 = num_font.render("5", True, BLACK)
        # # saved_value6 = num_font.render("6", True, BLACK)
        # # saved_value7 = num_font.render("7", True, BLACK)
        # # saved_value8 = num_font.render("8", True, BLACK)
        # # saved_value9 = num_font.render("9", True, BLACK)
        #
        #
        # # Font = pygame.font(Font(None, 25))
        # #
        # # Text = font.render(str(self.sketched_value)
        #
        # # border_color = BLUE if self.touch else LINE_COLOR
        # # border_thickness = 2 if self.touch else 1
        # # pygame.draw.rect(self.screen, border_color,
        # #                  pygame.Rect(self.column * SQUARE_SIZE//3, self.row * SQUARE_SIZE//3, SQUARE_SIZE//3, SQUARE_SIZE//3), border_thickness)
        #                   # column, row, width, height
        # if self.touch==True:
        #     # pygame.draw.rect(self.screen, BLUE,
        #     #                  pygame.Rect(self.column * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
        #     pygame.draw.rect(screen, BLUE,
        #                      pygame.Rect(self.column * 67, self.row * 67, SQUARE_SIZE // 3, SQUARE_SIZE // 3), 5)
        # #
        #     self.touch = False
        # #
        # if self.sketch_value == 1:
        #     num_rect = sketched_value1.get_rect(
        #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        #     screen.blit(sketched_value1, num_rect)
        # # if self.sketch_value == 2:
        # #     num_rect = sketched_value2.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value2, num_rect)
        # # if self.sketch_value == 3:
        # #     num_rect = sketched_value3.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value3, num_rect)
        # # if self.sketch_value == 4:
        # #     num_rect = sketched_value4.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value4, num_rect)
        # # if self.sketch_value == 5:
        # #     num_rect = sketched_value5.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value5, num_rect)
        # # if self.sketch_value == 6:
        # #     num_rect = sketched_value6.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value6, num_rect)
        # # if self.sketch_value == 7:
        # #     num_rect = sketched_value7.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value7, num_rect)
        # # if self.sketch_value == 8:
        # #     num_rect = sketched_value8.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value8, num_rect)
        # # if self.sketch_value == 9:
        # #     num_rect = sketched_value9.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(sketched_value9, num_rect)
        # #
        # #
        # #
        # # if self.value == 1:
        # #     num_rect = saved_value1.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value1, num_rect)
        # # if self.value == 2:
        # #     num_rect = saved_value2.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value2, num_rect)
        # # if self.value == 3:
        # #     num_rect = saved_value3.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value3, num_rect)
        # # if self.value == 4:
        # #     num_rect = saved_value4.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value4, num_rect)
        # # if self.value == 5:
        # #     num_rect = saved_value5.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value5, num_rect)
        # # if self.value == 6:
        # #     num_rect = saved_value6.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value6, num_rect)
        # # if self.value == 7:
        # #     num_rect = saved_value7.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value7, num_rect)
        # # if self.value == 8:
        # #     num_rect = saved_value8.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value8, num_rect)
        # # if self.value == 9:
        # #     num_rect = saved_value9.get_rect(
        # #         center=((SQUARE_SIZE * self.column) / 3 + SQUARE_SIZE // 6, (SQUARE_SIZE * self.row) / 3 + SQUARE_SIZE // 6))
        # #     screen.blit(saved_value9, num_rect)
        #
        #
        #
        # if self.value==1:
        #     num_rect=n1_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n1_num, num_rect)
        # if self.value==2:
        #     num_rect=n2_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n2_num, num_rect)
        #
        # if self.value==3:
        #     num_rect=n3_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n3_num, num_rect)
        #
        # if self.value==4:
        #     num_rect=n4_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n4_num, num_rect)
        #
        # if self.value==5:
        #     num_rect=n5_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n5_num, num_rect)
        #
        # if self.value==6:
        #     num_rect=n6_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n6_num, num_rect)
        #
        # if self.value==7:
        #     num_rect=n7_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n7_num, num_rect)
        #
        #
        # if self.value==8:
        #     num_rect=n8_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n8_num, num_rect)
        #
        #
        # if self.value==9:
        #     num_rect=n9_num.get_rect(
        #         center=((SQUARE_SIZE * self.column)/3 + SQUARE_SIZE//6, (SQUARE_SIZE * self.row)/3 + SQUARE_SIZE//6))
        #     screen.blit(n9_num, num_rect)
        #







