input_path = 'advent_of_code_2022/challenges/Day 12: Hill Climbing Algorithm/input'
from utils import floyd_warshall, dict_from_file, point_by

graph, goal_pos, all_as = dict_from_file(input_path)

shortest_paths = floyd_warshall(graph, graph.__len__(), graph[0].__len__())
print('Part 1: ', shortest_paths[point_by(0, 0)][point_by(goal_pos[0], goal_pos[1])])
print('Part 2: ', min(map(lambda point: shortest_paths[point_by(point[0], point[1])][point_by(goal_pos[0], goal_pos[1])], all_as)))
