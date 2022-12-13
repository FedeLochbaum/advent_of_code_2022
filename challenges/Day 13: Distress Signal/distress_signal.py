input_path = 'advent_of_code_2022/challenges/Day 13: Distress Signal/input'
from ast import literal_eval as parse_elem

is_list = lambda x: type(x) is list
is_int = lambda x: type(x) is int

memo = {} # { left: { right: True | False } }
pairs = []; prev = None; indices = []; i = 1

def compare_left_array(left, right, tab):
  if is_int(right): return compare(left, [right], tab)

  for i in range(left.__len__()):
    if (i > right.__len__() - 1): return False
  
    # Let's compare
    result = compare(left[i], right[i], tab + 2)
    if (result != None): return result

  return None if left.__len__() == right.__len__() else True

def compare_left_integer(left, right, tab):
  if is_int(right):
    return None if left == right else left < right
  
  return compare([left], right, tab)

def compare(left, right, tab): # Can return True | False | None ( which means there not evidence than the left value is smaller than the right value )
  evaluator = compare_left_array if is_list(left) else compare_left_integer
  return evaluator(left, right, tab + 2)

with open(input_path) as f:
  for line in f:
    if (line == '\n'): i += 1; prev = None; continue
    side = parse_elem(line[:-1])
    if (prev == None): prev = side; continue

    print('compare left: ', prev, ' vs right: ', side, ' gives -> ', compare(prev, side, 0))
    if (compare(prev, side, 0)): indices.append(i)

print('Part 1: ', sum(indices))
