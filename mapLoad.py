#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import numpy  # sudo apt-get install python-numpy


def hardCodeTestCase():
	# Hardcodear matris al principio, despues vemos si hacemos otra cosa
    matrix = numpy.zeros(shape=(9, 9))
    for i in range(0, 9):
        matrix[i][0] = 9
    for j in range(0, 9):
        matrix[8][j] = 9
    for j in range(0, 9):
        matrix[0][j] = 9
    for i in range(0, 9):
        matrix[i][8] = 9
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