#!/usr/bin/python3
import pygame
from PIL import Image
from ypstruct import structure

class turtle(object):
  def __init__(self, turtle_params):
    img = Image.open("assets/turtle.png")
    img = img.resize((turtle_params.tilesize // 2, turtle_params.tilesize // 2))
    self.surf = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    self.surf = pygame.transform.rotozoom(self.surf, -90, 1)
    self.rect = self.surf.get_rect(center = turtle_params.start)
    self.path = turtle_params.path
    self.iteration = 0
    self.dead = False
    self.stopped = False
    self.score = 0
