input_path = 'advent_of_code_2022/challenges/Day 19: Not Enough Minerals/input0'

blueprint = None
minutes = 21 # hasta 20 puede explorar
sum = 0
memo = {}

# blueprint = (ore_robot, clay_robot, obsidian_robot, geode_robot)
# state =
  # (ore, clay, obsidian) resources
  # (ore_robot, clay_robot, obsidian_robot, geode_robot) robots
  # current_iteration it
#

initial_state = lambda: ((0, 0, 0), (1, 0, 0, 0), 0)

def next_resources_to_add(state): return (state[1][0], state[1][1], state[1][2])

def next_states(state):
  states = set()
  next_turn = state[2] + 1
  ore_to_increment, clay_to_increment, obsidian_to_icrement = next_resources_to_add(state)

  # priorizing build geode robot
  c_geodes = int(min( state[0][0] / blueprint[3][0], state[0][2] / blueprint[3][1] ))

  # priorizing build obsidian robots
  ore = state[0][0] - (c_geodes * blueprint[3][0])

  count_obsidian = int(min(ore / blueprint[2][0], state[0][1] / blueprint[2][1]))

  ore = ore - (count_obsidian * blueprint[2][0])
  next_clay = state[0][1] - (count_obsidian * blueprint[2][1]) + clay_to_increment
  next_obsidian = state[0][2] - (c_geodes * blueprint[3][1]) + obsidian_to_icrement

  max_count_ore = int(ore / blueprint[0])
  max_count_clay = int(ore / blueprint[1])

  for count_ore in range(0, max_count_ore + 1):
    for count_clay in range(0, max_count_clay + 1):
      if ((count_ore * blueprint[0] + (count_clay * blueprint[1])) > ore): continue
      
      _resources = (
        (ore - (count_ore * blueprint[0]) - (count_clay * blueprint[1])) + ore_to_increment,
        next_clay,
        next_obsidian
      )

      states.add((
        _resources,
        (state[1][0] + count_ore, state[1][1] + count_clay, state[1][2] + count_obsidian, state[1][3] + c_geodes),
        next_turn
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
    break

print('Part 1: ', sum)