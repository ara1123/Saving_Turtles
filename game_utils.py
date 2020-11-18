#!/usr/bin/python3
import pygame
from PIL import Image


def image_to_tile(path_to_image, TILESIZE):
  img = Image.open(path_to_image)
  img = img.resize((TILESIZE, TILESIZE))
  return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

def load_tilesz(path_to_image, tilesize):
  img = Image.open(path_to_image)
  img = img.resize((tilesize, tilesize))
  surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
  surface.set_colorkey((0,0,0))
  surface.convert()
  return surface

def load_half_tilesz(path_to_image, tilesize):
  img = Image.open(path_to_image)
  img = img.resize((tilesize // 2, tilesize // 2))
  surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
  surface.set_colorkey((200,0,0))
  surface.convert()
  return surface

def coords_to_cardinal(path):
  last_coord = path[0]
  card = []
  for coord in path:
    if coord == last_coord:
      continue
    x, y = coord
    lx, ly = last_coord
    movey = y - ly
    movex = x - lx

    if movey > 0 and movex == 0:
      card.append('N')
    elif movey > 0 and movex > 0:
      card.append('NE')
    elif movey == 0 and movex > 0:
      card.append('E')
    elif movey < 0 and movex > 0:
      card.append('SE'):
    elif movey < 0 and movex == 0:
      card.append('S')
    elif movey < 0 and movex < 0:
      card.append('SW')
    elif movey == 0 and movex < 0:
      card.append('W')
    elif movey > 0 and movex < 0:
      card.append('NW')

  return card

def card_to_coords(start, card):
  path = [start]
  x = start[0]
  y = start[1]
  for move in card:
    if move == 'N':
      y += 1
    elif move == 'NE':
      y += 1
      x += 1
    elif move == 'E':
      x += 1
    elif move == 'SE':
      y -= 1
      x += 1
    elif move == 'S':
      y -= 1
    elif move == 'SW':
      y -= 1
      x -= 1
    elif move == 'W':
      x -= 1
    elif move == 'NW':
      y += 1
      x -= 1
    path.append((x,y))

  return path
