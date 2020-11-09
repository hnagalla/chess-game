#STORES ALL INFO ABOUT CURRENT STATE OF CHESS GAME
#DETERMINES VALID MOVES FOR CURRENT STATE
#STORES A MOVE LOG

class GameState():
    def __init__(self):
        #2-D List (list of list of pieces on board currently)
        self.__board_state = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR'],
        ]
        self.whiteToMove = True
        self.moveLog = []

    @property
    def board_state(self):
        return self.__board_state


    
