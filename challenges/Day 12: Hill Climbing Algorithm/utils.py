from queue import PriorityQueue
neighbors = lambda r, c: [[r, c-1], [r-1, c], [r, c+1], [r+1, c]]

point_by = lambda row, col: f'{row}' + ',' + f'{col}'

def dict_from_file(input_path):
  array = []
  goal = None
  with open(input_path) as f:
    for line in f:
      row = []
      for i in range(line[:-1].__len__()):
        if (line[i] == 'E'): goal = [array.__len__(), i]
        row.append(weight_of(line[i]))
      array.append(row)

  return array, goal

def value(char): return (ord(char) & 31) + (26 if char.isupper() else 0)

def weight_of(elem):
  if elem == 'S': return weight_of('a')
  if elem == 'E': return weight_of('z')
  return value(elem)

def distance_obj(row, col):
  distance = {}
  for i in range(row):
    for j in range(col):
      distance[point_by(i, j)] = float('inf')
  return distance

def processed_obj(row, col):
  processed = {}
  for i in range(row):
    for j in range(col):
      processed[point_by(i, j)] = False
  return processed

def dijkstra(graph, row, col, initial, final):
  queue = PriorityQueue()
  processed = processed_obj(row, col)
  distance = distance_obj(row, col)
  distance[initial] = 0
  queue.put((0, initial))

  while not queue.empty():
    _, point = queue.get()
    if(processed[point]): continue
    processed[point] = True
    a, b = point.split(',')
    current = graph[int(a)][int(b)]
    for _r, _c in neighbors(int(a), int(b)):
      if (_r < 0 or _c < 0 or _r >= row or _c >= col): continue
      neighbor = point_by(_r, _c)
      neighbor_val = graph[_r][_c]
      if (neighbor_val > current and (neighbor_val - current) > 1): continue
      if (distance[point] + 1 < distance[neighbor]):
        distance[neighbor] = distance[point] + 1
        queue.put((distance[neighbor], neighbor))
  return distance[final]

shortest_path = dijkstra