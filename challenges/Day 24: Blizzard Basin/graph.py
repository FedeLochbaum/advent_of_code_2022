UP = '^'; DOWN = 'v'; LEFT = '<'; RIGHT = '>'
next = { UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1) }
possible_movements = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def fix_row(row, row_size):
  if row == -1: return row_size - 1
  if row == row_size: return 0
  return row

def fix_col(col, col_size):
  if col == -1: return col_size - 1
  if col == col_size: return 0
  return col

def elem_to_print(r, c, char_pos, _blizzards):
  for blizzard in _blizzards:
    if blizzard[1] == (r, c): return blizzard[0]
    if char_pos == (r, c): return 'E'
  return '.'

def print_map(_blizzards, char, row_size, col_size):
  for r in range(1, row_size):
    print(''.join([elem_to_print(r, c, char, _blizzards) for c in range(1, col_size)]))

class BlizzardMap:
  def __init__(self, blizzards, row_size, col_size):
    self.row_size = row_size
    self.col_size = col_size
    self.goal = (row_size, col_size - 1)
    self.initial_point = (-1, 0)
    self.max_time = 300
    self.blizzards = self.precompute_blizzards(blizzards, self.max_time)

  def precompute_blizzards(self, blizzards, times):
    computed = [blizzards]
    for _ in range(times):
      computed.append(self.next_state(computed[-1]))
    return computed

  def move(self, point):
    add = next[point[0]];
    p = (fix_row(point[1][0] + add[0], self.row_size), fix_col(point[1][1] + add[1], self.col_size))
    return (point[0], p)

  def next_state(self, blizzards): return list(map(self.move, blizzards))
  def print_map(self, char, time): print_map(self.blizzards[time - 1], char, self.row_size, self.col_size)

  def __getitem__(self, node):
    pos, time = node
    next_positions = []
    if pos == self.initial_point: return [(0, 0)]
    if (time <= self.max_time): # Limiting the depth
      blizzard = self.blizzards[time] # Using precomputed state by minute :)
      for m in possible_movements:
        _pos = (pos[0] + m[0], pos[1] + m[1])

        # If is the goal, go ahead!
        if _pos == self.goal: return [_pos]

        # Impossible movements
        if (_pos in list(map(lambda x: x[1], blizzard))): continue
        if _pos[0] < 0 or _pos[0] >= self.row_size: continue
        if _pos[1] < 0 or _pos[1] >= self.col_size: continue
        
        next_positions.append(_pos)
    return next_positions