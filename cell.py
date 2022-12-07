import pygame
from constants import *

class Cell:
# this is the contructor for the class
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.sketch_value = 0
    self.selected = False
    self.can_edit = True

  def set_cell_value(self, value): # Setter for this cell’s value 
    self.value = value

  def set_sketched_value(self, value): # Setter for this cell’s sketched value
    self.sketch_value = value

  def draw(self): # Draws this cell, along with the value inside it
    num_font = pygame.font.Font(None, NUMBER_FONT)
    num_surf = num_font.render(str(self.value), 0, NUM_COLOR)
    sketch_font = pygame.font.Font(None, SKETCH_FONT)
    sketch_surf = sketch_font.render(str(self.sketch_value), 0, SKETCH_COLOR)
    # make outline of cell red when selected
    if self.selected:
      pygame.draw.rect(self.screen, RED, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

    if self.value == 0:
      if self.sketch_value != 0:
        # display sketched value in top left corner of cell
        sketch_rect = sketch_surf.get_rect(
          center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 4,
                  SQUARE_SIZE * self.row + SQUARE_SIZE // 3))
        self.screen.blit(sketch_surf, sketch_rect)
    else:
      # display value
      num_rect = num_surf.get_rect(
        center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      self.screen.blit(num_surf, num_rect)