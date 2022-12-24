input_path = 'advent_of_code_2022/challenges/Day 22: Monkey Map/input'

RIGHT = 0; DOWN = 1; LEFT = 2; UP = 3
facing = RIGHT
pos = None
done = False
instructions = []
screen = {} # row index -> (column shifting, row)
L = 0 # Counts of rows

next_face = {
  RIGHT: { 'R': DOWN, 'L': UP },
  DOWN:  { 'R': LEFT, 'L': RIGHT },
  LEFT:  { 'R': UP, 'L': DOWN },
  UP:    { 'R': RIGHT, 'L': LEFT },
}

next_to_sum = { UP: (-1, 0), DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1) }
def next_pos_from(_pos): r, c = next_to_sum[facing]; return _pos[0] + r, _pos[1] + c
is_in_range = lambda i, row: (i >= 0 and i < len(row))

def first_bottom_row(r, c):
  for _r in range(r + 1, L):
    if _r == L - 1: return _r
    
    shift, row = screen[_r]
    if (not is_in_range(c - shift, row)): return _r - 1

def first_top_row(r, c):
  for _r in reversed(range(0, r - 1)):
    if _r == 0: return _r
    
    shift, row = screen[_r]
    if (not is_in_range(c - shift, row)): return _r + 1

def next_pos_wrapping(r, c):
  if (facing == UP): return (first_bottom_row(r, c), c)
  if (facing == DOWN): return (first_top_row(r, c), c)

  shift, row = screen[r]
  if facing == RIGHT: return (r, shift)
  if facing == LEFT: return (r, len(row) -1 + shift)

def turn_to(dir): global facing; facing = next_face[facing][dir]
def move_forward(count, pos):
  _pos = pos
  for _ in range(count):
    r, c = next_pos_from(_pos)

    if ((r < 0 or r >= L) or not (is_in_range(c - screen[r][0], screen[r][1]))): r, c = next_pos_wrapping(r, c)

    shift, row = screen[r]
    if (row[c - shift] == '#'): break

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

    if (row == 0): pos = (row, first_col)

    screen[row] = (first_col, list(line[first_col:-1]))
    row += 1

L = len(screen)

i_i = 0
for inst in instructions:
  if (type(inst) == int):
    pos = move_forward(inst, pos)
  else: turn_to(inst)
  i_i += 1

print('Part 1: ', 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing)