input_path = 'advent_of_code_2022/challenges/Day 8: Treetop Tree House/input'

visibles = []

def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([int(num) for num in line[:-1]])
  return array

graph = dict_from_file(input_path)

first_row = [[0, i] for i in range(graph[0].__len__())] # aca se mira hacia abajo
last_row = [[graph.__len__() - 1, i] for i in range(graph[0].__len__())] # acca se mira hacia arriba
first_column = [[i, 0] for i in range(graph.__len__())] # aca es mira hacia la derecha
last_column = [[i, graph[0].__len__() - 1] for i in range(graph.__len__())] # aca se mira hacia la izq

def look_point_applying(graph, point, visibles, apply_next):
  prev = graph[point[0]][point[1]]
  visibles.append(' '.join(str(e) for e in point))
  while (True):
    point = apply_next(point)
    if (point[0] < 0 or point[0] >= graph.__len__() or point[1] < 0 or point[1] >= graph[0].__len__()): break
    next_val =  graph[point[0]][point[1]]
    if (next_val > prev): prev = next_val; visibles.append(' '.join(str(e) for e in point))

def extend_visibles_applying(graph, points, visibles, apply_next):
  for point in points:
    look_point_applying(graph, point, visibles, apply_next)

extend_visibles_applying(graph, first_row, visibles, lambda point: [point[0] + 1, point[1]] )
extend_visibles_applying(graph, last_row, visibles, lambda point: [point[0] - 1, point[1]] )
extend_visibles_applying(graph, first_column, visibles, lambda point: [point[0], point[1] + 1] )
extend_visibles_applying(graph, last_column, visibles, lambda point: [point[0], point[1] - 1] )

print('Part 1: ', set(visibles).__len__())
