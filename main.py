#!/usr/bin/python3
import pygame, sys
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from ypstruct import structure
import my_GA as ga
from game_class import game
from turtle_class import turtle
from bridge_class import bridge

# Sphere Cost Function
def sphere(x):
    return sum(x**2)


# Problem Definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5            # Number of variables (genes)
problem.varmin = -10        # Minimum value of variables
problem.varmax = 10         # Maximum value of variables


# GA Parameters
params = structure()
params.maxit = 100          # Max iterations
params.npop = 20           # Max population size (chromosomes)
params.pc = 1               # The ratio of children to parents. ie) 2 would mean double the amount of children than parents
params.gamma = 0.1          # Randomization factor between parents and children
params.mu = 0.1             # The mean for the mutation function, which is a Gaussian distribution
params.sigma = 0.1          # The std. dev. for the mutation function
params.beta = 1             # Parent selection variable
turtle_game = game()
turtle_game.init_game()
turtle_game.init_turtles(params)

while True:

  turtle_game.run_game()

  overall_turtle_list = turtle_game.turtle_list + turtle_game.retired_turtles

  for turtle in overall_turtle_list:
    turtle.cost = turtle_game.cost_function(turtle)
  overall_turtle_list.sort(key=lambda x: x.cost, reverse=True)      # A sorted list of turtles by reward

  problem.turtle_list = overall_turtle_list               # Getting rid of the worst 50% of parents

  # Run GA
  out = ga.run(problem, params)


  turtle_game.reset()
  turtle_game.init_turtles(params)
  i = 0
  for t in out:
    turtle_game.turtle_list[i].path = t.path
    i += 1

"""# Results
plt.plot(out.bestcost)
#plt.semilogy(out.bestcost)      # Using a logarithmic scale for y axis, to better see improvement
plt.xlim(0, params.maxit)
plt.ylabel('Best Cost')
plt.xlabel('Iterations')
plt.title('Genetic Algorithm')
plt.grid(True)
plt.show()
"""