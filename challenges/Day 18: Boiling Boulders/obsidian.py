input_path = 'advent_of_code_2022/challenges/Day 18: Boiling Boulders/input'

graph = []
points = []
square = '▢'
dot = '.'
max_range = 1000

def sides_of(point): return [
  (point[0] + 1, point[1], point[2]),
  (point[0], point[1] + 1, point[2]),
  (point[0], point[1], point[2] + 1),

  (point[0] - 1, point[1], point[2]),
  (point[0], point[1] - 1, point[2]),
  (point[0], point[1], point[2] - 1),
]

def out_of_range(point): return (
  (point[0] < 0 or point[0] >= max_range) or
  (point[1] < 0 or point[1] >= max_range) or
  (point[2] < 0 or point[2] >= max_range)
)

for x in range(max_range):
  graph.append([])
  for y in range(max_range):
    graph[x].append([])
    for z in range(max_range): graph[x][y].append(dot)

with open(input_path) as f:
  for line in f:
    point = tuple(map(int, line[:-1].split(',')))
    points.append(point)
    graph[point[0]][point[1]][point[2]] = square

# Part 1
sides_exposed = 0
for point in points:
  sides = sides_of(point)
  for side in sides:
    if (out_of_range(side)): continue

    if (graph[side[0]][side[1]][side[2]] == dot): sides_exposed += 1

print('Part 1: ', sides_exposed)