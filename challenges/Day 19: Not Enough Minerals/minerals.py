input_path = 'advent_of_code_2022/challenges/Day 19: Not Enough Minerals/input0'

blueprint = None
minutes = 24
sum = 0
memo = {}
initial_state = lambda: ((0, 0, 0), (1, 0, 0, 0), 0) # initial state, only a ore collector

# blueprint = (ore_robot, clay_robot, obsidian_robot, geode_robot)
# state =
  # (ore, clay, obsidian) counts of resources
  # (ore_robot, clay_robot, obsidian_robot, geode_robot)
  # current_iteration
# 

def next_resources_to_add(state): return (state[1][0], state[1][1], state[1][2])

def possible_combinations(resources):
  res = set()
  ore, clay, _ = resources
  max_count_ore = int(ore / blueprint[0])
  max_count_clay = int(clay / blueprint[1])
  max_count_obsidian = int(min(ore / blueprint[2][0], clay / blueprint[2][1]))

  for count_ore in range(0, max_count_ore + 1):
    for count_clay in range(0, max_count_clay + 1):
      for count_obsidian in range(0, max_count_obsidian + 1):
        if ((count_ore * blueprint[0] + (count_obsidian * blueprint[2][0])) > ore): continue
        if ((count_clay * blueprint[1] + (count_obsidian * blueprint[2][1])) > clay): continue

        res.add((count_ore, count_clay, count_obsidian))

  return res

def next_states(state):
  states = set()
  ore_to_increment, clay_to_increment, obsidian_to_icrement = next_resources_to_add(state)
  # priorizing build geode robot
  c_geodes = int(min( state[0][0] / blueprint[3][0], state[0][2] / blueprint[3][1] ))

  rest_resources = (state[0][0] - (c_geodes * blueprint[3][0]), state[0][1], state[0][2] - (c_geodes * blueprint[3][1]))
  # rest_resources = (rest_ore, rest_clay, rest_obsidian)
  for variant in possible_combinations(rest_resources):
    c_ore, c_clay, c_obsidian = variant
    _resources = (
      (rest_resources[0] - (c_ore * blueprint[0]) - (c_obsidian * blueprint[2][0])) + ore_to_increment,
      (rest_resources[1] - (c_clay * blueprint[1]) - (c_obsidian * blueprint[2][1])) + clay_to_increment,
      rest_resources[2] + obsidian_to_icrement
    )

    states.add((
      _resources,
      (state[1][0] + c_ore, state[1][1] + c_clay, state[1][2] + c_obsidian, state[1][3] + c_geodes),
      state[2] + 1
    ))

  return states

def simulate(state):
  if (state[2] >= minutes): return 0
  if (state not in memo): memo[state] = state[1][3] + max(map(simulate, next_states(state)))
  return memo[state]

def simulate_blueprint(): global memo; memo = {}; return simulate(initial_state())

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
    sum += simulate_blueprint() * index
    index += 1

print('Part 1: ', sum)