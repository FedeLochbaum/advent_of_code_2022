input_path = 'advent_of_code_2022/challenges/Day 19: Not Enough Minerals/input'
from collections import deque

blueprint = None
minutes_1 = 24
minutes_2 = 32
sum = 0; mul = 1

# blueprint = (ore_robot, clay_robot, obsidian_robot, geode_robot)
# state =
  # (ore, clay, obsidian, geoda) resources
  # (ore_robot, clay_robot, obsidian_robot, geode_robot) robots
  # current_iteration it
#

initial_state = lambda minutes: ((0, 0, 0, 0), (1, 0, 0, 0), minutes)

def simulate(minutes):
    _max = 0
    state = initial_state(minutes)
    pqueue = deque([state])
    visited = set()
    while pqueue:
      state = pqueue.popleft()
      resources, robots, time = state
      ore, clay ,obsidian, geode = resources
      robots_ore, robots_clay, robots_obsidian, geode_robot = robots

      _max = max(_max, geode)
      if time == 0: continue
      next_time = time-1

      expensive = max([blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]])

      if robots_ore >= expensive: robots_ore = expensive
      if robots_clay >= blueprint[2][1]: robots_clay = blueprint[2][1]
      if robots_obsidian >= blueprint[3][1]: robots_obsidian = blueprint[3][1]
      if ore >= time * expensive - robots_ore * (next_time): ore = time * expensive - robots_ore * (next_time)
      if clay >= time * blueprint[2][1] - robots_clay * (next_time): clay = time * blueprint[2][1] - robots_clay * (next_time)
      if obsidian >= time * blueprint[3][1] - robots_obsidian * (next_time): obsidian = time * blueprint[3][1] - robots_obsidian * (next_time)

      next_state = ((ore, clay, obsidian, geode), (robots_ore, robots_clay, robots_obsidian, robots[3]), time)

      if next_state in visited: continue
      visited.add(next_state)

      next_r2 = clay + robots_clay; next_r3 = obsidian + robots_obsidian; next_r4 = geode + geode_robot

      pqueue.append((
        (ore + robots_ore, next_r2, obsidian + robots_obsidian, next_r4),
        (robots_ore, robots_clay, robots_obsidian, robots[3]),
        next_time
      ))

      if ore >= blueprint[0]:
          pqueue.append(((ore-blueprint[0] + robots_ore, next_r2, next_r3, next_r4), (robots_ore + 1, robots_clay, robots_obsidian, robots[3]), next_time))

      if ore >= blueprint[1]:
          pqueue.append(((ore-blueprint[1] + robots_ore, next_r2, next_r3, next_r4), (robots_ore, robots_clay + 1, robots_obsidian, robots[3]), next_time))

      if ore >= blueprint[2][0] and clay>=blueprint[2][1]:
          pqueue.append(((ore-blueprint[2][0] + robots_ore, clay-blueprint[2][1] + robots_clay, next_r3, next_r4), (robots_ore, robots_clay , robots_obsidian + 1, robots[3]), next_time))

      if ore >= blueprint[3][0] and obsidian>=blueprint[3][1]:
          pqueue.append(((ore-blueprint[3][0] + robots_ore, next_r2, obsidian-blueprint[3][1] + robots_obsidian, next_r4), (robots_ore, robots_clay, robots_obsidian, robots[3]+1), next_time))

    return _max

with open(input_path) as f:
  index = 1
  for line in f:
    bp = line[:-1].split('.')
    obsidian_robot_split = bp[2].split(' and ')
    geode_robot_split = bp[3].split(' and ')

    ore_robot = int(bp[0][-5])
    clay_robot = int(bp[1][-5])
    obsidian_robot = (int(obsidian_robot_split[0][-5]), int(obsidian_robot_split[1].split(' ')[0]))
    geode_robot = (int(geode_robot_split[0][-5]), int(geode_robot_split[1].split(' ')[0]))

    blueprint = (ore_robot, clay_robot, obsidian_robot, geode_robot)
    sum += simulate(minutes_1) * index
    if index < 4: mul *= simulate(minutes_2)
    index += 1

print('Part 1: ', sum)
print('Part 2: ', mul)