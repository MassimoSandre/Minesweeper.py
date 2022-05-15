import pygame
import random

class Minesweeper:
    def __init__(self, pos,cell_size,margin, font, rows=9, cols=9, bombs=10):
        self.__pos = pos
        self.__font = font
        self.__cell_size = cell_size
        self.__margin = margin
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
        self.__gameover = False

        self.__board = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__revealed = [[False for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__flagged = [[False for _ in range(self.__cols)] for _ in range(self.__rows)]
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
        
    def flag(self, cell):
        i,j = cell
        if self.__revealed[i][j]:
            return
        
        self.__flagged[i][j] = not self.__flagged[i][j]

    def reveal(self, cell):
        i,j = cell
        if self.__revealed[i][j] or self.__flagged[i][j]:
            return

        self.__revealed[i][j] = True

        if self.__board[i][j] == -1:
            self.__gameover = True
        elif self.__board[i][j] == 0:
            for k in range(max(0,i-1), min(self.__rows,i+2)):
                for l in range(max(0,j-1), min(self.__cols,j+2)):
                    if (k,l) != (i,j):
                        self.reveal((k,l))

    def get_cell_by_pos(self, pos):
        rx,ry = pos
        rx-=self.__pos[0]
        ry-=self.__pos[1]

        i,j = ry//(self.__cell_size+self.__margin), rx//(self.__cell_size+self.__margin)
        fx,fy = j*(self.__cell_size+self.__margin)+self.__cell_size,i*(self.__cell_size+self.__margin)+self.__cell_size

        if rx >= fx or ry >= fy:
            return None
        if i < 0 or j < 0 or i >= self.__rows or j >= self.__cols:
            return None
        return (i,j)

    def check_gameover(self):
        return self.__gameover

    def show(self, screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.__pos, (self.__cols*self.__cell_size + (self.__cols+1)*self.__margin, self.__rows*self.__cell_size + (self.__rows+1)*self.__margin)), 0, 5)

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__revealed[i][j]:
                    cx,cy = (self.__pos[0]+j*self.__cell_size+(j+1)*self.__margin,self.__pos[1]+i*self.__cell_size+(i+1)*self.__margin)
                    pygame.draw.rect(screen, (100,100,100), pygame.Rect((cx,cy), (self.__cell_size,self.__cell_size)), 0, 3)

                    if self.__board[i][j] != 0:
                        text_surface = self.__font.render(str(self.__board[i][j]), False, (230,0,0))

                        r = text_surface.get_rect()

                        dx = (r.width)//2
                        dy = (r.height)//2
                        screen.blit(text_surface, (cx+self.__cell_size//2-dx, cy+self.__cell_size//2-dy))
                elif self.__flagged[i][j]:
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect((self.__pos[0]+j*self.__cell_size+(j+1)*self.__margin,self.__pos[1]+i*self.__cell_size+(i+1)*self.__margin), (self.__cell_size,self.__cell_size)), 0, 3)
                    pygame.draw.circle(screen, (255,0,0), (self.__pos[0]+j*self.__cell_size+(j+1)*self.__margin + self.__cell_size//2,self.__pos[1]+i*self.__cell_size+(i+1)*self.__margin + self.__cell_size//2), self.__cell_size//2)
                else:
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect((self.__pos[0]+j*self.__cell_size+(j+1)*self.__margin,self.__pos[1]+i*self.__cell_size+(i+1)*self.__margin), (self.__cell_size,self.__cell_size)), 0, 3)




