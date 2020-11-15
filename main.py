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

  for turtle in turtle_game.retired_turtles:
    print(turtle_game.reward_function(turtle))
  turtle_game.reset()
