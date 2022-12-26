input_path = 'advent_of_code_2022/challenges/Day 22: Monkey Map/input'

RIGHT = 0; DOWN = 1; LEFT = 2; UP = 3
facing = RIGHT
pos = None
done = False
instructions = []
screen = {} # row index -> (column_shifting, row)
L = 0 # Counts of rows

REGIONS = { # each region is 50 x 50
                 'B': (0, 50), 'C': (0, 100),
                 'A': (50, 50),
  'E': (100, 0), 'D': (100, 50),
  'F': (150, 0)
}

def region_by_point(_pos):
  for region in REGIONS.keys():
    if _pos[0] >= REGIONS[region][0] and _pos[1] >= REGIONS[region][1] and _pos[0] < REGIONS[region][0] + 50 and _pos[1] < REGIONS[region][1] + 50:
      return region

next_face = {
  RIGHT: { 'R': DOWN,  'L': UP },
  DOWN:  { 'R': LEFT,  'L': RIGHT },
  LEFT:  { 'R': UP,    'L': DOWN },
  UP:    { 'R': RIGHT, 'L': LEFT },
}

next_to_sum = { UP: (-1, 0), DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1) }
def next_pos_from(_pos): r, c = next_to_sum[facing]; return (_pos[0] + r, _pos[1] + c)
is_in_range = lambda i, row: i >= 0 and i < len(row)

wrapping = {
  'A': {
    RIGHT: lambda r, _: (REGIONS['C'][0] + 49, REGIONS['C'][1] + r, UP),
    LEFT: lambda r, _: (REGIONS['E'][0], REGIONS['E'][1] + r, DOWN),
  },
  'B': {
    UP: lambda _, c: (REGIONS['F'][0] + c, REGIONS['F'][1] + 0, RIGHT),
    LEFT: lambda _, c: (REGIONS['E'][0] + c, REGIONS['E'][1], RIGHT),
  },
  'C': {
    UP: lambda _, c: (REGIONS['F'][0] + 49, REGIONS['F'][1] + c, UP),
    DOWN: lambda _, c: (REGIONS['A'][0] + c, REGIONS['A'][1] + 49, LEFT),
    RIGHT: lambda _, c: (REGIONS['D'][0] + c, REGIONS['D'][1] + 49, LEFT),
  },
  'D': {
    DOWN: lambda _, c: (REGIONS['F'][0] + c, REGIONS['F'][1] + 49, LEFT),
    RIGHT: lambda r, _: (REGIONS['C'][0] + 49 - r, REGIONS['C'][1] + 49, LEFT),
  },
  'E': {
    UP: lambda _, c: (REGIONS['A'][0] + c, REGIONS['A'][1], RIGHT),
    LEFT: lambda r, _: (REGIONS['B'][0] + 49 - r , REGIONS['B'][1], RIGHT),
  },
  'F': {
    DOWN: lambda _, c: (REGIONS['C'][0], REGIONS['C'][1] + c, DOWN),
    RIGHT: lambda r, _: (REGIONS['D'][0] + 49, REGIONS['D'][1] + r, UP),
    LEFT: lambda r, c: (REGIONS['B'][0], REGIONS['B'][1] + c, DOWN),
  },
}

def next_pos_wrapping(pos):
  global facing
  region = region_by_point(pos)
  _r = pos[0] - REGIONS[region][0]
  _c = pos[1] - REGIONS[region][1]
  r, c, f = wrapping[region][facing](_r, _c); facing = f; return (r, c)
def turn_to(dir): global facing; facing = next_face[facing][dir]
def move_forward(count, pos):
  global facing
  _pos = pos
  for _ in range(count):
    r, c = next_pos_from(_pos)
    _facing = facing
    if ((r < 0 or r >= L) or not (is_in_range(c - screen[r][0], screen[r][1]))): r, c = next_pos_wrapping(_pos)

    if (screen[r][1][c - screen[r][0]] == '#'): facing = _facing; break # rollback facing
    _pos = r, c
  return _pos

def split_instructions(str):
  instructions = []
  cur = ''
  for c in str:
    if (c == 'L' or c == 'R'):
      instructions.append(int(cur))
      instructions.append(c)
      cur = ''
    else: cur = cur + c
  
  return instructions

with open(input_path) as f:
  row = 0
  for line in f:
    if line == '\n': done = True; continue
    if done: instructions = split_instructions(line[:-1]); continue
    first_col = 0
    for i in line[:-1]:
      if(i != ' '): break
      first_col += 1

    if (row == 0): pos = row, first_col

    screen[row] = (first_col, list(line[first_col:-1]))
    row += 1

L = len(screen)
for inst in instructions:
  if (type(inst) == int): pos = move_forward(inst, pos)
  else: turn_to(inst)

print('Part 2: ', 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)