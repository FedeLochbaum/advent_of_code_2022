input_path = 'advent_of_code_2022/challenges/Day 12: Hill Climbing Algorithm/input'
from utils import shortest_path, dict_from_file, point_by

graph, goal_pos, all_as = dict_from_file(input_path)

part1 = shortest_path(graph, graph.__len__(), graph[0].__len__(), point_by(0, 0), point_by(goal_pos[0], goal_pos[1]))
print('Part 1: ', part1)
_min = part1
for a in all_as:
  _min = min(_min, shortest_path(graph, graph.__len__(), graph[0].__len__(), point_by(a[0], a[1]), point_by(goal_pos[0], goal_pos[1])))

print(_min)