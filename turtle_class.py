#!/usr/bin/python3
import pygame
from PIL import Image
from ypstruct import structure
import math

# This is so rotozoom is called a set number of times when the program runs.
# Will prevent python from crashing
img = Image.open("assets/turtle.png")
img = img.resize((30, 30)) # This should be tilesize
surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
animations = {0 : pygame.transform.rotozoom(surface, -90, 1),
              45 : pygame.transform.rotozoom(surface, -45, 1),
              90 : surface,
              135 : pygame.transform.rotozoom(surface, 45, 1),
              180 : pygame.transform.rotozoom(surface, 90, 1),
              -45 : pygame.transform.rotozoom(surface, -135, 1),
              -90 : pygame.transform.rotozoom(surface, -180, 1),
              -135 : pygame.transform.rotozoom(surface, -225, 1),
              -225 : pygame.transform.rotozoom(surface, -315, 1)
              }

class turtle(object):

  def __init__(self, turtle_params):
    self.surf = animations[0]
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
    angle = math.degrees(math.atan2(-dy, dx))
    print(dx, dy, "So an angle of ", angle)
    rot_surf = animations[angle]
    rot_rect = rot_surf.get_rect(center = (self.rect.centerx, self.rect.centery))
    self.surf = rot_surf
    self.rect = rot_rect
