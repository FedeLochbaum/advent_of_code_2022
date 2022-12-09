input_path = 'advent_of_code_2022/challenges/Day 9: Rope Bridge/input'

visited = set()
head = [4, 0]
tail = [4, 0]

next_head_by_side = {
  'R': lambda point: [point[0], point[1] + 1],
  'L': lambda point: [point[0], point[1] - 1],
  'U': lambda point: [point[0] - 1, point[1]],
  'D': lambda point: [point[0] + 1, point[1]]
}

def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def move_diagonal(h, t):
  if (h[1] < t[1]): return [t[0] - 1, t[1] - 1] if h[0] < t[0] else [t[0] + 1, t[1] -1]
  
  return [t[0] - 1, t[1] + 1] if h[0] < t[0] else [t[0] + 1, t[1] + 1]

# def move_lineal(h, t)

def next_tail(p1, p2):
  return (
    move_diagonal(p1, p2)
    if (p1[1] != p2[1] and p1[0] != p2[0])
    else [int((p1[0] + p2[0])/2), int((p1[1] + p2[1])/2)] #move_lineal(p1, p2)
  )

def print_p(r, c, h, t):
  if h == [r, c]: return 'H'
  if t == [r, c]: return 'T'
  return '.'

def print_points(h, t):
  for r in range(5):
    print(' '.join(print_p(r, c, h, t) for c in range(6)))
  print('\n')

def must_update(p1, p2):
  return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) > 1

with open(input_path) as f:
  visited.add(''.join(str(e) for e in tail))
  for line in f:
    side, count = line[:-1].split(' ')
    print('== ', line[:-1] ,' ==\n')
    for _ in range(int(count)):
      head = next_head_by_side[side](head)
      if (must_update(head, tail)):
        tail = next_tail(head, tail)
        visited.add(''.join(str(e) for e in tail))
    print('points: ', ' head: ', head, ' tail: ', tail)

print('Part 1: ', visited.__len__())