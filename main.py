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
params.npop = 10           # Max population size (chromosomes)
params.pc = 1               # The ratio of children to parents. ie) 2 would mean double the amount of children than parents
params.gamma = 0.1          # Randomization factor between parents and children
params.mu = 3             # The mean for the mutation function, which is a Gaussian distribution
params.sigma = 0.1          # The std. dev. for the mutation function
params.beta = 1             # Parent selection variable
params.it = 0
turtle_game = game()
turtle_game.init_game()
turtle_game.init_turtles(params)

# Data from genetic algorithm
best_costs_over_it = []
best_turtles_from_each_it = []

# Run game with initial, random population
turtle_game.run_game()
main_pop = turtle_game.retired_turtles.copy()
turtle_game.reset()

while True:

  # Store turtle list in data structure for ga
  problem.turtle_list = main_pop.copy()

  # print("THERE ARE {} RETIRED TURTLES".format(len(problem.turtle_list)))
  # Fully reset the game by clearing out the previous population
  turtle_game.retired_turtles.clear()

  # Get children
  c_gene_pool = ga.breed_turtles(problem, params)

  turtle_game.init_children(c_gene_pool, params)

  # Calculate cost for new population
  turtle_game.run_game()
  turtle_game.reset()

  # Merge, sort, and select to get new population
  popc = turtle_game.retired_turtles.copy()
  turtle_game.retired_turtles.clear()
  main_pop = ga.sort_select(main_pop, popc)

  # Implement these later
  # best_costs_over_it.append(out.best)

  # best_turtles_from_each_it.append(out.best_solution)


