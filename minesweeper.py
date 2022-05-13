import pygame
import random

class Minesweeper:
    def __init__(self, pos, font, rows=9, cols=9, bombs=10):
        self.__pos = pos
        self.__font = font
        self.game_settings(rows=rows,cols=cols,bombs=bombs)

    def game_settings(self,*, rows=None, cols=None, bombs=None):
        if rows == None:
            rows = self.__rows
        if cols == None:
            cols = self.__cols
        if bombs == None:
            bombs = self.__bombs

        if bombs > rows*cols:
            raise "there aren't enough cells for the specified amount of bombs"

        self.__rows = rows
        self.__cols = cols
        self.__bombs = bombs

        self.new_game()

    def new_game(self):
        self.__board = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__revealed = []
        for _ in range(self.__bombs):
            j = random.randrange(0,self.__cols)
            i = random.randrange(0,self.__rows)
            while self.__board[i][j] == -1:
                j = random.randrange(0,self.__cols)
                i = random.randrange(0,self.__rows)
            self.__board[i][j] = -1

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__board[i][j] != -1:
                    b = 0
                    for k in range(max(0,i-1), min(self.__rows,i+2)):
                        for l in range(max(0,j-1), min(self.__cols,j+2)):
                            if self.__board[k][l] == -1:
                                b+=1
                    self.__board[i][j] = b

        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__board[i][j], end=' ')
            print()
        
    def reveal(self, cell):
        i,j = cell
        if self.__revealed[i][j]:
            return

        self.__revealed[i][j] = True

        if self.__board[i][j] == 0:
            for k in range(max(0,i-1), min(self.__rows,i+2)):
                for l in range(max(0,j-1), min(self.__cols,j+2)):
                    if self.__board[k][l] == 0 and (k,l) != (i,j):
                        self.reveal((k,l))
            




