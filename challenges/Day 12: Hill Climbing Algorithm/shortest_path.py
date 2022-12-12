input_path = 'advent_of_code_2022/challenges/Day 12: Hill Climbing Algorithm/input'
from utils import shortest_path, dict_from_file, point_by

graph, goal_pos = dict_from_file(input_path)

print(shortest_path(graph, graph.__len__(), graph[0].__len__(), point_by(0, 0), point_by(goal_pos[0], goal_pos[1])))