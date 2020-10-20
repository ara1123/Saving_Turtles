#!/usr/bin/python3

#This is the basic game file. When done, this will be packed into a function
#that returns the end of game statistics, which will then be plotted and displayed to the user.

import pygame, sys
import random
import numpy as np
from PIL import Image
from ypstruct import structure

# Other files
import game_utils as gu

class game:
  """ DEFINE TILES """
  tilesize = 40
  W = 0 #WATER
  G = 1 #GRASS
  R = 2 #ROAD
  F = 3 #FOREST
  M = 4 #MUD
  X = 5 #CLIFF/FENCE - IMPASSABLE AREA

  """DEFINE TILE COLORS/TEXTURES"""
  img_path = "assets/"
  WATER = gu.image_to_tile(img_path + "water.png", tilesize)
  GRASS = gu.image_to_tile(img_path + "grass.png", tilesize)
  ROAD = gu.image_to_tile(img_path + "road.png", tilesize)
  FOREST = gu.image_to_tile(img_path + "forest.png", tilesize)
  MUD = gu.image_to_tile(img_path + "mud.png", tilesize)
  IMPASSE = gu.image_to_tile(img_path + "cliff.png", tilesize)

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
  width = len(map1[0])
  height = len(map1)
  start = (50, (height*tilesize) // 2)
  end = (width, (height*tilesize) // 2)
  iteration = 0 # Used for keeping turtle positions consistent
  game_active = True

  """ GAME OBJECTS """
  turtle_list = []
  clock = pygame.time.Clock()

  def init_game(self):
    pygame.init()
    self.screen = pygame.display.set_mode((self.width*self.tilesize,self.height*self.tilesize))

  def init_turtles(self, params):
    num_turtles = params.npop
    turtle_img = Image.open(self.img_path + "turtle.png")
    for n in range(num_turtles - 1):
      turtle_img = turtle_img.resize((self.tilesize // 2, self.tilesize // 2))
      turtle_surface = pygame.image.fromstring(turtle_img.tobytes(), turtle_img.size, turtle_img.mode)
      turtle_surface = pygame.transform.rotozoom(turtle_surface, -90, 1)
      turtle_rect = turtle_surface.get_rect(center = self.start)
      turtle = structure()
      turtle.surf = turtle_surface
      turtle.rect = turtle_rect
      turtle.path = gu.create_random_path(self)
      self.turtle_list.append(turtle)

  def set_turtle_list(self, turtles):
    self.turtle_list = turtles

  def run_game(self):
    def display_map():
      """ DRAW MAP TO SCREEN """
      for row in range(self.height):
        for col in range(self.width):
          self.screen.blit(self.TileTexture[self.map1[row][col]],(col*self.tilesize,row*self.tilesize,self.tilesize,self.tilesize))

    """ MAIN LOOP """
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      display_map()

      # Turtle movement
      # turtle_rect.centerx += 1
      # screen.blit(turtle_surface, turtle_rect)
      gu.move_turtles(self)

      pygame.display.update()
      self.clock.tick(120)
