input_path = 'advent_of_code_2022/challenges/Day 3: Rucksack Reorganization/input'

# Part 1
NUM = 31

def value(char): return (ord(char) & NUM) + (26 if char.isupper() else 0)

count = 0

with open(input_path) as f:
  for line in f:
    c1 = line[:int(line.__len__() / 2)]
    c2 = line[int(line.__len__() / 2):]
    for c in c2:
      if(c in c1):
        count += value(c)
        break

print('Part 1:', count)

# Part 2
group = []
count = 0

with open(input_path) as f:
  for line in f:
    group.append(line)
    if (group.__len__() == 3):
      for c in group[0]:
        if (c in group[1] and c in group[2]):
          count += value(c)
          break
      group = []

print('Part 2:', count)
