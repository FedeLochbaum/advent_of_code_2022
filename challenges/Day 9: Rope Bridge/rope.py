input_path = 'advent_of_code_2022/challenges/Day 9: Rope Bridge/input'

visited = {}
initial_point = [0, 0]
rope = [initial_point] * 10

next_head = {
  'R': lambda point: [point[0], point[1] + 1],
  'L': lambda point: [point[0], point[1] - 1],
  'U': lambda point: [point[0] - 1, point[1]],
  'D': lambda point: [point[0] + 1, point[1]]
}

def move_diagonal(h, t):
  if (h[1] < t[1]): return [t[0] - 1, t[1] - 1] if h[0] < t[0] else [t[0] + 1, t[1] - 1]

  return [t[0] - 1, t[1] + 1] if h[0] < t[0] else [t[0] + 1, t[1] + 1]

def move_lineal(h, t):
  if (h[0] == t[0]): return [t[0], t[1] - 1] if h[1] < t[1] else [t[0], t[1] + 1]

  return [t[0] - 1, t[1]] if h[0] < t[0] else [t[0] + 1, t[1]]

def next_tail(h, t): return (
  move_diagonal(h, t)
  if h[0] != t[0] and h[1] != t[1]
  else move_lineal(h, t)
)

def should_move(h, t): return abs(h[0] - t[0]) == 2 or abs(h[1] - t[1]) == 2

with open(input_path) as f:
  visited[str(initial_point)] = True
  for line in f:
    side, count = line[:-1].split(' ')
    for _ in range(int(count)):
      rope[0] = next_head[side](rope[0])
      for i in range(1, rope.__len__()):
        if (should_move(rope[i - 1], rope[i])):
          rope[i] = next_tail(rope[i - 1], rope[i])
          if ((i == rope.__len__() - 1) and str(rope[i]) not in visited): visited[str(rope[i])] = True

print('Part 2: ', visited.__len__())
