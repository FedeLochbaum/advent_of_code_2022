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

h1 = lambda point: int(math.dist(goal, point))
h2 = lambda point: int(math.dist(initial_point, point))

graph1 = BlizzardMap(blizzards, row_size, col_size, initial_point, goal)
first_part = a_star(graph1, initial_point, h1) - 1

graph2 = BlizzardMap(graph1.blizzards[first_part], row_size, col_size, goal, initial_point)
second_part = a_star(graph2, goal, h2) - 1

graph3 = BlizzardMap(graph2.blizzards[second_part], row_size, col_size, initial_point, goal)
third_part = a_star(graph3, initial_point, h1) - 1

print('Part 1: ', first_part)
print('Part 2: ', first_part + second_part + third_part)