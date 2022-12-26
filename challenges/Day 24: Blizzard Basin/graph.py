UP = '^'; DOWN = 'v'; LEFT = '<'; RIGHT = '>'
next = { UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1) }

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
    self.max_time = 300
    self.blizzards = self.precompute_blizzards(blizzards, self.max_time)

  def precompute_blizzards(self, blizzards, times):
    computed = []
    _blizzards = blizzards
    for _ in range(times):
      _blizzards = self.next_state(_blizzards)
      computed.append(_blizzards)
    return computed

  def move(self, point):
    add = next[point[0]];
    p = (fix_row(point[1][0] + add[0], self.row_size), fix_col(point[1][1] + add[1], self.col_size))
    return (point[0], p)

  def next_state(self, blizzards): return list(map(self.move, blizzards))

  def __getitem__(self, node):
    pos, time = node
    next_positions = []
    if (time < self.max_time):
      blizzard = self.blizzards[time] # Using precomputed state by minute :)
      for n in next.values():
        _pos = (pos[0] + n[0], pos[1] + n[1])

        if _pos == self.goal: next_positions.append(_pos); continue

        # Impossible movements
        if _pos in blizzard: continue
        if _pos[0] < 0 or _pos[0] >= self.row_size: continue
        if _pos[1] < 0 or _pos[1] >= self.col_size: continue
        
        next_positions.append(_pos)
      
      # Adding stay movement if the time is not too much
      next_positions.append(pos)
    return next_positions