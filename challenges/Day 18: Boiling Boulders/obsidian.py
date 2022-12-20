input_path = 'advent_of_code_2022/challenges/Day 18: Boiling Boulders/input'

points = []

def sides_of(point): return [
  (point[0] + 1, point[1], point[2]),
  (point[0], point[1] + 1, point[2]),
  (point[0], point[1], point[2] + 1),

  (point[0] - 1, point[1], point[2]),
  (point[0], point[1] - 1, point[2]),
  (point[0], point[1], point[2] - 1),
]

with open(input_path) as f:
  for line in f:
    point = tuple(map(int, line[:-1].split(',')))
    points.append(point)

# Part 1
sides_exposed = 0
for point in points:
  sides = sides_of(point)
  for side in sides:
    if (side not in points): sides_exposed += 1

print('Part 1: ', sides_exposed)