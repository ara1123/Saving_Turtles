#!/usr/bin/python3

import pygame, sys
import random
import numpy as np

""" DEFINE TILES """
W = 0 #WATER
G = 1 #GRASS
R = 2 #ROAD
F = 3 #FOREST
M = 4 #MUD
X = 5 #CLIFF/FENCE - IMPASSABLE AREA

"""DEFINE TILE COLORS/TEXTURES"""
WATER = (0,0,255)
GRASS = (124,252,0)
ROAD = (121,121,121)
FOREST = (0,100,0)
MUD = (102,51,0)
IMPASSE = (0,0,0)

"""LINK TILES AND TEXTURES/COLORS"""
TileTexture = {W : WATER,
              G : GRASS,
              R : ROAD,
              F : FOREST,
              M : MUD,
              X : IMPASSE}

"""DEFINE MAP"""
map1 = np.array([[G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W],
                [G, G, G, G, G, G, G, G, R, G, G, G, G, G, G, G, W]])

TILESIZE = 40
MAPWIDTH = len(map1[1])
MAPHEIGHT = len(map1)

""" GAME VARIABLES """
# None yet

""" INIT GAME """
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
CLOCK = pygame.time.Clock()

""" FUNCTION DEFS """
def display_map():
  """ DRAW MAP TO DISPLAY """
  for row in range(MAPHEIGHT):
    for col in range(MAPWIDTH):
      pygame.draw.rect(DISPLAY,TileTexture[map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  display_map()
  pygame.display.update()


