class Figure:
  def __init__(self, pos, points, id):
    self.pos = pos
    self.points = points
    self.id = id

  def move_to_dir(self, dir, board): (self.move_left if dir == '<' else self.move_right)(board)
  def can_move_to(self, vector, board, points_to_check):
    for p in points_to_check:
      x = str(p[0] + self.pos[0] + vector[0])
      if x not in board: return False

      y = str(p[1] + self.pos[1] + vector[1])
      if y in board[x]: return False

    return True

  def move_to(self, vector, board, points_to_check):
    if self.can_move_to(vector, board, points_to_check):
      self.pos[0] += vector[0]
      self.pos[1] += vector[1]

  def can_move_down(self, board): return self.can_move_to((0, -1), board, self.points_to_check_to_move_down())
  def move_left(self, board): self.move_to((-1, 0), board, self.points_to_check_to_move_left())
  def move_right(self, board): self.move_to((1, 0), board, self.points_to_check_to_move_right())
  def move_down(self, _): self.pos[1] -= 1

  def points_to_check_to_move_down(self): None
  def points_to_check_to_move_left(self): None
  def points_to_check_to_move_right(self): None

# B1 = ['#','#','#','#']     (-1, 0) | (0, 0) | (1, 0) | (2, 0)
class Horizotal(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (0, 0), (1, 0), (2, 0)], '1')
  
  def points_to_check_to_move_left(self): return [(-1, 0)]
  def points_to_check_to_move_right(self): return [(2, 0)]
  def points_to_check_to_move_down(self): return [(0, 0), (1, 0), (-1, 0), (2, 0)]

# B2 = [
#   ['.', '#', '.'],                 | (0, 2) |
#   ['#', '#', '#'],         (-1, 1) | (0, 1) | (1, 1)
#   ['.', '#', '.']                  | (0, 0) |
# ]
class Plus(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 1), (0, 0), (0, 1), (1, 1), (0, 2)], '2')
  
  def points_to_check_to_move_down(self): return [(0, 0), (-1, 1), (1, 1)]
  def points_to_check_to_move_left(self): return [(-1, 1), (0, 0), (0, 2)]
  def points_to_check_to_move_right(self): return [(1, 1), (0, 0), (0, 2)]

# B3 = [
#   ['.', '.', '#'],                          | (1, 2)
#   ['.', '.', '#'],                          | (1, 1)
#   ['#', '#', '#']          (-1, 0) | (0, 0) | (1, 0)
# ]
class L(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(- 1, 0), (0, 0), (1, 0), (1, 1), ((1, 2))], '3')
  
  def points_to_check_to_move_down(self): return [(1, 0), (0, 0), (-1, 0)]
  def points_to_check_to_move_left(self): return [(-1, 0), (1, 1), (1, 2)]
  def points_to_check_to_move_right(self): return [(1, 0), (1, 1), (1, 2)]

# B4 = [
#   ['#'],                   (-1, 3)
#   ['#'],                   (-1, 2)
#   ['#'],                   (-1, 1)
#   ['#']                    (-1, 0)
# ]
class Vertical(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (-1, 1), (-1, 2), (-1, 3)], '4')
  
  def points_to_check_to_move_down(self): return [(-1, 0)]
  def points_to_check_to_move_left(self): return self.points
  def points_to_check_to_move_right(self): return self.points

# B5 = [
#   ['#','#'],              (-1, 1) | (0, 1)
#   ['#','#']               (-1, 0) | (0, 0)
# ]
class Block(Figure):
  def __init__(self, pos):
    super().__init__(pos, [(-1, 0), (0, 0), (0, 1), (-1, 1)], '5')
  
  def points_to_check_to_move_down(self): return [(0, 0), (-1, 0)]
  def points_to_check_to_move_left(self): return [(-1, 0), (-1, 1)]
  def points_to_check_to_move_right(self): return [(0, 0), (0, 1)]