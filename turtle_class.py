#!/usr/bin/python3
import pygame
from PIL import Image
from ypstruct import structure
import random
import math

# This is so rotozoom is called a set number of times when the program runs.
# Will prevent python from crashing
turtle_img_01 = Image.open("assets/turtle2.png")
turtle_img_02 = Image.open("assets/box-turtle.png")
turtle_img_03 = Image.open("assets/diamondback.png")
turtle_img_04 = Image.open("assets/electric.png")
turtle_img_05 = Image.open("assets/fuerte.png")
turtle_img_06 = Image.open("assets/groovy.png")
turtle_img_07 = Image.open("assets/hydro.png")
turtle_img_08 = Image.open("assets/indigo.png")
turtle_img_09 = Image.open("assets/jade.png")
turtle_img_10 = Image.open("assets/kinetic.png")
turtle_img_11 = Image.open("assets/lunar.png")
turtle_img_12 = Image.open("assets/melodic.png")
turtle_img_13 = Image.open("assets/robot-turtle.png")
turtle_img_14 = Image.open("assets/sea-turtle.png")
turt_list = [turtle_img_01, turtle_img_02, turtle_img_03, turtle_img_04, turtle_img_05,
                     turtle_img_06, turtle_img_07, turtle_img_08, turtle_img_09, turtle_img_10,
                     turtle_img_11, turtle_img_12, turtle_img_13, turtle_img_14]

choice = random.randrange(len(turt_list))
img = turt_list[choice]
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
    self.bridge = False
    self.reward = 0
    self.safe = False

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
    rot_surf = animations[angle]
    rot_rect = rot_surf.get_rect(center = (self.rect.centerx, self.rect.centery))
    self.surf = rot_surf
    self.rect = rot_rect


