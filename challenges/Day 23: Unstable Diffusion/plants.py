input_path = 'advent_of_code_2022/challenges/Day 23: Unstable Diffusion/input'
from collections import deque

elfs = []; rounds = 10
N = (-1, 0); NE = (-1, 1); E = (0, 1); SE = (1, 1); S = (1, 0); SW = (1, -1); W = (0, -1); NW = (-1, -1)
DIRS = [N, NE, E, SE, S, SW, W, NW]

class Check():
  def __init__(self, dirs, dir):
    self.dirs = dirs
    self.dir = dir

  def check(self, elf):
    for dir in self.dirs:
      if (elf[0] + dir[0], elf[1] + dir[1]) in elfs: return False
    return True
  def next(self, elf): return (elf[0] + self.dir[0], elf[1] + self.dir[1])

NonCheck = Check(DIRS, None)
movements = deque([ Check([N, NE, NW], N), Check([S, SE, SW], S), Check([W, NW, SW], W), Check([E, NE, SE], E) ])
ele_for = lambda r, c: '#' if (r, c) in elfs else '.'

def next_movement_for(elf):
  if NonCheck.check(elf): return None

  for move in movements:
    if move.check(elf): return move.next(elf)

def considering_next_movements(elfs):
  next_spaces = {}
  not_valids = []
  for elf in elfs:
    m = next_movement_for(elf)
    if (m == None or m in not_valids): continue # Nothing to do now
    if (m in next_spaces): del next_spaces[m]; not_valids.append(m); continue

    next_spaces[m] = elf

  return len(next_spaces) > 0, next_spaces

def round(elfs):
  r, nexts_spaces = considering_next_movements(elfs) # { pos: [elf_pos_1, ..., elf_pos_i] }
  if (not r): return False, []

  for _pos in nexts_spaces.keys():
    interested_elf = nexts_spaces[_pos]
    if (interested_elf not in nexts_spaces):
      elfs.remove(interested_elf)

    elfs.append(_pos)
  return True, elfs

with open(input_path) as f:
  row = 0
  for line in f:
    r = list(line[:-1])
    for col in range(len(r)):
      if (r[col] == '#'): elfs.append((row, col))
    row += 1

for i in range(1000):
  r, _elfs = round(elfs)
  if(not r): print('Part 2: ', i + 1); break
  elfs = _elfs
  movements.append(movements.popleft())

min_row = float('inf'); min_col = float('inf'); max_row = 0; max_col = 0
for elf in elfs:
  min_row = min(min_row, elf[0])
  max_row = max(max_row, elf[0])

  min_col = min(min_col, elf[1])
  max_col = max(max_col, elf[1])

empty_tiles = 0
for r in range(min_row, max_row + 1):
  for c in range(min_col, max_col + 1):
    if (r, c) not in elfs: empty_tiles += 1

print('Part 1: ', empty_tiles)
