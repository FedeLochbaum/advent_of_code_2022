input_path = 'advent_of_code_2022/challenges/Day 24: Blizzard Basin/input0'
from a_star import a_star
from graph import BlizzardMap
import math

row_size = 0; col_size = 0
blizzards = []
UP = '^'; DOWN = 'v'; LEFT = '<'; RIGHT = '>'
is_dir = lambda x: x in [UP, DOWN, LEFT, RIGHT]

def elem_to_print(r, c, _blizzards):
  for blizzard in _blizzards:
    if blizzard[1] == (r, c): return blizzard[0]
  return '.'

def print_map(_blizzards):
  for r in range(1, row_size):
    print(''.join([elem_to_print(r, c, _blizzards) for c in range(1, col_size)]))

with open(input_path) as f:
  row = 0
  for line in f:
    if (not col_size): col_size = len(line[:-1])
    for col in range(col_size):
      if (is_dir(line[col])): blizzards.append((line[col], (row, col)))
    row += 1
  row_size = row - 2
  col_size = col_size - 2

initial_point = (-1, 0) # The unique moment where the point is valid
goal = (row_size, col_size - 1) # Goal to achieve
graph = BlizzardMap(blizzards, row_size, col_size)
h = lambda point: math.dist(goal, point)
print('Part 1: ', a_star(graph, initial_point, h))
