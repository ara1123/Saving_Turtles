#!/usr/bin/python3
import pygame
import random
import numpy as np
from ypstruct import structure
from PIL import Image



# Which tile is this pixel in?
def which_tile(pos, game):
  x = pos[0]
  y = pos[1]
  x_ind = x // game.tilesize
  y_ind = game.height - (y // game.tilesize)
  return (x_ind, y_ind)

# Generates a random path through the game.
def create_random_path(game):
  tile_size = game.tilesize
  lower_bound = 0 # Remember this is the top of the screen in pygame
  high_bound = game.height * tile_size # And this is the bottom
  left_bound = 0
  right_bound = game.width * tile_size
  game_map = game.map
  start = game.start
  end = game.end
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
                        [x + 1,y],
                        [x + 1,y],
                        [x + 1,y],
                        [x,y + 1],
                        [x,y - 1],
                        [x + 1,y + 1],
                        [x + 1,y - 1]])

    # Make sure to not travel back to previous tile
    choices = remove_tile(prev_tile, choices)

    # Randomly choose the next tile
    next_ind = random.randrange(len(choices))
    prev_tile = current_tile
    tile_wise_path.append(prev_tile)
    if is_end_path(prev_tile):
      break
    print(choices[next_ind])
    current_tile = (choices[next_ind][0],choices[next_ind][1])

  return tile_wise_path
