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
      self.x = left_pos * tilesize
      self.y = random.randrange((map_bot + 2), map_top - 2, 1) * tilesize
      self.rect = None
      self.surf = None


    def load_pic(self, img_path, tilesize):
      img = Image.open(img_path)
      img = img.resize((tilesize * 2, tilesize))
      surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
      surface.convert_alpha()
      self.surf = surface
      self.rect = self.surf.get_rect(topleft = (self.x, self.y))
