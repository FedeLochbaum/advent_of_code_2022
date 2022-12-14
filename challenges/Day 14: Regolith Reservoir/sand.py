input_path = 'advent_of_code_2022/challenges/Day 14: Regolith Reservoir/input0'

starting_sand_point = [500, 0]
max_row = 10; max_col = 550
_min_col = float('inf'); _max_col = 0; _min_row = float('inf'); _max_row = 0

cave = [['.' for _ in range(max_col)] for _ in range(max_row)] # Original cave

def insert_blocks(ps):
  for p in ps: cave[p[0]][p[1]] = '#'

def middle_points(p1, p2): return (
  [[p1[0], i] for i in range(min(p1[1], p2[1] + 1), max(p1[1], p2[1] + 1))] if p1[0] == p2[0] else
  [[i, p1[1]] for i in range(min(p1[0], p2[0] + 1), max(p1[0], p2[0] + 1))]
)

with open(input_path) as f:
  for line in f:
    ranges = line[:-1].split(' -> ')
    ranges = list(map(lambda str: [int(str.split(',')[1]), int(str.split(',')[0])], ranges)) # inverted
    for i in range(ranges.__len__()):
      to_insert = [ranges[i]] if i == 0 else middle_points(ranges[i-1], ranges[i])

      _min_row = min(_min_row, ranges[i][0]); _max_row = max(_max_row, ranges[i][0])
      _min_col = min(_min_col, ranges[i][1]); _max_col = max(_max_col, ranges[i][1])

      cave[ranges[i][0]][ranges[i][1]] = '#'
      insert_blocks(to_insert)

print('min_row: ', _min_row, ' max_row: ', _max_row)
print('min_col: ', _min_col, ' max_col: ', _max_col)

# Print cave
for r in range(_min_row, _max_row + 1):
  print([cave[r][c] for c in range(_min_col, _max_col + 1)])
