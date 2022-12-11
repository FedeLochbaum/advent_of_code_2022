from math import lcm
input_path = 'advent_of_code_2022/challenges/Day 11: Monkey in the Middle/input'

current_monkey = None; dividing_lcm = 0; monkeys = []

op_by = {
  '+': lambda val: lambda old: (old if val == 'old' else int(val)) + old,
  '*': lambda val: lambda old: (old if val == 'old' else int(val)) * old
}

class Monkey():
  def __init__(self):
    self.items = []
    self.dividend = None
    self.operation = None
    self.if_true = None
    self.if_false = None
    self.items_inspected = 0
  
  def apply_op(self, val): return self.operation(val)
  def get_items_inspected(self): return self.items_inspected
  def get_item(self, item): self.items.append(item)
  def play(self, monkeys, dividing_lcm):
    for _ in range(self.items.__len__()):
      worry_level = self.apply_op(self.items.pop(0)) % dividing_lcm
      throw_to = self.if_true if (worry_level % self.dividend) == 0 else self.if_false
      monkeys[throw_to].get_item(worry_level)
      self.items_inspected += 1

def round(dividing_lcm):
  for monkey in monkeys: monkey.play(monkeys, dividing_lcm)

with open(input_path) as f:
  for line in f:
    if (line == '\n'): monkeys.append(current_monkey); continue

    splited = line[:-1].strip().split(' ')
    if (splited[0] == 'Monkey'): current_monkey = Monkey(); continue
    if (splited[0] == 'Starting'): current_monkey.items = list(map(lambda x: int(x[:-1] if x[-1] == ',' else x), splited[2:])); continue
    if (splited[0] == 'Operation:'): current_monkey.operation = op_by[splited[-2]](splited[-1]); continue
    if (splited[0] == 'Test:'):
      dividend = int(splited[-1])
      dividing_lcm = lcm(dividing_lcm, dividend) if dividing_lcm != 0 else dividend
      current_monkey.dividend = dividend; continue
    if (splited[0] == 'If' and splited[1] == 'true:'): current_monkey.if_true = int(splited[-1]); continue
    if (splited[0] == 'If' and splited[1] == 'false:'): current_monkey.if_false = int(splited[-1]); continue

monkeys.append(current_monkey)
for i in range(10000): round(dividing_lcm)
print(list(map(lambda m: m.get_items_inspected(), monkeys)))