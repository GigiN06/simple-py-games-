import pygame
import sys
import random
import itertools 

#Settings
win_width=800
win_height=500
FPS=60
title="Game"


# Initialize Pygame
pygame.init()


def displaytext(screen,text,size,color,pos,alph):
    font=pygame.font.Font('fonts/Game-Font.ttf',size)
    text_surface=font.render(text,True,color)
    text_surface.set_alpha(alph)
    text_rect=text_surface.get_rect()
    text_rect.x=pos[0]
    text_rect.y=pos[1]
    screen.blit(text_surface,text_rect)

def safetycheck(r,c,mat,n):
    if n in mat[r]:
        return False
    for i in range(9):
        if mat[i][c]==n:
            return False
    row,col=3*(r//3),3*(c//3)
    for i in range(row,row+3):
        for j in range(col,col+3):
            if mat[i][j]==n:
                return False
    return True

def board(mat):
    for row in range(9):
        for col in range(9):
            if mat[row][col]==0:
                numb=list(range(1,10))
                random.shuffle(numb)
                for n in numb:
                    if safetycheck(row,col,mat,n):
                        mat[row][col]=n
                        if board(mat):
                            return True
                        mat[row][col]=0
                return False
    return True
                        
def genmat():
    mat=[[0 for _ in range(9)] for _ in range(9)]
    if board(mat):
        return mat
    return None

def wait(start,dur):
    time=pygame.time.get_ticks()
    #print(time-start)
    return time-start>=dur