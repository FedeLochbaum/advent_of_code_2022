input_path = 'advent_of_code_2022/challenges/Day 12: Hill Climbing Algorithm/input0'
from utils import floyd_warshall, dict_from_file, point_by

graph, goal_pos, all_as = dict_from_file(input_path)

points = [[r, c] for c in range(graph[0].__len__()) for r in range(graph.__len__())]
all_as_index = []
for i in range(points.__len__()):
  if points[i] in all_as: all_as_index.append(i)

shortest_paths = floyd_warshall(graph, points)
print('Part 1: ', shortest_paths[0][points.index(goal_pos)])
print('Part 2: ', min(map(lambda i: shortest_paths[i][points.index(goal_pos)], all_as_index)))