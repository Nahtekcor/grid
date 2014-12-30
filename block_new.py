import pygame
class Block():
    rect_width = 0
    rect_height = 0
    rect_x = 0
    rect_y = 0
    rect_color = 0
    def __init__(self, color, width, height):
        self.rect_color = color
        self.rect_width = width
        self.rect_height = height
    def set_coord(self,screen, x, y):
        pygame.draw.rect(screen, self.rect_color, (self.rect_x, self.rect_y, self.rect_width, self.rect_height))
