input_path = 'advent_of_code_2022/challenges/Day 8: Treetop Tree House/input'

visibles = []

def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([int(num) for num in line[:-1]])
  return array

graph = dict_from_file(input_path)

first_row = [[0, i] for i in range(graph[0].__len__())]
last_row = [[graph.__len__() - 1, i] for i in range(graph[0].__len__())]
first_column = [[i, 0] for i in range(graph.__len__())]
last_column = [[i, graph[0].__len__() - 1] for i in range(graph.__len__())]

def look_point_applying(graph, point, visibles, next):
  prev = graph[point[0]][point[1]]
  visibles.append(''.join(str(e) for e in point))
  while (True):
    point = next(point)
    if (point[0] < 0 or point[0] >= graph.__len__() or point[1] < 0 or point[1] >= graph[0].__len__()): break
    next_val =  graph[point[0]][point[1]]
    if (next_val > prev): prev = next_val; visibles.append(''.join(str(e) for e in point))

def extend_visibles_applying(graph, points, visibles, next):
  for point in points:
    look_point_applying(graph, point, visibles, next)

TOP = lambda point: [point[0] + 1, point[1]]
BOTTOM = lambda point: [point[0] - 1, point[1]]
LEFT = lambda point: [point[0], point[1] - 1]
RIGHT = lambda point: [point[0], point[1] + 1]

extend_visibles_applying(graph, first_row, visibles, BOTTOM)
extend_visibles_applying(graph, last_row, visibles, TOP)
extend_visibles_applying(graph, first_column, visibles, RIGHT)
extend_visibles_applying(graph, last_column, visibles, LEFT)

print('Part 1: ', set(visibles).__len__())

def visibles_applying(max, point, graph, next):
  count = 0
  while (True):
    point = next(point)
    if (point[0] < 0 or point[0] >= graph.__len__() or point[1] < 0 or point[1] >= graph[0].__len__()): break
    next_val =  graph[point[0]][point[1]]
    count += 1
    if (next_val >= max): break
  return count

def scenic_score_of(point, graph):
  val = graph[point[0]][point[1]]
  return (visibles_applying(val, point, graph, BOTTOM) *
    visibles_applying(val, point, graph, TOP) *
    visibles_applying(val, point, graph, RIGHT) *
    visibles_applying(val, point, graph, LEFT))

max_scenic_score = 0
for r in range(graph.__len__()):
  for c in range(graph[r].__len__()):
    score = scenic_score_of([r, c], graph)
    max_scenic_score = max(max_scenic_score, score)
print('Part 2: ', max_scenic_score)