#!/usr/bin/python3

# This is the genetic algorithm

import pygame, sys
import random
import numpy as np
import matplotlib.pyplot as plt
import copy
from PIL import Image
from ypstruct import structure
from turtle_class import turtle
import pygame


def run(problem, params):

    # Extracting Problem information
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax
    turtle_list = problem.turtle_list

    # Extracting Parameters
    maxit = params.maxit
    npop = params.npop
    beta = params.beta
    pc = params.pc
    nc = int(np.round(pc*npop/2)*2)            # a ratio times total pop, rounded to make sure it is an integer value
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma
    it = params.it

    # Empty Individual Template
    #empty_turtle_shell = turtle()

    # Best Solution found
    best_solution = structure()
    best_solution.path = []
    best_solution.cost = np.inf               # This is the default value, which should be the worst case scenario

    pop = turtle_list
    print("THERE ARE {} TURTLES IN POP".format(len(pop)))
    for turtle in pop:
        if turtle.cost < best_solution.cost:
            best_solution.path = turtle.path.copy()

    # Best cost of Iterations
    best_cost_over_iterations = np.empty(maxit)     # array of maxit empty spots

    costs = np.array([turtle.cost for turtle in pop])   # List of costs for every member in population
    avg_cost = np.mean(costs)
    if avg_cost != 0:
        costs = costs/avg_cost

    pop_children = []
    i = 0
    # for k in range(nc//2):          # nc is the number of children, a control variable, divided by 2
    #     # Selecting Parents here
    #     q = np.random.permutation(npop)     # Randomly selecting the indices of parent list, so parents are RANDOM!!!!
    #     p1 = pop[i]
    #     p2 = pop[i+1]
    #     i += 2

    #     # Roulette wheel selection
    #     #p1 = pop[roulette_wheel_selection(probs)]
    #     #p2 = pop[roulette_wheel_selection(probs)]

    #     # Perform Crossover
    #     c1, c2 = crossover(p1, p2, gamma)

    #     # Add children to population of children
    #     pop_children.append(c1)
    #     pop_children.append(c2)

    # Merge, sort, and select
    pop += pop_children
    pop = sorted(pop, key=lambda x: x.cost, reverse=True)   # Sorting population by each element's cost
    pop = pop[0:npop]                         # We will have the top npop members of the population

    # Store best cost
    best_cost = best_solution.cost

    # Output
    out = structure()
    out.pop = pop
    out.best_solution = best_solution
    out.best_cost = best_cost

    return out


def crossover(p1, p2, gamma):

    return p1, p2


def mutate(x, mu, sigma):
    y = x

    flag = (np.random.rand(*x.gene.shape) <= mu)    # an array of boolean entities
    ind = np.argwhere(flag)                             # A list of the indices where it is true

    y.gene[ind] += (mu + sigma*np.random.randn(*ind.shape))    # anthony has a picture explaining where this came from

    return y


def apply_bounds(x, varmin, varmax):
    x.gene = np.maximum(x.gene, varmin)         # The result of this will always be >= varmin
    x.gene = np.minimum(x.gene, varmax)         # The result of this will always be <= varmax

    return x

def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
