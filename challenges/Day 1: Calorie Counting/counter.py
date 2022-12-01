## Get the maximum number of calories ( trivial )
input_path = 'challenges/Day 1: Calorie Counting/input'

maximum = 0
current_mount = 0

## Part 1
## O(n), just getting the greatest value
with open(input_path) as f:
  for line in f:
    if (line == '\n'):
      maximum = max(maximum, current_mount)
      current_mount = 0
      continue
    current_mount += int(line)

print('Part 1: ', maximum)

## Part 2
## O(n), how the input is too small,
## I only need to sort the array, which is lineal and enough good
## Other option could be to use a priority fixed buffer (where we could void sorting a lineal array)

list = []
current_mount_2 = 0

with open(input_path) as f:
  for line in f:
    if (line == '\n'):
      list.append(current_mount_2)
      current_mount_2 = 0
      continue
    current_mount_2 += int(line)

list.sort()

print('Part 2: ', sum(list[-3:]))