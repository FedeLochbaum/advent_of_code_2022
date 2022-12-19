class Figure:
  def __init__(self, pos, points, id):
    self.pos = pos
    self.points = points
    self.id = id

  def move_to_dir(self, dir, board): (self.move_left if dir == '<' else self.move_right)(board)
  def can_move_to(self, vector, board):
    for p in self.points:
      x = str(p[0] + self.pos[0] + vector[0])
      if x not in board: return False

      y = str(p[1] + self.pos[1] + vector[1])
      if y in board[x]: return False

    return True

  def move_to(self, vector, board):
    if self.can_move_to(vector, board):
      self.pos[0] += vector[0]
      self.pos[1] += vector[1]

  def can_move_down(self, board): return self.can_move_to((0, -1), board)
  def move_left(self, board): self.move_to((-1, 0), board)
  def move_right(self, board): self.move_to((1, 0), board)
  def move_down(self, _): self.pos[1] -= 1

# B1 = ['#','#','#','#']     (-1, 0) | (0, 0) | (1, 0) | (2, 0)
class Horizotal(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (0, 0), (1, 0), (2, 0)], '1')

# B2 = [
#   ['.', '#', '.'],                 | (0, 2) |
#   ['#', '#', '#'],         (-1, 1) | (0, 1) | (1, 1)
#   ['.', '#', '.']                  | (0, 0) |
# ]
class Plus(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 1), (0, 0), (0, 1), (1, 1), (0, 2)], '2')

# B3 = [
#   ['.', '.', '#'],                          | (1, 2)
#   ['.', '.', '#'],                          | (1, 1)
#   ['#', '#', '#']          (-1, 0) | (0, 0) | (1, 0)
# ]
class L(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(- 1, 0), (0, 0), (1, 0), (1, 1), ((1, 2))], '3')

# B4 = [
#   ['#'],                   (-1, 3)
#   ['#'],                   (-1, 2)
#   ['#'],                   (-1, 1)
#   ['#']                    (-1, 0)
# ]
class Vertical(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (-1, 1), (-1, 2), (-1, 3)], '4')

# B5 = [
#   ['#','#'],              (-1, 1) | (0, 1)
#   ['#','#']               (-1, 0) | (0, 0)
# ]
class Block(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (0, 0), (0, 1), (-1, 1)], '5')
