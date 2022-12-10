input_path = 'advent_of_code_2022/challenges/Day 10: Cathode-Ray Tube/input1'

state = { 'X': 1, 'cycle': 0, 'queue': [], 'signal_strength': 0 }

add_process = lambda inst: { 'inst': [inst[0], int(inst[1])], 'wait': 2 }
noop_process = lambda inst: { 'inst': [inst[0]], 'wait': 0 }

def queue_inst(inst):
  process = (add_process if (inst[0] == 'addx') else noop_process)(inst)
  state['queue'].append(process)

def execute(inst):
  if (inst['inst'][0] == 'addx'): state['X'] += inst['inst'][1]

def update_head(state):
  if (state['queue'].__len__() > 0): state['queue'][0]['wait'] -= 1

def execute_inst(state):
  if (state['queue'].__len__() > 0 and (state['queue'][0]['wait'] <= 0)):
    execute(state['queue'].pop(0))

def cycle():
  if (state['cycle'] in [20, 60, 100, 140, 180, 220]):
    state['signal_strength'] += (state['X'] * state['cycle'])

  execute_inst(state)
  update_head(state)
  state['cycle'] += 1

with open(input_path) as f:
  for line in f:
    queue_inst(line[:-1].split(' '))

while(state['queue'].__len__() > 0): cycle()

print('Part 1: ', state['signal_strength'])
