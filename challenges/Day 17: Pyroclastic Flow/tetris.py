input_path = 'advent_of_code_2022/challenges/Day 17: Pyroclastic Flow/input'
from Figure import Horizotal, Plus, L, Vertical, Block

game = None

class Tetris:
  def __init__(self, moves):
    self.moves = moves
    self.next_move = 0
    self.turn = 0
    self.floor = 0
    self.board = {
      '0': { '-1': '-' }, '1': { '-1': '-' }, '2': { '-1': '-' }, '3': { '-1': '-' }, '4': { '-1': '-' }, '5': { '-1': '-' }, '6': { '-1': '-' }
    } # { x: { y: -|1|2|3|4|5 } }
    self.talls = [0, 0, 0, 0, 0, 0, 0]
    self.figure_by_index = [lambda pos: Horizotal(pos), lambda pos: Plus(pos), lambda pos: L(pos), lambda pos: Vertical(pos), lambda pos: Block(pos)]
  
  def next_figure(self): return self.figure_by_index[self.turn % (self.figure_by_index.__len__())]([3, self.max_tall() + 3])
  def max_tall(self): return max(self.talls)

  def update_floor_and_figures(self):
    new_floor = min(self.talls)
    if (new_floor > self.floor):
      self.floor = new_floor

      # Delete unnecessary points
      # for k in self.board.keys():
      #   to_delete = list(filter(lambda y: int(y) < self.floor - 1000, self.board[k]))
      #   for e in to_delete: del self.board[k][e]

  def play_turn(self):
    figure = self.next_figure()
    while(True):
      move = self.next_move % self.moves.__len__()
      dir = self.moves[move]
      figure.move_to_dir(dir, self.board)
      self.next_move += 1

      if (not figure.can_move_down(self.board)): break
      figure.move_down(self.board)

    for point in figure.points:
      x = point[0] + figure.pos[0]
      y = point[1] + figure.pos[1]
      self.talls[x - 3] = max(self.talls[x - 3], point[1] + figure.pos[1] + 1)

      self.board[str(x)][str(y)] = figure.id # Update the board

    self.update_floor_and_figures()
    self.turn += 1
    del figure

with open(input_path) as f:
  for line in f: game = Tetris(line[:-1])

rocks = 100000
for _ in range(rocks): game.play_turn()

print('Part 1: ', game.max_tall())

# for y in reversed(range(-1, game.max_tall() + 1)):
#   print(' '.join([game.board[str(x)][str(y)] if str(y) in game.board[str(x)] else '.' for x in range(0, 7)]))


#   1087248    0.790    0.000    6.099    0.000 Figure.py:18(move_to)
#    100000    0.045    0.000    0.045    0.000 Figure.py:2(__init__)
#    593624    0.245    0.000    3.064    0.000 Figure.py:22(can_move_down)
#    296482    0.124    0.000    1.636    0.000 Figure.py:23(move_left)
#    297142    0.125    0.000    1.804    0.000 Figure.py:24(move_right)
#    493624    0.202    0.000    3.109    0.000 Figure.py:25(move_down)