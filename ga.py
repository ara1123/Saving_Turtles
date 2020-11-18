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

    # Empty Individual Template
    #empty_turtle_shell = turtle()

    # Best Solution found
    best_solution = structure()
    best_solution.cost = np.inf               # This is the default value, which should be the worst case scenario


    # Creating initial population
    pop = turtle_list

    for turtle in turtle_list:
        #pop[i].position = np.random.uniform(varmin, varmax, nvar)
        #pop[i].cost = costfunc(pop[i].position)
        if turtle.cost < best_solution.cost:
            best_solution.cost = turtle.cost

    # Best cost of Iterations
    best_cost_over_iterations = np.empty(maxit)     # array of maxit empty spots


    costs = np.array([turtle.cost for turtle in turtle_list])   # List of costs for every member in population
    avg_cost = np.mean(costs)
    if avg_cost != 0:
        costs = costs/avg_cost

    pop_children = []
    i = 0
    for k in range(nc//2):          # nc is the number of children, a control variable, divided by 2
        # Selecting Parents here
        #q = np.random.permutation(npop)     # Randomly selecting the indices of parent list, so parents are RANDOM!!!!
        p1 = pop[i]
        p2 = pop[i+1]
        i += 2

        # Roulette wheel selection
        #p1 = pop[roulette_wheel_selection(probs)]
        #p2 = pop[roulette_wheel_selection(probs)]

        # Perform Crossover
        c1, c2 = crossover(p1, p2, gamma)

        # Add children to population of children
        pop_children.append(c1)
        pop_children.append(c2)

    # Merge, sort, and select
    pop += pop_children
    pop = sorted(pop, key=lambda x: x.cost, reverse=True)   # Sorting population by each element's cost
    pop = pop[0:npop]                         # We will have the top npop members of the population

    # Store best cost
    #best_cost_over_iterations[it] = best_solution.cost

    # Show iteration information
    #print("Iteration {}: Best cost = {}".format(it, best_cost_over_iterations[it]))



    # Output
    #out = structure()
    #out.pop = pop
    #out.best_solution = best_solution
    #out.best_cost_over_iterations = best_cost_over_iterations

    return pop


def crossover(p1, p2, gamma):

    c1 = p1
    c2 = p2
    #alpha = np.random.uniform(-gamma, 1 + gamma, *c1.position.shape)

    # Some level of randomization between parents and offspring
    #c1.position = alpha*p1.position + (1-alpha)*p2.position
    #c2.position = alpha*p2.position + (1-alpha)*p1.position


    return c1, c2


def mutate(x, mu, sigma):
    y = x

    #flag = (np.random.rand(*x.position.shape) <= mu)    # an array of boolean entities
    #ind = np.argwhere(flag)                             # A list of the indices where it is true

    #y.position[ind] += (mu + sigma*np.random.randn(*ind.shape))    # anthony has a picture explaining where this came from

    return y


def apply_bounds(x, varmin, varmax):
    x.position = np.maximum(x.position, varmin)         # The result of this will always be >= varmin
    x.position = np.minimum(x.position, varmax)         # The result of this will always be <= varmax

    return x

def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
