from collections import deque
from functools import reduce
input_path = 'advent_of_code_2022/challenges/Day 5: Supply Stacks/input'

stacks = {}; simulate = False

def move(count, _from, _to):
  sub_array = deque()
  for _ in range(count):
    sub_array.appendleft(stacks[_from - 1].popleft())
  stacks[_to - 1].extendleft(sub_array)

with open(input_path) as f:
  for line in f:
    if (line == '\n'): simulate = True; continue
    if (line[:2] == ' 1'): continue

    if (not simulate):
      consume = line[:-1]
      tops = []
      while consume:
        tops.append(consume[:3])
        consume = consume[4:]
      for i in range(tops.__len__()):
        if (i not in stacks): stacks[i] = deque()
        if (tops[i] != '   '): stacks[i].append(tops[i])
      continue

    # Simulate
    ops = line[:-1].split(' ')
    move(int(ops[1]), int(ops[3]), int(ops[5]))

print('Result: ', reduce(lambda acc, s: acc + stacks[s].popleft()[1:-1], stacks, ''))