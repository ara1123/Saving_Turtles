#!/usr/bin/python3
import pygame
from PIL import Image


def image_to_tile(path_to_image, TILESIZE):
  img = Image.open(path_to_image)
  img = img.resize((TILESIZE, TILESIZE))
  return pygame.image.fromstring(img.tobytes(), img.size, img.mode)

def load_car(path_to_image, tilesize):
  img = Image.open(path_to_image)
  img = img.resize((tilesize, tilesize))
  surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
  surface.set_colorkey((0,0,0))
  surface.convert()
  return surface
