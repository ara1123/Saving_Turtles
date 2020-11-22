#!/usr/bin/python3

# This is the genetic algorithm

# This genetic algorithm code is based off an example by Yarpiz
# https://www.youtube.com/watch?v=PhJgktRB1AM
# Thanks Yarpiz!

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

# Create children,
def breed_turtles(problem, params):
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

    # Best Solution found
    best_solution = structure()
    best_solution.path = []
    best_solution.cost = np.inf               # This is the default value, which should be the worst case scenario

    pop = turtle_list
    print("THERE ARE {} TURTLES IN POP".format(len(pop)))
    for turtle in pop:
        if turtle.cost < best_solution.cost:
            best_solution.gene = turtle.gene.copy()

    # Best cost of Iterations
    best_cost_over_iterations = np.empty(maxit)     # array of maxit empty spots

    costs = np.array([turtle.cost for turtle in pop])   # List of costs for every member in population
    avg_cost = np.mean(costs)
    if avg_cost != 0:
        costs = costs/avg_cost

    c_gene_pool = []

    for k in range(nc//2):          # nc is the number of children, a control variable, divided by 2
        # Selecting Parents here
        q = np.random.permutation(npop)     # Randomly selecting the indices of parent list, so parents are RANDOM!!!!
        p1_gene = pop[q[0]].gene.copy()
        p2_gene = pop[q[1]].gene.copy()

        # Perform Crossover
        c1, c2 = crossover(p1_gene, p2_gene, gamma)

        c1 = mutate(c1, mu, sigma)
        c2 = mutate(c2, mu, sigma)

        # Add children to population of children
        children_gene_pool.append(c1)
        children_gene_pool.append(c2)

    return c_gene_pool

def sort_select(pop, popc):
    npop = len(o)
    pop += popc
    pop = sorted(pop, key=lambda x: x.cost)
    pop = pop[0:npop]
    return pop

#Anthony, this will need to be different. His method doesn't work or apply here I'm pretty sure.
def crossover(p1, p2, gamma):
    c1 = np.array(p1)
    c2 = np.array(p2)
    print("Gene of child 1", c1)
    alpha = np.random.uniform(-gamma, 1+gamma, c1.shape()) # * converts the tuple to a list of distinct values/arguments
    c1 = alpha*p1 + (1-alpha)*p2
    c2 = alpha*p2 + (1-alpha)*p1
    return c1.to_list(), c2.to_list()


def mutate(x, mu, sigma):
    y = np.array(x)
    flag = (np.random.rand(*x.gene.shape) <= mu)    # an array of boolean entities
    ind = np.argwhere(flag)                             # A list of the indices where it is true
    y.gene[ind] += (mu + sigma*np.random.randn(*ind.shape))    # anthony has a picture explaining where this came from

    return y.to_list()


def apply_bounds(x, varmin, varmax):
    x.gene = np.maximum(x.gene, varmin)         # The result of this will always be >= varmin
    x.gene = np.minimum(x.gene, varmax)         # The result of this will always be <= varmax

    return x

def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p)*np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
