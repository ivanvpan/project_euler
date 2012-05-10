#!/usr/bin/python

BIG_NUMBER = 999999999

f = open('matrix.txt')
matrix = []
for line in f:
    matrix.append([int(i) for i in line.split(',')])

def walk_matrix(i, j, matrix):
    results = []
    if i < 79:
        results.append(walk_matrix(i+1, j, matrix))
    if j < 79:
        results.append(walk_matrix(i, j+1, matrix))
    if i == 79 and j == 79:
        return matrix[i][j]
    return matrix[i][j] + min(results)

print walk_matrix(0, 0, matrix)
