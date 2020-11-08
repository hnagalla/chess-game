#DRIVER FILE
#HANDLES USER INPUT AND CHANGES GAME STATE INFO

import pygame as p

class Board:
    def __init__(self):
        #Chess board constants
        self.__BOARD_HEIGHT = 800
        self.__BOARD_WIDTH = 800
        self.__SQ_SIZE = self.__BOARD_HEIGHT / 8
        self.__BOARD_COLORS = (p.Color('white'),p.Color('gray'))    

    def draw_board(self):
        p.display.init()
        screen = p.display.set_mode((self.__BOARD_WIDTH,self.__BOARD_HEIGHT)) #Define window/chess board size
        
        #Draw chess board
        for row in range(self.__BOARD_HEIGHT):
            for col in range(self.__BOARD_WIDTH):
                #Black/White square
                color = self.__BOARD_COLORS[(row + col) % 2]
                #Draw the black or white square
                p.draw.rect(screen, color, p.Rect(col * self.__SQ_SIZE, row * self.__SQ_SIZE, self.__SQ_SIZE, self.__SQ_SIZE))

        p.display.set_caption('PvP Chess')
        #Display the board
        p.display.flip()
        
        #Keep window open unless user exits window
        running = True
        while running: 
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False

def main():
    #Initialize pygame
    p.init()

    #Create chess board object
    chess_board = Board()
    #Draw the board
    chess_board.draw_board()

    return 0

if __name__ == "__main__":
    main()
