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

class BlizzardMap:
  def __init__(self, blizzards, row_size, col_size):
    self.row_size = row_size
    self.col_size = col_size
    self.goal = (row_size, col_size - 1)
    self.blizzards = self.precompute_blizzards(blizzards, 1000)

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
    blizzard = self.blizzards[time] # Using precomputed state by minute :)
    for n in next.values():
      _pos = (pos[0] + n[0], pos[1] + n[1])

      if _pos == self.goal: next_positions.append(_pos); continue

      # Impossible movements
      if _pos in blizzard: continue
      if _pos[0] < 0 or _pos[0] >= self.row_size: continue
      if _pos[1] < 0 or _pos[1] >= self.col_size: continue
      
      next_positions.append(_pos)

    print('valid points para altura :', time, ' y point: ', pos, ' = ', next_positions)
    return next_positions