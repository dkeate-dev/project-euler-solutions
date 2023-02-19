# Copyright 2023, Dustin Keate, All rights reserved.

# Lattice Paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?



# YAY, RECURSION, MAYBE? And identified.
# WHEN IT SUCKS:  :-(
# Stop repeating calculations and store solutions in an array and return that instead of going over and over and over and...

GRID_SIZE = 20
INTERSECTIONS = GRID_SIZE + 1

grid = [[0 for j in range(INTERSECTIONS)] for i in range(INTERSECTIONS)]

start_pos_x = GRID_SIZE
start_pos_y = GRID_SIZE

grid[start_pos_x][start_pos_y-1] = 1
grid[start_pos_x-1][start_pos_y] = 1


def lattice (pos_x, pos_y):
  result = 0
  if grid[pos_x][pos_y] > 0:
    return grid[pos_x][pos_y]
  else:
    if pos_x < GRID_SIZE:
      result += lattice(pos_x + 1, pos_y)
    if pos_y < GRID_SIZE:
      result += lattice(pos_x, pos_y + 1)
  grid[pos_x][pos_y] = result
  return result
  

print(lattice (0,0))
