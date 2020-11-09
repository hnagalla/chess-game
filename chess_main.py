#DRIVER FILE
#HANDLES USER INPUT AND CHANGES GAME STATE INFO

import pygame as p
import chess_engine as chess_eng

class Board:
    def __init__(self):
        #Chess board constants
        self.__DIMENSION = 8
        self.__BOARD_HEIGHT = 800
        self.__BOARD_WIDTH = 800
        self.__SQ_SIZE = int(self.__BOARD_HEIGHT / 8)
        self.__BOARD_COLORS = (p.Color('white'),p.Color('gray')) 
        self.__PIECES = ['wR','wN','wB','wQ','wK','wp','bR','bN','bB','bQ','bK','bp']
        #Dictionary of images. {'piece': image}
        self.__IMAGES = {}
        self.screen = 0

    @property
    def IMAGES(self):
        return self.__IMAGES

    def load_images(self):
        for piece in self.__PIECES:
            self.__IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"),(self.__SQ_SIZE,self.__SQ_SIZE))
            
    def draw_game_state(self,gs):
        self.draw_board()
        self.draw_pieces(gs)
  
    def draw_board(self):
        p.display.init()
        self.screen = p.display.set_mode((self.__BOARD_WIDTH,self.__BOARD_HEIGHT)) #Define window/chess board size
        
        #Draw chess board
        for row in range(self.__DIMENSION):
            for col in range(self.__DIMENSION):
                #Black/White square
                color = self.__BOARD_COLORS[(row + col) % 2]
                #Draw the black or white square
                p.draw.rect(self.screen, color, p.Rect(col * self.__SQ_SIZE, row * self.__SQ_SIZE, self.__SQ_SIZE, self.__SQ_SIZE))

        p.display.set_caption('PvP Chess')
        
    #Draw pieces on board, depending on the current game state
    def draw_pieces(self, GameState):
        for row in range(self.__DIMENSION):
            for col in range(self.__DIMENSION):
                #Get the piece at this position of the board
                piece = GameState.board_state[row][col]
                #Check if piece is an empty square
                if piece != "--":
                    #self.screen.blit(self.__IMAGES[piece], p.Rect(col * self.__SQ_SIZE, row * self.__SQ_SIZE, self.__SQ_SIZE, self.__SQ_SIZE))
                    self.screen.blit(self.__IMAGES[piece], p.Rect(col * self.__SQ_SIZE, row * self.__SQ_SIZE, self.__SQ_SIZE, self.__SQ_SIZE))


#Main driver 
def main():
    MAX_FPS = 15
    #Initialize pygame
    p.init()
    clock = p.time.Clock()

    #Create chess board object
    chess_board = Board()
    #Create initial game state object
    game_state = chess_eng.GameState()
    #Load chess piece image files
    chess_board.load_images()

    #Keep window open unless user exits window
    running = True
    while running: 
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        #Draw the board with the current game state (pieces)
        chess_board.draw_game_state(game_state)
        clock.tick(MAX_FPS)
        #Display the board
        p.display.flip()

    return 0

if __name__ == "__main__":
    main()
