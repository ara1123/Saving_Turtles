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
  tilesize = 60
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

  """ DEFINE TILE SPEEDS """
  # Will multiply the movement by these numbers
  TileSpeed = {W : 4,
               G : 3,
               R : 3,
               F : 1,
               M : 2,
               X : 0}

  """ GAME VARIABLES """
  width = len(map1[0])
  height = len(map1)
  start = (50, (height*tilesize) // 2)
  end = (width*tilesize, (height*tilesize) // 2)
  game_active = True

  """ GAME OBJECTS """
  turtle_list = []
  clock = pygame.time.Clock()

  """ HELPER FUNCTIONS """

  def get_tile_speed(self, turtle):
    pos = (turtle.rect.centerx, turtle.rect.centery)
    x, y = self.which_tile(pos)
    tile_type = self.map1[x][y]
    print("TILE_TYPE ", tile_type)
    return self.TileSpeed[tile_type]

  def create_random_path(self):
    tile_size = self.tilesize
    lower_bound = 0 - 1# Remember this is the top of the screen in pygame
    high_bound = self.height + 1# And this is the bottom
    left_bound = 0 - 1
    right_bound = self.width + 1
    game_map = self.map1
    start = self.which_tile(self.start)
    end = self.which_tile(self.end)
    tile_wise_path = []

    def is_end_path(pos):
      return pos[0] < left_bound or pos[0] > right_bound \
             or pos[1] < lower_bound or pos[1] > high_bound \
             or pos == end

    def remove_tile(tile, choices):
      for i in range(len(choices)):
        if tile[0] == choices[i][0] and tile[1] == choices[i][1]:
          return np.delete(choices, i, 0)
      return choices

    # Create a tile-by-tile path
    current_tile = start
    prev_tile = current_tile
    while True:
      x, y = current_tile
      choices = np.array([[x + 1,y],
                          [x - 1,y],
                          [x,y + 1],
                          [x,y - 1],
                          [x + 1,y + 1],
                          [x + 1,y - 1],
                          [x - 1, y + 1],
                          [x - 1, y - 1]])

      # Make sure to not travel back to previous tile
      choices = remove_tile(prev_tile, choices)

      # Randomly choose the next tile
      next_ind = random.randrange(len(choices))
      prev_tile = current_tile
      tile_wise_path.append(prev_tile)
      if is_end_path(prev_tile):
        break
      current_tile = (choices[next_ind][0],choices[next_ind][1])

    print("\nCHOSE THIS PATH: ", tile_wise_path)
    return tile_wise_path

  def which_tile(self, pos):
    x = pos[0]
    y = pos[1]
    x_ind = x // self.tilesize
    y_ind = self.height - (y // self.tilesize)
    return (x_ind, y_ind)

  def move_turtles(self):
    for turtle in self.turtle_list:
      path_ind = turtle.iteration
      tilesize = self.tilesize
      posx = turtle.rect.centerx # Pixel
      posy = turtle.rect.centery
      current_tile = self.which_tile((posx,posy))
      if path_ind >= len(turtle.path) - 1:
        self.screen.blit(turtle.surf, turtle.rect)
        continue
      if turtle.path[path_ind] == current_tile:
        path_ind += 1
        turtle.iteration = path_ind

      # print("\nGoing to ", turtle.path[path_ind])
      diffx = turtle.path[path_ind][0] - current_tile[0]
      diffy = turtle.path[path_ind][1] - current_tile[1]
      movex = 1
      movey = 1
      if not diffy:
        movey = 0
      if diffy > 0:
        movey *= -1
      if not diffx:
        movex = 0
      elif diffx < 0:
        movex *= -1
      speed = self.get_tile_speed(turtle)
      turtle.rect.centerx += speed * movex
      turtle.rect.centery += speed * movey
      # print("\nMoved to ", which_tile((turtle.rect.centerx,turtle.rect.centery),game))
      self.screen.blit(turtle.surf, turtle.rect)

  """MAIN GAME FUNCTIONS"""
  def init_game(self):
    pygame.init()
    self.screen = pygame.display.set_mode((self.width*self.tilesize,self.height*self.tilesize))

  def init_turtles(self, params):
    num_turtles = params.npop
    turtle_img = Image.open(self.img_path + "turtle.png")
    for n in range(num_turtles):
      turtle_img = turtle_img.resize((self.tilesize // 2, self.tilesize // 2))
      turtle_surface = pygame.image.fromstring(turtle_img.tobytes(), turtle_img.size, turtle_img.mode)
      turtle_surface = pygame.transform.rotozoom(turtle_surface, -90, 1)
      turtle_rect = turtle_surface.get_rect(center = self.start)
      turtle = structure()
      turtle.surf = turtle_surface
      turtle.rect = turtle_rect
      turtle.path = self.create_random_path()
      turtle.iteration = 0
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
      self.move_turtles()
      pygame.display.update()
      self.clock.tick(60)
