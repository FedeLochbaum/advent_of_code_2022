input_path = 'advent_of_code_2022/challenges/Day 23: Unstable Diffusion/input0'
from collections import deque

scan = {}; rounds = 1
N = (-1, 0); NE = (-1, 1); E = (0, 1); SE = (1, 1); S = (1, 0); SW = (1, -1); W = (0, -1); NW = (-1, -1)
DIRS = [N, NE, E, SE, S, SW, W, NW]

class Check():
  def __init__(self, dirs, dir):
    self.dirs = dirs
    self.dir = dir

  def check(self, point):
    for dir in self.dirs:
      _r, _c = point[0] + dir[0], point[1] + dir[1]
      if _r not in scan: return True
      if _c not in scan[_r]: return True
      if scan[_r][_c] == '.': return True

    return False
  
  def next(self, point): return (point[0] + self.dir[0], point[1] + self.dir[1])

movements = deque([ Check([N, NE, NW], N), Check([S, SE, SW], S), Check([W, NW, SW], W), Check([E, NE, SE], E) ])
ele_for = lambda r, c: '.' if r not in scan or c not in scan[r] else scan[r][c]

with open(input_path) as f:
  row = 0
  for line in f:
    scan[row] = {}
    r = list(line[:-1])
    for i in range(len(r)): scan[row][i] = r[i]
    row += 1

def next_movement_for(r, c):
  if '#' not in map(lambda p: ele_for(r + p[0], c + p[1]), DIRS): return None

  for move in movements:
    if move.check((r, c)): return move.next((r, c))

def considering_next_movements():
  next_spaces = {}
  for r in scan.keys():
    for c in scan[r].keys():
      if (scan[r][c] == '#'):
        pair = next_movement_for(r, c)
        if (pair == None): continue # Nothing to do now
        if (pair not in next_spaces): next_spaces[pair] = []
        next_spaces[pair].append((r, c))
  return next_spaces

def round():
  nexts_spaces = considering_next_movements() # { pos: [elf_pos_1, ..., elf_pos_i] } 
  copy = scan.copy()
  for _pos in nexts_spaces.keys():
    elfs = nexts_spaces[_pos]
    if (len(elfs) == 1):
      elf = elfs[0]
      if (elf not in nexts_spaces):
        copy[elf[0]][elf[1]] = '.'

      if _pos[0] not in copy: copy[_pos[0]] = {}
      copy[_pos[0]][_pos[1]] = '#'
  return copy

for _ in range(rounds): scan = round(); movements.append(movements.popleft())

min_row = float('inf'); min_col = float('inf'); max_row = 0; max_col = 0
for row_num in scan.keys():
  if '#' in scan[row_num].values():
    min_row = min(min_row, int(row_num))
    max_row = max(max_row, int(row_num))
  for col_num in scan[row_num].keys():
    if (scan[row_num][col_num] == '#'):
      min_col = min(min_col, int(col_num))
      max_col = max(max_col, int(col_num))

empty_tiles = 0
for r in range(min_row, max_row + 1):
  for c in range(min_col, max_col + 1):
    if (c not in scan[r] or scan[r][c] == '.'): empty_tiles += 1

for r in range(min_row, max_row + 1):
  print(''.join([ele_for(r, c) for c in range(min_col, max_col + 1)]))

print('Part 1: ', empty_tiles)

# 4656 to high