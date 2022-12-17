input_path = 'advent_of_code_2022/challenges/Day 16: Proboscidea Volcanium/input'
from queue import PriorityQueue

initial_time = 30
initial_valve = 'AA'

memo = {} # label -> time -> pressure
rates = {} # label -> flow_rate
graph = {} # label -> [label]
count = 0
initial_state = (initial_valve, initial_time, 0, initial_valve, 0) # Volcano state = (current, missing_time, counter, opens, count_opens)

def possibles_states_from(graph, state):
  next_t = state[1] - 1
  states = []

  if(state[3].find(state[0]) == -1 and rates[state[0]] > 0):
    states.append((state[0], next_t, state[2] + (rates[state[0]] * next_t), state[3] + ',' + state[0], state[4] + 1))

  for valve in graph[state[0]]:
    # if (state[3].find(valve) == -1): continue
    states.append((valve, next_t, state[2], state[3], state[4]))

  return states

def max_flow(graph, initial_state):
  pqueue = PriorityQueue()
  visited = set() # visited states
  pqueue.put(initial_state)
  _max = 0
  while not pqueue.empty():
    state = pqueue.get_nowait()
    if (state[1] == 0 or (state[4] == count)): _max = max(_max, state[2]) # cutting
    else:
      for s in possibles_states_from(graph, state):
        if (s not in visited):
          visited.add(s)
          pqueue.put(s)
  return _max

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