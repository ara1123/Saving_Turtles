#!/usr/bin/python3

#This is the basic game file. When done, this will be packed into a function
#that returns the end of game statistics, which will then be plotted and displayed to the user.

import pygame, sys
import random
import numpy as np
from PIL import Image
from ypstruct import structure

# Other files
import utils

""" DEFINE TILES """
TILESIZE = 40
W = 0 #WATER
G = 1 #GRASS
R = 2 #ROAD
F = 3 #FOREST
M = 4 #MUD
X = 5 #CLIFF/FENCE - IMPASSABLE AREA

"""DEFINE TILE COLORS/TEXTURES"""
img_path = "assets/"
WATER = utils.image_to_tile(img_path + "water.png", TILESIZE)
GRASS = utils.image_to_tile(img_path + "grass.png", TILESIZE)
ROAD = utils.image_to_tile(img_path + "road.png", TILESIZE)
FOREST = utils.image_to_tile(img_path + "forest.png", TILESIZE)
MUD = utils.image_to_tile(img_path + "mud.png", TILESIZE)
IMPASSE = utils.image_to_tile(img_path + "cliff.png", TILESIZE)

"""LINK TILES AND TEXTURES/COLORS"""
TileTexture = {W : WATER,
              G : GRASS,
              R : ROAD,
              F : FOREST,
              M : MUD,
              X : IMPASSE}

"""DEFINE MAP"""
map1 = np.array([[G, G, G, G, G, G, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, G, G, G, G, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, G, G, G, G, G, G, R, R, G, G, X, G, G, G, W],
                 [G, G, G, M, M, G, G, G, R, R, G, G, X, G, G, G, W],
                 [G, G, G, M, M, G, G, G, R, R, G, G, X, G, G, G, W],
                 [G, G, G, M, M, G, G, G, R, R, G, G, X, G, G, G, W],
                 [G, G, G, G, G, X, G, G, R, R, G, G, X, G, G, G, W],
                 [G, G, G, G, G, X, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, M, M, G, G, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, M, M, G, G, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, G, G, G, G, G, G, R, R, G, G, G, G, G, G, W],
                 [G, G, G, G, G, G, G, G, R, R, G, G, G, G, G, G, W]])

""" GAME VARIABLES """
MAPWIDTH = len(map1[0])
MAPHEIGHT = len(map1)
starting_pos = (50, (MAPHEIGHT*TILESIZE) // 2)
ending_pos = (MAPWIDTH, (MAPHEIGHT*TILESIZE) // 2)


game = structure()
game.tilesize = TILESIZE
game.width = MAPWIDTH
game.height = MAPHEIGHT
game.start = starting_pos
game.end = ending_pos
game.map = map1
game.cliff = X

""" INIT GAME """
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
clock = pygame.time.Clock()

print("PATH CHOICE: ", utils.create_random_path(game))

""" GAME OBJECTS """
# TURTLES
turtle_img = Image.open(img_path + "turtle.png")
turtle_img = turtle_img.resize((TILESIZE // 2, TILESIZE // 2))
turtle_surface = pygame.image.fromstring(turtle_img.tobytes(), turtle_img.size, turtle_img.mode)
turtle_surface = pygame.transform.rotozoom(turtle_surface, -90, 1)
turtle_rect = turtle_surface.get_rect(center = starting_pos)

""" FUNCTION DEFS """
def display_map():
  """ DRAW MAP TO SCREEN """
  for row in range(MAPHEIGHT):
    for col in range(MAPWIDTH):
      screen.blit(TileTexture[map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

def turtle_safe(trect):
  return trect.centerx >= MAPWIDTH

""" MAIN LOOP """
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  display_map()

  # Turtle movement
  turtle_rect.centerx += 1
  screen.blit(turtle_surface, turtle_rect)

  pygame.display.update()
  clock.tick(120)


