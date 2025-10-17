"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 4
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        # Draw the grid
        
        for row in range(self.GRID_SIZE):
            for column in range(self.GRID_SIZE):
                x = column * (self.WIDTH + self.MARGIN) + self.MARGIN
                y = row * (self.HEIGHT + self.MARGIN) + self.MARGIN + 40
                rectangle = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
                pygame.draw.rect(self.screen, self.WHITE, rectangle, width = 3 )
        
        
        # Draw pieces on the board
        for row in range(self.GRID_SIZE):
            for column in range(self.GRID_SIZE):
                x = column * (self.WIDTH + self.MARGIN) + self.MARGIN
                y = row * (self.HEIGHT + self.MARGIN) + self.MARGIN + 40
                if self.game_state.board_state[row][column] == 1:
                    self.draw_cross(x, y)
                elif self.game_state.board_state[row][column] == -1:
                    self.draw_circle(x, y)
        
        pygame.display.update()

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
       
       circleX = x + self.WIDTH // 2
       circleY = y + self.HEIGHT // 2
       
       radius = int(min(self.WIDTH, self.HEIGHT) * .35)
       pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (circleX, circleY), radius, width=3)
        

    def draw_cross(self, x, y):
        pad = int(min(self.WIDTH, self.HEIGHT) * .2)
        x1, y1 = x + pad, y + pad
        x2, y2 = x + self.WIDTH - pad, y + self.HEIGHT - pad
        x3 = x + pad
        y3 = y + self.HEIGHT - pad
        x4 = x + self.WIDTH - pad
        y4 = y + pad
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x1, y1), (x2, y2), width=3)
        pygame.draw.line(self.screen, self.CROSS_COLOR, (x3, y3), (x4, y4), width=3)
        

    def is_game_over(self):

        return self.game_state.is_terminal()
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self): 
        if self.algorithm == "minimax":
            score, best_move = minimax(self.game_state, depth=4, maximizingPlayer=self.game_state.turn_O) # if turn_O is True, then maximizing player
        else:
            tm = 1 if self.game_state.turn_O else -1 # turn multiplier for sign to match player turn
            score, best_move = negamax(self.game_state, depth=4, turn_multiplier=tm)
        
        if best_move is not None: # in case there are no possible moves
            self.game_state = self.game_state.get_new_state(best_move)
        
        self.draw_game() # redraw the game after AI move 
        
        self.change_turn() # change turn display
        pygame.display.update()
        
        terminal = self.game_state.is_terminal() # cgeck if game is over
        if terminal:
            
            final_score = self.game_state.get_scores(terminal = True)
            
            print(f"Winner: {self.game_state.winner} with score {final_score}")



    def game_reset(self):
        
        new_board = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int) # create empty board
        
        self.game_state = GameStatus(new_board, turn_O=True) # O starts first
        
        self.draw_game() # draw the empty board
        
        self.change_turn() # set turn display
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()
        
        self.draw_game()
        pygame.display.update()


        while not done:
            for event in pygame.event.get():  # User did something
               
               if event.type == pygame.QUIT:  # If user clicked close
                   done = True  # Flag that we are done so we exit this loop
                   break
               
               if event.type == pygame.KEYDOWN: # key press event
                     if event.key == pygame.K_ESCAPE: # exit the game if 'Esc' is pressed
                            done = True
                            break
                     if event.key == pygame.K_r: # reset the game if 'r' is pressed
                          self.game_reset()
                          continue
                        
               
               if self.game_state.is_terminal():
                   final_score = self.game_state.get_scores(terminal = True)
                   print(f"Game Over! Winner: {self.game_state.winner} with score {final_score}")
                   pygame.display.update()
                   continue
               
               
               
               if event.type == pygame.MOUSEBUTTONUP: # mouse click event
                   mousex, mousey = event.pos
                   cell_w = self.WIDTH + self.MARGIN
                   cell_h = self.HEIGHT + self.MARGIN
                   cell = (mousex // cell_w)
                   row = (mousey // cell_h)  # adjust for top margin
                   
                   
                   if 0 <= row < self.GRID_SIZE and 0 <= cell < self.GRID_SIZE: # check for valid click inside the grid
                       
                       if self.game_state.board_state[row, cell] == 0: # only allow move if cell is empty
                           # player move
                           self.game_state = self.game_state.get_new_state((row, cell))
                           self.draw_game()
                           self.change_turn()
                           pygame.display.update()
                           
                           # ai move
                           if mode == "player_vs_ai" and not self.game_state.is_terminal():
                               self.play_ai()
                       
                   
                
                   
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()
def menu(game):
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Tic Tac Toe Menu")
    font = pygame.font.Font(None, 36)
    
    selected_algorithm = "minimax"
    mode = "player_vs_ai"
    
    minimax_button = pygame.Rect(50, 50, 300, 50)
    negamax_button = pygame.Rect(50, 120, 300, 50)
    start_button = pygame.Rect(50, 200, 300, 50)
    
    running = True
    while running:
        screen.fill((50, 50, 50))
        
        title = font.render("Select Algorithm", True, (255, 255, 255))
        screen.blit(title, (100, 10))
        
        #buttons
        pygame.draw.rect(screen, (100, 100, 200) if selected_algorithm == "minimax" else(100, 100, 100),  minimax_button)
        pygame.draw.rect(screen, (100, 100, 200) if selected_algorithm == "negamax" else(100,100,100), negamax_button)
        pygame.draw.rect(screen, (100, 200, 100), start_button)
        
        screen.blit(font.render("Minimax", True, (255, 255, 255)), (minimax_button.x + 100, minimax_button.y + 10))
        screen.blit(font.render("Negamax", True, (255, 255, 255)), (negamax_button.x + 100, negamax_button.y + 10))
        screen.blit(font.render("Start Game", True, (255, 255, 255)), (start_button.x + 80, start_button.y + 10))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if minimax_button.collidepoint(event.pos):
                    algorithms = "minimax"
                elif negamax_button.collidepoint(event.pos):
                    algorithms = "negamax"
                elif start_button.collidepoint(event.pos):
                    game.algorithm = selected_algorithm
                    game.grid_size = 4
                    board = np.zeros((game.grid_size, game.grid_size), dtype=int)
                    game.game_state = GameStatus(board, turn_O=True)
                    game.draw_game()
                    pygame.display.update()
                    game.play_game(mode)
                    running = False
                
menu(tictactoegame)
