input_path = 'advent_of_code_2022/challenges/Day 4: Camp Cleanup/input'

contained = 0
_overlaps = 0

def contains(r1, r2): return r1[0] <= r2[0] and r1[1] >= r2[1]
def overlaps(r1, r2): return range(max(r1[0],r2[0]), min(r1[1],r2[1])) or None

with open(input_path) as f:
  for line in f:
    r1, r2 = line[:-1].split(',')
    _r1min, _r1max = r1.split('-')
    _r2min, _r2max = r2.split('-')
    r1 = [int(_r1min), int(_r1max) + 1]
    r2  = [int(_r2min), int(_r2max) + 1]
    if (contains(r1, r2) or contains(r2, r1)): contained += 1
    if (overlaps(r1, r2)): _overlaps += 1

print('Part 1: ', contained)
print('Part 2: ', _overlaps)
