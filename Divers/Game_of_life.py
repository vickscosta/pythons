#Main
x = 800
y = 30

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(x,y)
import pygame
# pygame.init()
from pygame.locals import *
# from pygame.transform import *
# import math
# import pdb
import numpy as np
import random

running=True
clock = pygame.time.Clock()

ORANGE=(255,160,16)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

screen_size = (1024,768)
screen = pygame.display.set_mode(screen_size)
screen.fill(WHITE)

matrix_height=int(1024/8)
matrix_lenght=int(768/8)

nb_cells=matrix_height*matrix_height

matrix=np.zeros(shape=(matrix_height,matrix_lenght),dtype=int)

init_ratio=0.3

for idx in range(int(init_ratio*nb_cells)):
    matrix[random.randint(0,matrix_height-1)][random.randint(0,matrix_lenght-1)]=1

rect=pygame.Surface((8,8))
rect.set_colorkey(WHITE)
# rect.fill(ORANGE)

def matrix_draw(m_h,m_l,matrix,rect,color):
    for h in range(m_h):
        for l in range(m_l):
            if matrix[h][l]==1:
                rect_=rect.get_rect()
                rect_.center=(h*8+4,l*8+4)
                rect.fill(color)
                screen.blit(rect,rect_)
            elif matrix[h][l]==8:
                rect_=rect.get_rect()
                rect_.center=(h*8+4,l*8+4)
                rect.fill(BLACK)
                screen.blit(rect,rect_)
            elif matrix[h][l]==4:
                rect_=rect.get_rect()
                rect_.center=(h*8+4,l*8+4)
                rect.fill(GREEN)
                screen.blit(rect,rect_)

def count_n(m_h,m_l,matrix):
    n_matrix=np.zeros(shape=(m_h,m_l),dtype=int)
    for h in range(m_h):
        for l in range(m_l):
            #up
            if h-1>=0:
                if matrix[h-1][l]==1:
                    n_matrix[h][l]+=1
                if l-1>=0: 
                    if matrix[h-1][l-1]==1:
                        n_matrix[h][l]+=1
                if l+1<=m_l-1:
                    if matrix[h-1][l+1]==1:
                        n_matrix[h][l]+=1
            #down
            if h+1<=m_h-1:
                if matrix[h+1][l]==1:
                    n_matrix[h][l]+=1
                if l-1>=0: 
                    if matrix[h+1][l-1]==1:
                        n_matrix[h][l]+=1
                if l+1<=m_l-1:
                    if matrix[h+1][l+1]==1:
                        n_matrix[h][l]+=1

            #left
            if l-1>=0:
                if matrix[h][l-1]==1:
                    n_matrix[h][l]+=1
            #right
            if l+1<=m_l-1:    
                if matrix[h][l+1]==1:
                    n_matrix[h][l]+=1
    return n_matrix

def update_matrix(m_h,m_l,matrix,n_matrix):

    for h in range(m_h):
        for l in range(m_l):
            #live
            if matrix[h][l]==1:
                if n_matrix[h][l]==2 or n_matrix[h][l]==3:
                    matrix[h][l]=1
                else:
                    matrix[h][l]=0
            
            #zombie
            elif matrix[h][l]==8 or matrix[h][l]==4:
                try:
                    if matrix[h+1][l]==1:
                        matrix[h+1][l]=4
                except: 
                    pass
                try:
                    if matrix[h-1][l]==1:
                        matrix[h-1][l]=4
                except: 
                    pass
                try:
                    if matrix[h][l+1]==1:
                        matrix[h][l+1]=4
                except: 
                    pass
                try:
                    if matrix[h][l-1]==1:
                        matrix[h][l-1]=4
                except: 
                    pass
            #dead
            else:
                if n_matrix[h][l]==3: #3
                    matrix[h][l]=1
                else:
                    matrix[h][l]=0
    return matrix

def feed_system(matrix,size,val):

    alea_x=random.randint(0,108)
    alea_y=random.randint(0,80)

    for idx_x in range(size):
        for idx_y in range(size):
            matrix[alea_x+idx_x][alea_y+idx_y]=val

    return matrix


matrix_draw(matrix_height,matrix_lenght,matrix,rect,RED)

#main loop
while running:
   
    pygame.display.flip()
    
    clock.tick(12)
    screen.fill(WHITE)

    n_matrix=count_n(matrix_height,matrix_lenght,matrix)

    matrix=update_matrix(matrix_height,matrix_lenght,matrix,n_matrix)

    matrix_draw(matrix_height,matrix_lenght,matrix,rect,RED)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key==K_SPACE:
                matrix=feed_system(matrix,10,1)
            if event.key==K_k:
                matrix=feed_system(matrix,1,8)
            if event.key==K_n:
                matrix=np.zeros(shape=(matrix_height,matrix_lenght),dtype=int)
                for idx in range(int(init_ratio*nb_cells)):
                    matrix[random.randint(0,matrix_height-1)][random.randint(0,matrix_lenght-1)]=1
            if event.key == K_ESCAPE:
                running = False
