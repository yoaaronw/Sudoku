import copy
from sudoku_generator import *
from cell import *
from constants import *

class Board:
# this is the contructor for the class
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.original_board = generate_sudoku(9, difficulty)
    self.board = copy.deepcopy(self.original_board)
    self.cells = [[Cell(self.board[i][j], i, j, screen) for j in range(9)]
                  for i in range(9)]

  def draw(self):
    self.screen.fill(BG_COLOR)
    # draw horizontal lines
    for i in range(10):
      if i % 3 == 0:
        pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE),
                         (self.width, i * SQUARE_SIZE), BOLD_LINE_WIDTH)
      else:
        pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE),
                         (self.width, i * SQUARE_SIZE), LINE_WIDTH)
    # draw vertical lines
    for i in range(10):
      if i % 3 == 0:
        pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0),
                         (i * SQUARE_SIZE, self.height - SQUARE_SIZE),
                         BOLD_LINE_WIDTH)
      else:
        pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0),
                         (i * SQUARE_SIZE, self.height - SQUARE_SIZE),
                         LINE_WIDTH)

    # draw cells
    for i in range(9):
      for j in range(9):
        self.cells[i][j].draw()

  def select(self, row, col):
    if self.cells[row][col].can_edit:
      for i in range(9):  # set everything else selected = to false
        for j in range(9):
          self.cells[i][j].selected = False
      self.draw()
      self.cells[row][col].selected = True  # set the only one we want to true
      self.cells[row][col].draw()

  def clear(self):
    for row in self.cells:
      for cell in row:
        if cell.selected:
          cell.set_cell_value(0) # sets all values to 0, clearing the cell
          cell.set_sketched_value(0)
          self.draw()

  def sketch(self, value):
    for row in self.cells:
      for cell in row:
        if cell.selected:  # check if the cell is selected
          if cell.value == 0 and cell.sketch_value == 0:
            cell.set_sketched_value(value) # sketch value
            cell.draw()
            break

  def place_number(self, value):
    for i, row in enumerate(self.cells):
      for j, cell in enumerate(row):
        if cell.selected:  # check if the cell is selected
          cell.set_cell_value(value) # sets value, draws, updates board
          self.draw()
          self.board[i][j] = value
          break

  def reset_to_original(self): # this function resets all cells in the board to their original values
    self.board = copy.deepcopy(self.original_board)
    self.update_board()
    self.set_edit()
    self.draw()

  def is_full(self): # Returns a Boolean value indicating whether the board is full or not
    for i in range(9):
      for j in range(9):
        if self.board[i][j] == 0:
          return False
    return True

  def update_board(self): # Updates the underlying 2D board with the values in all cells
    self.cells = [[Cell(self.board[i][j], i, j, self.screen) for j in range(9)]
                  for i in range(9)]

  def check_row(self): # this function checks if a number if already in that row
    for row in self.board:
      nums = []
      for col in row:
        if col in nums:
          return False
        else:
          nums.append(col)
    return True

  def check_col(self): # this function checks if a number if already in that column
    for i in range(9):
      nums = []
      for row in self.board:
        for index, col in enumerate(row):
          if index == i:
            if col in nums:
              return False
            else:
              nums.append(col)
    return True

  def check_box(self): # this function checks if a number if already in that box
    for row_start in range(9):
      if row_start % 3 == 0:
        for col_start in range(9):
          if col_start % 3 == 0:
            nums = []
            for i in range(3):
              for j in range(3):
                if self.board[row_start + i][col_start + j] in nums:
                  return False
                else:
                  nums.append(self.board[row_start + i][col_start + j])
    return True

  def check_board(self): # Check whether the Sudoku board is solved correctly
    if self.check_row() and self.check_col() and self.check_box():
      return True
    else:
      return False

  def set_edit(self):
    for row in self.cells:
      for cell in row:
        if cell.value != 0:
          cell.can_edit = False 
          # when board is made it sets all generated cells to be False so they can't be edited
