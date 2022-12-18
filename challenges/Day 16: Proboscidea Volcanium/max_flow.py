input_path = 'advent_of_code_2022/challenges/Day 16: Proboscidea Volcanium/input'

initial_time = 26
initial_valve = 'AA'

memo = {} # label -> time -> pressure
rates = {} # label -> flow_rate
graph = {} # label -> [label]
count = 0
initial_state = ((initial_valve, initial_valve), initial_time, 0, 0, initial_valve) # Volcano state = ((current_p1, current_p2), missing_time, counter, count_opens, opens)

def elephant_movements_from_state(state):
  states = []
  # if (state[3] == count): return [state]

  if(rates[state[0][1]] > 0 and state[4].find(state[0][1]) == -1):
    states.append((state[0], state[1], state[2] + (rates[state[0][1]] * state[1]), state[3] + 1, state[4] + ',' + state[0][1]))

  for valve in graph[state[0][1]]:
    if (valve == state[0][0]): continue
    # if (state[4].find(valve) != -1): continue # not sure
    states.append(((state[0][0], valve), state[1], state[2], state[3], state[4]))
  
  return states

def possibles_states_from(graph, state):
  next_t = state[1] - 1
  states = []

  if (next_t < 4): return [] # cutting with branch lvl 15 or fewer

  if (next_t == 0): return states

  if(rates[state[0][0]] > 0 and state[4].find(state[0][0]) == -1):
    states.append((state[0], next_t, state[2] + (rates[state[0][0]] * next_t), state[3] + 1, state[4] + ',' + state[0][0]))

  if (next_t == 1): return states

  for valve in graph[state[0][0]]:
    if (valve == state[0][1]): continue
    # if (state[4].find(valve) != -1): continue # not sure
    states.append(((valve, state[0][1]), next_t, state[2], state[3], state[4]))

  return states

def max_flow(graph, state):
  if (state[1] == 0 or (state[3] == count)): return state[2] # cutting

  k1 = (state[0], state[1], state[2])
  k2 = ((state[0][1], state[0][0]), state[1], state[2])
  if (k1 not in memo and k2 not in memo):
    _max = state[2]
    possibles = possibles_states_from(graph, state)
    for _s in possibles:
      with_help = elephant_movements_from_state(_s)
      for s in with_help:
        _max = max(_max, max_flow(graph, s))
    memo[k1] = _max
    memo[k2] = _max

  return memo[k1]

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