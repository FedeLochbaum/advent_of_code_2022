input_path = 'advent_of_code_2022/challenges/Day 11: Monkey in the Middle/input'

current_monkey = None
monkeys = []

op_by = {
  '+': lambda val: lambda old: (old if val == 'old' else int(val)) + old,
  '*': lambda val: lambda old: (old if val == 'old' else int(val)) * old
}

class Monkey():
  def __init__(self):
    self.items = []
    self.divisible_test = None
    self.operation = None
    self.if_true = None
    self.if_false = None
    self.items_inspected = 0
  
  def apply_op(self, val): return self.operation(val)
  def get_items_inspected(self): return self.items_inspected
  def get_item(self, item): self.items.append(item)
  def play(self, monkeys):
    for _ in range(self.items.__len__()):
      item = int(self.apply_op(self.items.pop(0)) / 3)
      throw_to = self.if_true if (item % self.divisible_test) == 0 else self.if_false
      monkeys[throw_to].get_item(item)
      self.items_inspected += 1

def round():
  for monkey in monkeys: monkey.play(monkeys)

with open(input_path) as f:
  for line in f:
    if (line == '\n'): monkeys.append(current_monkey); continue

    splited = line[:-1].strip().split(' ')
    if (splited[0] == 'Monkey'): current_monkey = Monkey(); continue
    if (splited[0] == 'Starting'): current_monkey.items = list(map(lambda x: int(x[:-1] if x[-1] == ',' else x), splited[2:])); continue
    if (splited[0] == 'Operation:'): current_monkey.operation = op_by[splited[-2]](splited[-1]); continue
    if (splited[0] == 'Test:'): current_monkey.divisible_test = int(splited[-1]); continue
    if (splited[0] == 'If' and splited[1] == 'true:'): current_monkey.if_true = int(splited[-1]); continue
    if (splited[0] == 'If' and splited[1] == 'false:'): current_monkey.if_false = int(splited[-1]); continue

monkeys.append(current_monkey)
for i in range(20): round()
print(list(map(lambda m: m.get_items_inspected(), monkeys)))