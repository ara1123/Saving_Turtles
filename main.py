#!/usr/bin/python3
from game_class import game
from ypstruct import structure


params = structure()
params.npop = 1

turtle_game = game()
turtle_game.init_game()
turtle_game.init_turtles(params)
turtle_game.run_game()
