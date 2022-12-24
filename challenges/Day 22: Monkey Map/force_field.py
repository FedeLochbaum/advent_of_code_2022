input_path = 'advent_of_code_2022/challenges/Day 22: Monkey Map/input0'

RIGHT = 0; DOWN = 1; LEFT = 2; UP = 3
facing = RIGHT
pos = None
done = False
instructions = []
screen = {} # row index -> (column shifting, row)

next_face = {
  RIGHT: { 'R': DOWN, 'L': UP },
  DOWN:  { 'R': LEFT, 'L': RIGHT },
  LEFT:  { 'R': UP, 'L': DOWN },
  UP:    { 'R': RIGHT, 'L': LEFT },
}

next_to_sum = { UP: (-1, 0), DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1) }

def next_pos_from(_pos): r, c = next_to_sum[facing]; return _pos[0] + r, _pos[1] + c

is_in_range = lambda i, row: (i < 0 or i >= len(row))

def first_bottom_row(r, c):
  for _r in range(r + 1, len(screen.keys())):
    if _r == len(screen.keys()) - 1: return _r
    
    shift, row = screen[_r]
    if is_in_range(c - shift, row): continue
    
    return _r

def first_top_row(r, c):
  for _r in reversed(range(0, r -1)):
    if _r == 0: return _r
    
    shift, row = screen[_r]
    if is_in_range(c - shift, row): continue
    
    return _r

def next_pos_wrapping(r, c):
  shift, row = screen[r]

  if facing == RIGHT: return (r, shift)
  if facing == LEFT: return (r, len(row) + shift)

  if (facing == UP): return (first_bottom_row(r, c), c)
  if (facing == UP): return (first_top_row(r, c), c)

def turn_to(dir): facing = next_face[facing][dir]
def move_forward(count, pos):
  _pos = pos
  for _ in range(count):
    r, c = next_pos_from(_pos)
    shift, row = screen[r]
    
    valid_pos = next_pos_wrapping(r, c) if is_in_range(c - shift, row) else (r, c)
    shift, row = screen[valid_pos[0]]
    
    if (row[valid_pos[1] - shift] == '#'): break

    _pos = valid_pos

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
  row = 1
  for line in f:
    if line == '\n': done = True; continue
    if done: instructions = split_instructions(line[:-1]); continue
    first_col = 1
    for i in line[:-1]:
      if(i != ' '): break
      first_col += 1

    if (row == 1): pos = (row, first_col)

    screen[row] = (first_col, [line[first_col - 1:-1]])
    row += 1

for inst in instructions:
  if (type(inst) == int): pos = move_forward(inst, pos)
  else: turn_to(inst)

print('Part 1: ', 1000 * pos[0] + 4 * pos[1] + facing)