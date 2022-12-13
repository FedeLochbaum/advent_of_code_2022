input_path = 'advent_of_code_2022/challenges/Day 13: Distress Signal/input'
from functools import cmp_to_key
from ast import literal_eval as parse_elem

is_list = lambda x: type(x) is list
is_int = lambda x: type(x) is int

packages = []; pairs = []; prev = None; indices = []; i = 1

def compare_left_array(left, right):
  if is_int(right): return compare(left, [right])

  for i in range(left.__len__()):
    if (i > right.__len__() - 1): return False
  
    result = compare(left[i], right[i])
    if (result != None): return result

  return None if left.__len__() == right.__len__() else True

def compare_left_integer(left, right):
  if is_int(right):
    return None if left == right else left < right
  
  return compare([left], right)

def compare(left, right):
  evaluator = compare_left_array if is_list(left) else compare_left_integer
  return evaluator(left, right)

with open(input_path) as f:
  for line in f:
    if (line == '\n'): i += 1; prev = None; continue
    side = parse_elem(line[:-1])
    packages.append(side)
    if (prev == None): prev = side; continue
    if (compare(prev, side)): indices.append(i)

div_1 = [[2]]; div_2 = [[6]]; packages.append(div_1); packages.append(div_2)

def compare_f(i, i2):
  res = compare(i, i2)
  if res == True: return -1
  if res == False: return 1
  return 0

print('Part 1: ', sum(indices))
sorted_packages = sorted(packages, key=cmp_to_key(compare_f))
print('Part 2: ', (sorted_packages.index(div_1) + 1) * (sorted_packages.index(div_2) + 1))