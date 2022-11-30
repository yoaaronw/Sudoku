import math,random
import pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
        self.box_length = math.sqrt(row_length)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for index, list in enumerate(self.board):
            for int in list:
                print(int)
            if index != len(self.board) - 1:
                print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for index, list in enumerate(self.board):
            if index == row:
                for int in list:
                    if int == num:
                        return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        i = 0
        while i < len(self.board):
            for indexR in range(len(self.board)):
                if col == i and num == self.board[indexR][i]:
                    return False
            i += 1
        return True
          

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        if num == self.board[row_start][col_start]:
            return False
        if num == self.board[row_start+1][col_start]:
            return False
        if num == self.board[row_start+2][col_start]:
            return False
        if num == self.board[row_start][col_start+1]:
            return False
        if num == self.board[row_start][col_start+2]:
            return False
        if num == self.board[row_start+1][col_start +1]:
            return False
        if num == self.board[row_start +1][col_start + 2]:
            return False
        if num == self.board[row_start + 2][col_start + 1]:
            return False
        if num == self.board[row_start+2][col_start + 2]:
            return False
        else:
            return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_column(col, num) and self.valid_in_box(row // 3 * 3, col // 3 * 3, num) and self.board[row][col] == 0:
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        list = []
        for i in range(3):
            for j in range(3):
                not_available = True
                while not_available:
                    num = random.randint(1, 9)
                    if num not in list:
                        list.append(num)
                        self.board[i + row_start][j + col_start] = num
                        not_available = False

              
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        for i in range(self.removed_cell):
            not_available = True
            while not_available:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if self.board[row][col] != 0:
                    self.board[row][col] = 0
                    not_available = False
              
          
'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


WIDTH = 540
HEIGHT = 600 
LINE_WIDTH = 2
BOLD_LINE_WIDTH = 5
SQUARE_SIZE = 60
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (66, 66, 66)
SKETCH_COLOR = (155, 155, 155)
NUM_COLOR = (66, 66, 66)
NUMBER_FONT = 50
SKETCH_FONT = 38
GAME_OVER_FONT = 40

'''
WIN_LINE_WIDTH = 15
SPACE = 55
'''

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_value = 0
  
    def set_cell_value(self, value):
        self.value = value
  
    def set_sketched_value(self, value):
        self.sketch_value = value
  
    def draw(self):
        num_font = pygame.font.Font(None, NUMBER_FONT)
        num_surf = num_font.render(str(self.value), 0, NUM_COLOR)
        sketch_font = pygame.font.Font(None, SKETCH_FONT)
        sketch_surf = sketch_font.render(str(self.sketch_value), 0, SKETCH_COLOR)
        if self.value == 0:
            if self.sketch_value != 0:
                # display sketched value in top left corner of cell
                sketch_rect = sketch_surf.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 4, SQUARE_SIZE * self.row + SQUARE_SIZE // 3))
                self.screen.blit(sketch_surf, sketch_rect)
        else:
            # display value
            num_rect = num_surf.get_rect(center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            self.screen.blit(num_surf, num_rect)
          
        # make outline of cell red when selected

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen 
        self.difficulty = difficulty
  
    def draw(self):
        # draw horizontal lines
        for i in range(10):
            if (i + 1) % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (self.width, i * SQUARE_SIZE), BOLD_LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (0, i * SQUARE_SIZE), (self.width, i * SQUARE_SIZE), LINE_WIDTH)
        # draw vertical lines
        for i in range(10):
            if (i + 1) % 3 == 0:
                pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, self.height), BOLD_LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, self.height), LINE_WIDTH)

        # draw cells
        # draw buttons maybe? or maybe draw buttons in main
              
    def select(self, row, col):
      pass
  
    def click(self, x, y):
      pass
  
    def clear(self):
      pass
  
    def sketch(self, value):
      pass
  
    def place_number(self, value):
      pass
  
    def reset_to_original(self):
      pass
  
    def is_full(self):
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == 0:
                    return False
        return True
  
    def update_board(self):
      pass
  
    def find_empty(self):
      pass
  
    def check_board(self):
      pass

def start_screen(screen):
     pass
  
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # draw game start screen
    start_screen(screen)
  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    