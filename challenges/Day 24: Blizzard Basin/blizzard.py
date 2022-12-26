input_path = 'advent_of_code_2022/challenges/Day 24: Blizzard Basin/input'
from a_star import a_star
from graph import BlizzardMap
import math

row_size = 0; col_size = 0
blizzards = []
UP = '^'; DOWN = 'v'; LEFT = '<'; RIGHT = '>'
is_dir = lambda x: x in [UP, DOWN, LEFT, RIGHT]

with open(input_path) as f:
  row = 0
  for line in f:
    if (not col_size): col_size = len(line[:-1])
    for col in range(col_size):
      if (is_dir(line[col])): blizzards.append((line[col], (row - 1, col - 1)))
    row += 1
  row_size = row - 2
  col_size = col_size - 2

initial_point = (-1, 0) # The unique moment where this point is valid
goal = (row_size, col_size - 1) # Goal to achieve
graph = BlizzardMap(blizzards, row_size, col_size)
h = lambda point: int(math.dist(goal, point))
print('Part 1: ', a_star(graph, initial_point, h) - 1)