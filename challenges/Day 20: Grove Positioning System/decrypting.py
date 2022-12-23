input_path = 'advent_of_code_2022/challenges/Day 20: Grove Positioning System/input0'

array = []
numbers = {}
L = 5000

with open(input_path) as f:
  for line in f:
    n = int(line[:-1])
    numbers[n] = (array.__len__(), 0)
    array.append(n)

def shift_to(array, _from, dir):
  temp = array[_from]
  focus = (_from + dir) % L
  array[_from] = array[focus]
  array[focus] = temp
  numbers[temp] = (numbers[temp][0], numbers[temp][1] + dir)
  numbers[array[_from]] = (numbers[array[_from]][0], numbers[array[_from]][1] - dir)

def get_move(pos, n):
  # <-
  if (n < 0): return [( L - ( abs(n) - pos ) ) - pos - 1, 1] if (pos + n) <= 0 else [n, -1]

  # ->
  return [pos - ( n - ( L - pos ) ) - 1, -1] if (pos + n) >= L else [n, 1]

def shift_number(array, _from, n):
  count, dir = get_move(_from, n)
  for _ in range(abs(count)):
    shift_to(array, _from, dir)
    _from = _from + dir

def mix_numbers():
  copy = array.copy()
  for i in range(len(array)):
    cur_pos = (numbers[array[i]][0] +  numbers[array[i]][1]) % len(array)
    shift_number(copy, cur_pos, array[i])
  return copy

L = len(array)
new_array = mix_numbers()
print('new array: ', new_array)
i = new_array.index(0)
ns = [new_array[(i + 1000) % L], new_array[(i + 2000) % L], new_array[(i + 3000) % L]]
print('Part 1: ',  sum(ns))


# too low 6419