input_path = 'advent_of_code_2022/challenges/Day 23: Unstable Diffusion/input0'
from collections import deque
from copy import deepcopy

elfs = []; rounds = 10
N = (-1, 0); NE = (-1, 1); E = (0, 1); SE = (1, 1); S = (1, 0); SW = (1, -1); W = (0, -1); NW = (-1, -1)
DIRS = [N, NE, E, SE, S, SW, W, NW]

class Check():
  def __init__(self, dirs, dir):
    self.dirs = dirs
    self.dir = dir

  def check(self, elf): return all(map(lambda dir: (elf[0] + dir[0], elf[1] + dir[1]) not in elfs, self.dirs))
  
  def next(self, elf): return (elf[0] + self.dir[0], elf[1] + self.dir[1])

movements = deque([ Check([N, NE, NW], N), Check([S, SE, SW], S), Check([W, NW, SW], W), Check([E, NE, SE], E) ])
ele_for = lambda r, c: '#' if (r, c) in elfs else '.'

def next_movement_for(elf):
  if '#' not in map(lambda p: ele_for(elf[0] + p[0], elf[1] + p[1]), DIRS): return None

  for move in movements:
    if move.check(elf): return move.next(elf)

def considering_next_movements(elfs):
  next_spaces = {}
  for elf in elfs:
    m = next_movement_for(elf)
    if (m == None): continue # Nothing to do now
    if (m not in next_spaces): next_spaces[m] = []
    next_spaces[m].append(elf)
  return next_spaces

def round(elfs):
  nexts_spaces = considering_next_movements(elfs) # { pos: [elf_pos_1, ..., elf_pos_i] }
  copy_elfs = deepcopy(elfs)

  for _pos in nexts_spaces.keys():
    interested_elfs = nexts_spaces[_pos]
    if (len(interested_elfs) == 1):
      elf = interested_elfs[0]
      if (elf not in nexts_spaces):
        copy_elfs.remove(elf)

      copy_elfs.append(_pos)
  return True, copy_elfs

with open(input_path) as f:
  row = 0
  for line in f:
    r = list(line[:-1])
    for col in range(len(r)):
      if (r[col] == '#'): elfs.append((row, col))
    row += 1

for i in range(rounds):
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

# for r in range(min_row, max_row + 1): print(''.join([ele_for(r, c) for c in range(min_col, max_col + 1)]))

print('Part 1: ', empty_tiles)

# 4656 to high
