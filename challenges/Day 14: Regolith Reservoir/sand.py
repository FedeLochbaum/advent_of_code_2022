input_path = 'advent_of_code_2022/challenges/Day 14: Regolith Reservoir/input0'

starting_sand_point = [0, 500]
max_row = 200; max_col = 600
_min_col = float('inf'); _max_col = 0; _min_row = 0; _max_row = 0
row_floor = 0

cave = [['.' for _ in range(max_col)] for _ in range(max_row)] # Original cave

# Print cave
def print_cave():
  # for r in range(_min_row, _max_row + 1): print(' '.join([cave[r][c] for c in range(_min_col, _max_col + 1)]))
  for r in range(_min_row, row_floor + 1):
    if (r == row_floor): print(''.join(['F'] * ((_max_col + 10) - (_min_col - 6)) )); continue

    print(''.join([cave[r][c] for c in range(_min_col - 6, _max_col + 10)]))

def insert_blocks(ps):
  for p in ps: cave[p[0]][p[1]] = '#'

def middle_points(p1, p2): return (
  [[p1[0], i] for i in range(min(p1[1], p2[1] + 1), max(p1[1], p2[1] + 1))] if p1[0] == p2[0] else
  [[i, p1[1]] for i in range(min(p1[0], p2[0] + 1), max(p1[0], p2[0] + 1))]
)

def is_valid_point(point, row_limits, col_limits):
  if (point[0] not in range(row_limits[0], row_limits[1])): return False
  if (point[1] not in range(col_limits[0], col_limits[1])): return False

  return True

def is_out(point):
  if (point[0] < 0 or point[0] >= max_row): return True
  if (point[1] < 0 or point[1] >= max_col): return True

  return False

def not_blocked(point):
  if (point[0] == row_floor): return False

  if (is_out(point)): return True

  return cave[point[0]][point[1]] == '.'

def next_sand_point(point):
  next = [point[0] + 1, point[1]]
  if (not_blocked(next)): return next
  
  next = [point[0] + 1, point[1] - 1]
  if (not_blocked(next)): return next

  next = [point[0] + 1, point[1] + 1]
  if (not_blocked(next)): return next

  return point

def simulate_next_sand_unit():
  point = starting_sand_point # The first point is [0, 500]
  next_point = next_sand_point(point) # Calculate the next fall position

  while(point != next_point):
    point = next_point
    next_point = next_sand_point(point)

  return point # When the unit sand is not to move anymore, just return the point

with open(input_path) as f:
  for line in f:
    ranges = line[:-1].split(' -> ')
    ranges = list(map(lambda str: [int(str.split(',')[1]), int(str.split(',')[0])], ranges)) # inverted
    for i in range(ranges.__len__()):
      to_insert = [ranges[i]] if i == 0 else middle_points(ranges[i-1], ranges[i])

      row_floor = max(row_floor, ranges[i][0] + 2)
      _min_row = min(_min_row, ranges[i][0]); _max_row = max(_max_row, ranges[i][0])
      _min_col = min(_min_col, ranges[i][1]); _max_col = max(_max_col, ranges[i][1])

      cave[ranges[i][0]][ranges[i][1]] = '#'
      insert_blocks(to_insert)

row_limits = [_min_row, _max_row + 1]; col_limits = [_min_col, _max_col + 1]

def move_sand():
  next_point = simulate_next_sand_unit() # Get the next position
  if (next_point == starting_sand_point and cave[next_point[0]][next_point[1]] == 'o'): return False, next_point
  
  cave[next_point[0]][next_point[1]] = 'o'
    
  return True, next_point

# Simulate sand unit
unit = 0;
while(True):
  res, point = move_sand()
  if (not res): break
  unit +=1

# To debug the sand
# for i in range(93):
#   r, point = move_sand()
#   print_cave()
#   print('point: ', point)

print('Part 2: ', unit)
print_cave()
