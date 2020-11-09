#!/usr/bin/python3
from game_class import game
from ypstruct import structure


params = structure()
params.npop = 100

turtle_game = game()
turtle_game.init_game()

while True:
  turtle_game.init_turtles(params)
  turtle_game.run_game()
  turtle_game.reset()
