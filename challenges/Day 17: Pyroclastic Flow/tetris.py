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

  def play_turn(self, index):
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

rocks = 1
for i in range(0, rocks): game.play_turn(i)

print('Part 1: ', game.max_tall())

# Part 2 - # Solution

# Each 1700 iterations will repeat the pattern
# Base height before repetion 1007
# Pattern -> +2654 each 1700
# It_pattern -> 1700
# N = 1000000000000

# H(N) = ((N - BASE / It_pattern) * Pattern) + BASE + REST_DIFF
# REST_DIFF = H(660 + (N - BASE % It_pattern)) - 1007