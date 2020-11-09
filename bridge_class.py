#!/usr/bin/python3
import pygame
import random
from PIL import Image


class bridge:
    def __init__(self, bridge_params):
      left_pos = bridge_params.left
      map_top = bridge_params.top # These are in tiles, not pixels
      map_bot = bridge_params.bot
      tilesize = bridge_params.tilesize
      x = left_pos * tilesize
      y = random(map_top, map_bot - 1) * tilesize
      img_path = bridge_params.img_path
      self.surf = self.load_pic(self.img_path, self.tilesize)
      self.rect = self.surface.get_rect(topleft = (x, y))

    def load_pic(self, img_path, tilesize):
      img = Image.open(path_to_image)
      img = img.resize((tilesize * 2, tilesize))
      surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
      surface.convert_alpha()
      return surface
