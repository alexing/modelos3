#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import numpy  # sudo apt-get install python-numpy
from numpy.random import random_integers as rand
from main import FINISH_POINT, STARTING_POINT
import matplotlib.pyplot as pyplot


DEFAULT_DIM=9
RANDOM_DIM=9


def createMap(dim=DEFAULT_DIM): #Default 9 espaciones
    matrix = numpy.zeros(shape=(dim, dim))
    for i in range(0, dim):
        matrix[i][0] = 9
    for j in range(0, dim):
        matrix[dim-1][j] = 9
    for j in range(0, dim):
        matrix[0][j] = 9
    for i in range(0, dim):
        matrix[i][dim-1] = 9
    return matrix

def hardCodeTestCase():
	# Hardcodear matris al principio, despues vemos si hacemos otra cosa
    matrix=createMap()
    
    matrix[7][3] = 7
    matrix[1][7] = 8
    matrix[2][2] = 1
    matrix[3][2] = 3
    matrix[4][3] = 6
    matrix[2][4] = 5
    matrix[2][5] = 4
    matrix[5][5] = 3
    matrix[2][6] = 2
    return matrix

def randomCase():

    matrix=createMap(RANDOM_DIM)
    complexity=.75
    density=.75

    # Only odd shapes
    shape = ((RANDOM_DIM // 2) * 2 + 1, (RANDOM_DIM // 2) * 2 + 1)
     # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))

    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        matrix[y, x] = 9
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if matrix[y_, x_] == 0:
                    matrix[y_, x_] = 9
                    matrix[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 9
                    x, y = x_, y_

    startOK = False
    finishOK = False
    while startOK == False:
        x=rand(0, RANDOM_DIM-1)
        y=rand(0, RANDOM_DIM-1)
        if matrix[x,y]==0:
            matrix[x,y] = STARTING_POINT
            startOK=True

    while finishOK == False:
        x=rand(0, RANDOM_DIM-1)
        y=rand(0, RANDOM_DIM-1)
        if matrix[x,y]==0:
            matrix[x,y] = FINISH_POINT
            finishOK=True

    return matrix