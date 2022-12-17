input_path = 'advent_of_code_2022/challenges/Day 16: Proboscidea Volcanium/input'

initial_time = 30
initial_valve = 'AA'

memo = {} # label -> time -> pressure
rates = {} # label -> flow_rate
graph = {} # label -> [label]
count = 0
initial_state = (initial_valve, initial_time, 0, 0, initial_valve) # Volcano state = (current, missing_time, counter, count_opens, opens)

def possibles_states_from(graph, state):
  next_t = state[1] - 1
  states = []

  if (next_t == 0): return states

  if(state[4].find(state[0]) == -1 and rates[state[0]] > 0):
    states.append((state[0], next_t, state[2] + (rates[state[0]] * next_t), state[3] + 1, state[4] + ',' + state[0]))

  if (next_t == 1): return states

  for valve in graph[state[0]]:
    if (state[4].find(valve) != -1): continue #
    states.append((valve, next_t, state[2], state[3], state[4]))

  return states

def max_flow(graph, state):
  if (state[1] == 0 or (state[3] == count)): return state[2] # cutting

  k = (state[0], state[1], state[2]) 
  if (k not in memo):
    _max = state[2]
    possibles = possibles_states_from(graph, state)
    for s in possibles: _max = max(_max, max_flow(graph, s))

    memo[k] = _max

  return memo[k]

with open(input_path) as f:
  for line in f:
    split = line[:-1].split('; to ')
    valve_split = split[0].split(' has flow ')
    LABEL = valve_split[0][-2:]
    RATE = int(valve_split[1].split('=')[1])

    rates[LABEL] = RATE; memo[LABEL] = {}
    graph[LABEL] = split[1].split(', ')
    if (RATE > 0): count += 1

print(max_flow(graph, initial_state))