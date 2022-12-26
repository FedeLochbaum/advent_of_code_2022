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
    self.graph = {}
    self.blizzards = blizzards
    self.row_size = row_size
    self.col_size = col_size

  def move(self, point):
    add = next[point[0]];
    p = (fix_row(point[1][0] + add[0], self.row_size), fix_col(point[1][1] + add[1], self.col_size))
    return (point[0], p)

  def next_state(self, blizzards): return list(map(self.move, blizzards))

  def __getitem__(self, node):
    str_node = str(node)
    if str_node not in self.graph:
      self.graph[str_node] = {}
      for op in operations(node):
        self.graph[str_node].update({ op[0]: compute_next_state(node, op) })

    return self.graph[str_node]