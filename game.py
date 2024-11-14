from enum import Enum
import random
class GameState(Enum):
    STALEMATE = 0
    PLAYER_1_TURN = 1
    PLAYER_2_TURN = 2
    PLAYER_1_WINNER = 3
    PLAYER_2_WINNER = 4

class Connect4():
    def __init__(self, columns=7, rows=6):
        self.columns = columns
        self.rows = rows
        self.board = [["." for _ in range(columns)] for _ in range(rows)]
        self.state = GameState.PLAYER_1_TURN
        
    
    def makeMove(self, column):
        if not self.checkMove(column):
            return 0
        row = 0
        for i in range(self.rows):
            if self.board[i][column] != ".":
                row = i-1
                break
            elif i == self.rows-1:
                row = i
                break
        
        if self.state == GameState.PLAYER_1_TURN:
            self.board[row][column] = "1"
            self.state = GameState.PLAYER_2_TURN
        elif self.state == GameState.PLAYER_2_TURN:
            self.board[row][column] = "2"
            self.state = GameState.PLAYER_1_TURN
        self.checkBoard()
        return 1
        

    def checkMove(self, column):
        if column < 0 or column > self.columns - 1:
            return 0
        if not self.board[0][column] == ".":
            return 0
        return 1
    
    def checkBoard(self):
        directions = [
            [-1,0],
            [-1,1],
            [0,1],
            [1,1],
            [1,0],
            [1,-1],
            [0,-1]
        ]
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == ".":
                    pass
                for direction in directions:
                    if self.dfs(i,j,"1",direction,4):
                        self.state = GameState.PLAYER_1_WINNER
                        return True
                    if self.dfs(i,j,"2",direction,4):
                        self.state = GameState.PLAYER_2_WINNER
                        return True
        return False
    
    def dfs(self, r, c, token, direction, number):
        if r < 0 or c < 0 or r == self.rows or c == self.rows:
            return False
        
        if self.board[r][c] != token:
            return False
        
        number -= 1
        if number == 0:
            return True
        
        return self.dfs(r-direction[0], c-direction[1], token, direction, number)

    def getBoard(self):
        return self.board

    def getState(self):
        return self.state

    def printBoard(self):
        for i in range(self.rows):
            print(self.board[i])