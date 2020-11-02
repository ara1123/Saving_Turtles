#!/usr/bin/python3
import pygame
from PIL import Image
from ypstruct import structure
import math

class turtle(object):
  def __init__(self, turtle_params):
    img = Image.open("assets/turtle.png")
    img = img.resize((turtle_params.tilesize // 2, turtle_params.tilesize // 2))
    self.surf = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    self.surf = pygame.transform.rotozoom(self.surf, -90, 1)
    self.rect = self.surf.get_rect(center = turtle_params.start)
    self.path = turtle_params.path
    self.iteration = 0
    self.effort = 0
    self.dead = False
    self.stopped = False
    self.score = 0

  def kill(self):
    self.dead = True
    self.stopped = True

  def stop(self):
    self.stopped = True

  def reset(self):
    self.iteration = 0
    self.effort = 0
    self.dead = False
    self.stopped = False

  def animate(self, dx, dy):
    angle = math.degrees(math.atan2(dy, dx)) + 90
    surf = pygame.transform.rotozoom(self.surf, angle, 1)
    print(dy, dx, "So an angle of ", angle)
    self.surf = surf
