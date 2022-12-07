import pygame
import sys
from sudoku_generator import *
from cell import *
from board import *
from constants import *


def reset_button(screen):
    # creating button font and text
    button_font = pygame.font.Font(None, 20)
    reset_text = button_font.render("RESET", 0, BG_COLOR)
    # creating button background color and placing the text
    reset_surface = pygame.Surface(((reset_text.get_size()[0] + 20),
                                    (reset_text.get_size()[1] + 20)))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    # creating the button's rectangle
    reset_rectangle = reset_text.get_rect(center=(WIDTH // 2 - 80, 560), width=70, height=30)
    # drawing button
    screen.blit(reset_surface, reset_rectangle)

    return reset_rectangle


def restart_button(screen):
    # creating button font and text
    button_font = pygame.font.Font(None, 20)
    restart_text = button_font.render("RESTART", 0, BG_COLOR)
    # creating button background color and placing the text
    restart_surface = pygame.Surface(((restart_text.get_size()[0] + 20),
                                      (restart_text.get_size()[1] + 20)))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    # creating the button's rectangle
    restart_rectangle = restart_text.get_rect(center=(WIDTH // 2,
                                                      560), width=70, height=30)
    # drawing button
    screen.blit(restart_surface, restart_rectangle)

    return restart_rectangle


def exit_button(screen):
    # creating button font and text
    button_font = pygame.font.Font(None, 20)
    exit_text = button_font.render("EXIT", 0, BG_COLOR)
    # creating button background color and placing the text
    exit_surface = pygame.Surface(((exit_text.get_size()[0] + 20),
                                   (exit_text.get_size()[1] + 20)))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    # creating the button's rectangle
    exit_rectangle = exit_text.get_rect(center=(WIDTH // 2 + 80, 560),width=70, height=30)
    # drawing button
    screen.blit(exit_surface, exit_rectangle)

    return exit_rectangle


def draw_buttons(screen): # draws reset, restart, and exit buttons
    r = reset_button(screen)
    re = restart_button(screen)
    ex = exit_button(screen)
    return r, re, ex


def start_screen(screen): # start menu that shows easy, medium, and hard modes
    screen.fill(BG_COLOR)

    start_font = pygame.font.Font(None, 70)
    game_mode_text_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 35)

    # initializing the title
    title_surface = start_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 4 - 25))
    screen.blit(title_surface, title_rectangle)
    game_mode_text = game_mode_text_font.render("Select Game Mode:", 0,
                                                LINE_COLOR)
    game_mode_rectangle = game_mode_text.get_rect(center=(WIDTH // 2,
                                                          HEIGHT // 2))
    screen.blit(game_mode_text, game_mode_rectangle)

    # creating the button's text

    easy_text = button_font.render("Easy", 0, BG_COLOR)
    medium_text = button_font.render("Medium", 0, BG_COLOR)
    hard_text = button_font.render("Hard", 0, BG_COLOR)

    # creating button background color and placing the text

    easy_surface = pygame.Surface(((easy_text.get_size()[0] + 20),
                                   (easy_text.get_size()[1] + 20)))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface(((medium_text.get_size()[0] + 20),
                                     (medium_text.get_size()[1] + 20)))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface(((hard_text.get_size()[0] + 20),
                                   (hard_text.get_size()[1] + 20)))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # creating the button's rectangle

    easy_rectangle = easy_text.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 100), width=150, height=200)
    medium_rectangle = medium_text.get_rect(center=(WIDTH // 2,
                                                    HEIGHT // 2 + 100), width=150, height=200)
    hard_rectangle = hard_text.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2 + 100), width=150, height=200)

    # drawing buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # user has to either exit out of the window or select one of the buttons
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 'easy'
                if medium_rectangle.collidepoint(event.pos):
                    return 'medium'
                if hard_rectangle.collidepoint(event.pos):
                    return 'hard'
        pygame.display.update()

def game_win_screen(screen): # if user wins display and then user exits
    screen.fill(BG_COLOR)

    # the fonts
    win_font = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 45)

    # creating the game over text and drawing it
    title_surface = win_font.render("You Won!", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 2 - 100))
    screen.blit(title_surface, title_rectangle)

    # creating the exit button and drawing it
    exit_text = button_font.render("Exit", 0, BG_COLOR)
    exit_surface = pygame.Surface(((exit_text.get_size()[0] + 20),
                                   (exit_text.get_size()[1] + 20)))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_text.get_rect(center=(WIDTH // 2,
                                                HEIGHT // 2 + 50), width=50, height=30)
    screen.blit(exit_surface, exit_rectangle)

    # user has to either close out the window or hit the restart button,
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


def game_over_screen(screen): # if user loses then display and user can restart
    screen.fill(BG_COLOR)

    # the fonts
    game_over_font = pygame.font.Font(None, 85)
    button_font = pygame.font.Font(None, 45)

    # creating the game over text and drawing it
    title_surface = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 2 - 100))
    screen.blit(title_surface, title_rectangle)

    # creating the exit button and drawing it 
    restart_text = button_font.render("Restart", 0, BG_COLOR)
    restart_surface = pygame.Surface(((restart_text.get_size()[0] + 20),
                                      (restart_text.get_size()[1] + 20)))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_text.get_rect(center=(WIDTH // 2,
                                                      HEIGHT // 2 + 50), width=150, height=200)
    screen.blit(restart_surface, restart_rectangle)

    # user has to either close out the window or hit the restart button
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return start_screen(screen)
        pygame.display.update()


if __name__ == '__main__':
    game_over = False

    pygame.init() # initiates pygame
    pygame.display.set_caption("Sudoku") # sets window to be named "Sudoku"
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # sets size of window

    result = start_screen(screen) # display start menu

    if result == 'easy': # if easy is clicked, create board with 30 removed cells
        removed_cells = 30
        board = Board(WIDTH, HEIGHT, screen, removed_cells)
        board.set_edit()
        board.draw()
    if result == 'medium': # if medium is clicked, create board with 40 removed cells
        removed_cells = 40
        board = Board(WIDTH, HEIGHT, screen, removed_cells)
        board.set_edit()
        board.draw()
    if result == 'hard': # if hard is clicked, create board with 50 removed cells
        removed_cells = 50
        board = Board(WIDTH, HEIGHT, screen, removed_cells)
        board.set_edit()
        board.draw()

    while True:
        ev = pygame.event.get()
        reset, restart, exit = draw_buttons(screen) # have buttons always on screen while game is running
        for event in ev:
            if event.type == pygame.QUIT:
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset.collidepoint(event.pos):
                    # reset board
                    board.reset_to_original()
                if restart.collidepoint(event.pos):
                    # back to main menu
                    result = start_screen(screen)
                    if result == 'easy': # creates new easy board
                        removed_cells = 30
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()
                    if result == 'medium': # creates new medium board
                        removed_cells = 40
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()
                    if result == 'hard': # creates new hard board
                        removed_cells = 50
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()
                if exit.collidepoint(event.pos):
                    # exit program
                    sys.exit()
                x, y = event.pos # uses mouse coordinates to get row and col of board
                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                if row < 9 and col < 9:
                    board.select(row, col) # if box is clicked and able to be selected, select
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: # if 1 key is pressed, sketch 1
                    board.sketch(1)
                if event.key == pygame.K_2: # 2 key
                    board.sketch(2)
                if event.key == pygame.K_3: # 3 key
                    board.sketch(3)
                if event.key == pygame.K_4: # so on
                    board.sketch(4)
                if event.key == pygame.K_5:
                    board.sketch(5)
                if event.key == pygame.K_6:
                    board.sketch(6)
                if event.key == pygame.K_7:
                    board.sketch(7)
                if event.key == pygame.K_8:
                    board.sketch(8)
                if event.key == pygame.K_9:
                    board.sketch(9)
                if event.key == pygame.K_RETURN: # when enter is pressed if selected cell has a sketched value, display value
                    for row in board.cells:
                        for cell in row:
                            if cell.selected:
                                if cell.sketch_value != 0:
                                    value = cell.sketch_value
                                    board.place_number(value)
                if event.key == pygame.K_BACKSPACE: # remove value/sketched value of selected cell
                    for row in board.cells:
                        for cell in row:
                            if cell.selected:
                                board.clear()
            if board.is_full(): # check if board is full
                game_over = True

            if game_over == True:
                if board.check_board(): # if board is the solution, print game win screen
                    game_win_screen(screen)
                else: # if board is not the solution, print the game over screen
                    game_over = False
                    game_over_screen(screen)
                    result = start_screen(screen)
                    if result == 'easy': # new easy board
                        removed_cells = 30
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()
                    if result == 'medium': # new medium board
                        removed_cells = 40
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()
                    if result == 'hard': # new hard board
                        removed_cells = 50
                        board = Board(WIDTH, HEIGHT, screen, removed_cells)
                        board.set_edit()
                        board.draw()

        pygame.display.update() 