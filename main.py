#!/usr/bin/python3
import pygame, sys
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from ypstruct import structure
import ga
from game_class import game
from turtle_class import turtle
from bridge_class import bridge


# Problem Definition
problem = structure()
problem.nvar = 5            # Number of variables (genes)
problem.varmin = 0        # Minimum value of variables
problem.varmax = 7         # Maximum value of variables


# GA Parameters
params = structure()
params.maxit = 100          # Max iterations
params.npop = 20           # Max population size (chromosomes)
params.pc = 1               # The ratio of children to parents. ie) 2 would mean double the amount of children than parents
params.gamma = 0.1          # Randomization factor between parents and children
params.mu = 0.1             # The mean for the mutation function, which is a Gaussian distribution
params.sigma = 0.1          # The std. dev. for the mutation function
params.beta = 1             # Parent selection variable
params.it = 0
turtle_game = game()
turtle_game.init_game()
turtle_game.init_turtles(params)

# Data from genetic algorithm
best_costs_over_it = []
best_turtles_from_each_it = []

while True:

  turtle_game.run_game()

  # This stuff should be done inside the GA
  # overall_turtle_list = turtle_game.turtle_list + turtle_game.retired_turtles

  # for turtle in overall_turtle_list:
  #   turtle.cost = turtle_game.cost_function(turtle)
  # overall_turtle_list.sort(key=lambda x: x.cost, reverse=True)      # A sorted list of turtles by reward

  # problem.turtle_list = overall_turtle_list               # Getting rid of the worst 50% of parents

  # Run GA
  problem.turtle_list = turtle_game.retired_turtles.copy()
  print("THERE ARE {} RETIRED TURTLES".format(len(problem.turtle_list)))
  turtle_game.retired_turtles.clear()
  out = ga.run(problem, params)
  turtle_game.set_turtle_list(out.pop)
  best_costs_over_it.append(out.best)
  best_turtles_from_each_it.append(out.best_solution)

  turtle_game.reset()


