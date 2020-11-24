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

"""def run(problem, params):
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

    return out"""


# Create children,
def breed_turtles(problem, params):
    # Extracting Problem information
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax
    turtle_list = problem.turtle_list

    # Extracting Parameters
    maxit = params.maxit
    npop = params.npop
    beta = params.beta
    pc = params.pc
    nc = int(np.round(pc * npop / 2) * 2)  # a ratio times total pop, rounded to make sure it is an integer value
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma
    it = params.it

    # Best Solution found
    best_solution = structure()
    best_solution.path = []
    best_solution.cost = np.inf  # This is the default value, which should be the worst case scenario

    pop = turtle_list
    # Sorting by best cost. the more positive the better
    pop.sort(key=lambda x: x.cost, reverse=False)

    print("THERE ARE {} TURTLES IN POP".format(len(pop)))
    for turtle in pop:
        if turtle.cost < best_solution.cost:
            best_solution.gene = turtle.gene.copy()

    # Best cost of Iterations
    best_cost_over_iterations = np.empty(maxit)  # array of maxit empty spots

    costs = np.array([turtle.cost for turtle in pop])  # List of costs for every member in population
    avg_cost = np.mean(costs)
    if avg_cost != 0:
        costs = costs / avg_cost

    children_gene_pool = []

    for k in range(nc // 2):  # nc is the number of children, a control variable, divided by 2
        # Selecting Parents here
        p1_gene = pop[0].gene.copy()
        p2_gene = pop[1].gene.copy()

        # Perform Crossover
        c1, c2 = crossover(p1_gene, p2_gene, mu)

        # Add children to population of children
        children_gene_pool.append(c1)
        children_gene_pool.append(c2)

    return children_gene_pool


def sort_select(pop, popc):
    npop = len(pop)
    pop += popc
    pop = sorted(pop, key=lambda x: x.cost)
    pop = pop[0:npop]
    return pop


def crossover(p1, p2, mu):
    # For half of the first parents, + half of the seconds, so parent's path length isnt an issue
    #c1_gene = p1[:len(p1) // 2] + p2[len(p2) // 2:]
    #c2_gene = p2[:len(p2) // 2] + p1[len(p1) // 2:]
    c1_gene = p1
    c2_gene = p2
    c1_gene = mutate(c1_gene, mu)
    c2_gene = mutate(c2_gene, mu)

    return c1_gene, c2_gene


def mutate(x, mu):
    m_gene = x
    # We may want to remove west/southwest from the lineup, so the little bastards cant backtrack
    # [N, NE, E, SE, S, SW, W, NW]
    directions = [0, 1, 2, 3, 4, 5, 2, 7]

    for index in range(0, len(m_gene), mu):
        m_gene[index] = random.choice(directions)

    # Adding more movements, so that turtles have capabilities beyond the parent
    for i in range(100):
        m_gene.append(random.choice(directions))

    return m_gene


def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p) * np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]
