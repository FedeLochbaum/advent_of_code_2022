input_path = 'advent_of_code_2022/challenges/Day 19: Not Enough Minerals/input0'
blueprint = None
minutes = 24 # hasta 20 puede explorar
sum = 0
current_max = 0
memo = {}

# blueprint = (ore_robot, clay_robot, obsidian_robot, geode_robot)
# state =
  # (ore, clay, obsidian, geoda) resources
  # (ore_robot, clay_robot, obsidian_robot, geode_robot) robots
  # current_iteration it
#

initial_state = lambda: ((0, 0, 0, 0), (1, 0, 0, 0), 0)

def next_states(state):
  global current_max
  states = []

  ore_to_increment, clay_to_increment, obsidian_to_icrement, geodas_to_increment = state[1]

  next_geodas = state[0][3] + geodas_to_increment

  # priorizing build geode robot
  c_geodes = min( state[0][0] // blueprint[3][0], state[0][2] // blueprint[3][1] )
  ore = state[0][0] - (c_geodes * blueprint[3][0])
  obsidian = state[0][2] - (c_geodes * blueprint[3][1])

  # priorizing build obsidian robots
  count_obsidian = min(ore // blueprint[2][0], state[0][1] // blueprint[2][1])
  ore = ore - (count_obsidian * blueprint[2][0])
  clay = state[0][1] - (count_obsidian * blueprint[2][1])

  next_clay = clay + clay_to_increment
  next_obsidian = obsidian + obsidian_to_icrement

  max_count_clay = ore // blueprint[1]

  for count_clay in range(0, max_count_clay + 1):
    partial_ore = ore - (count_clay * blueprint[1])
    count_ore = partial_ore // blueprint[0]

    partial_ore = partial_ore - (count_ore * blueprint[0])

    _resources = (
      partial_ore + ore_to_increment,
      next_clay,
      next_obsidian,
      next_geodas
    )

    _robots = (
      state[1][0] + count_ore,
      state[1][1] + count_clay,
      state[1][2] + count_obsidian,
      state[1][3] + c_geodes
    )

    new_state = (_resources, _robots, state[2] + 1)
    states.append(new_state)

  return states

def simulate(state):
  global current_max
  if (state[2] == minutes): return state[0][3]
  if (state not in memo):
    _max = 0
    for s in next_states(state): _max = max(_max, simulate(s))
    current_max = max(current_max, _max)
    memo[state] = _max
  return memo[state]

def simulate_blueprint(): global memo; global current_max; current_max = 0; memo = {}; return simulate(initial_state())

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
    simulation = simulate_blueprint()
    print('simulation: ', simulation)
    sum += simulation * index
    index += 1

print('Part 1: ', sum)