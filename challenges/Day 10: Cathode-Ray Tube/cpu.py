input_path = 'advent_of_code_2022/challenges/Day 10: Cathode-Ray Tube/input'

state = { 'X': 1, 'cycle': 0, 'queue': [], 'signal_strength': 0, 'pixel': 0  }
pixels = [[]] # Array of arrays of chars

add_process = lambda inst: { 'inst': [inst[0], int(inst[1])], 'wait': 2 }
noop_process = lambda inst: { 'inst': [inst[0]], 'wait': 1 }

def queue_inst(inst):
  process = (add_process if (inst[0] == 'addx') else noop_process)(inst)
  state['queue'].append(process)

def execute(inst):
  if (inst['inst'][0] == 'addx'): state['X'] += inst['inst'][1]

def update_head(state):
  if (state['queue'].__len__() > 0): state['queue'][0]['wait'] -= 1

def execute_inst(state):
  if (state['queue'].__len__() > 0 and (state['queue'][0]['wait'] <= 0)): execute(state['queue'].pop(0))

def draw_pixel(state):
  if (state['cycle'] < 240):
    to_append = '#' if pixels[-1].__len__() in [state['X'] - 1, state['X'], state['X'] + 1] else '.'
    pixels[-1].append(to_append)

def cycle():
  if (state['cycle'] in [20, 60, 100, 140, 180, 220]):
    state['signal_strength'] += (state['X'] * state['cycle'])
  
  if (state['cycle'] in [40, 80, 120, 160, 200, 240]):
    state['pixel'] += 1; pixels.append([])

  execute_inst(state)
  draw_pixel(state)
  update_head(state)
  
  state['cycle'] += 1

with open(input_path) as f:
  for line in f: queue_inst(line[:-1].split(' '))

while(state['queue'].__len__() > 0): cycle()

print('Part 1: ', state['signal_strength'])
for row in pixels: print(''.join(row))