input_path = 'advent_of_code_2022/challenges/Day 18: Boiling Boulders/input'
from collections import deque

points = set()
surfaces = set()
inside = set()

def sides_of(point): return [
  (point[0] + 1, point[1], point[2]),
  (point[0], point[1] + 1, point[2]),
  (point[0], point[1], point[2] + 1),

  (point[0] - 1, point[1], point[2]),
  (point[0], point[1] - 1, point[2]),
  (point[0], point[1], point[2] - 1),
]

def check_side(point):
  # Memoized to void repeat checks
  if point in surfaces: return True
  if point in inside: return False

  # Check sides from points using a bfs style and Memoize them by class
  queue = deque()
  visited = set()
  queue.append(point)

  while(queue):
    _point = queue.popleft()
    if (_point in points or _point in visited): continue # Ignore points which we will check later or which were visited before
    
    visited.add(_point)

    if visited.__len__() > 10: surfaces.union(visited); return True
    for side in sides_of(_point): queue.append(side)

  inside.union(visited)
  return False

with open(input_path) as f:
  for line in f:
    point = tuple(map(int, line[:-1].split(',')))
    points.add(point)

# Part 2
sides_exposed = 0
for point in points:
  for side in sides_of(point):
    if (check_side(side)): sides_exposed += 1

print('Part 2: ', sides_exposed)
