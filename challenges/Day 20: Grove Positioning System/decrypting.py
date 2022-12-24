input_path = 'advent_of_code_2022/challenges/Day 20: Grove Positioning System/input'
array = []
numbers = {}
decryption_key = 811589153
times = 10
L = 0

with open(input_path) as f:
  for line in f:
    n = int(line[:-1]) * decryption_key
    numbers[n] = (len(array), 0)
    array.append(n)

L = len(array)

def shift_to(array, _from, dir):
  temp = array[_from]
  next_pos = (_from + dir) % L
  array[_from] = array[next_pos]
  array[next_pos] = temp
  numbers[temp] = (numbers[temp][0], numbers[temp][1] + dir)
  numbers[array[_from]] = (numbers[array[_from]][0], numbers[array[_from]][1] - dir)
  return next_pos

def get_move(pos, n):
  n = (abs(n) % L) * (-1 if n < 0 else 1)
  # <-
  if (n < 0): return [( L - (( abs(n) - pos ) ) - pos) - 1, 1] if (pos + n) < 0 else [n, -1]

  # ->
  return [pos - ( n - ( L - pos ) ) - 1, -1] if (pos + n) > L else [n, 1]

def shift_number(array, _from, N):
  count, dir = get_move(_from, N)
  for _ in range(count): _from = shift_to(array, _from, dir)

def mix_numbers(original):
  copy = original.copy()
  for i in range(L):
    cur_pos = (numbers[original[i]][0] + numbers[original[i]][1]) % L
    shift_number(copy, cur_pos, original[i])
  return copy

def print_result(a, t):
  i = a.index(0); ns = [a[(i + 1000) % L], a[(i + 2000) % L], a[(i + 3000) % L]]
  print('Part ', t, ': ',  sum(ns))

for i in range(times):
  array = mix_numbers(array)
  if (i == 0): print_result(array, 1)

print_result(array, 2)