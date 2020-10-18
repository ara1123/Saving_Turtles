#!/usr/bin/python3
import pygame
import random

# Tells us which squares not to go to.
# def invalid_tile(game):
#   cliff_tag = game.cliff
#   invalid_tiles = []
#   for tile in game.map:
#     if tile == cliff.tag:
#       invalid_tiles.append(tile)
#   return invalid_tiles

# Which tile is this pixel in?
def which_tile(pos, game):
  x = pos[0]
  y = pos[1]
  print("POSITION: ", (x, y), "\n")
  x_ind = x // game.tilesize
  y_ind = game.height - (y // game.tilesize)
  return (x_ind, y_ind)

# def create_random_path(game):
#   lower_bound = game.height
#   high_bound = 0
#   right_bound = game.width
#   left_bound = 0
#   game_map = game.map
#   tile_wise_path = []
#   while True:






