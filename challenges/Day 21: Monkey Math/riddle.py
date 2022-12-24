input_path = 'advent_of_code_2022/challenges/Day 21: Monkey Math/input'

graph = {}

op_by_string = { '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y }
op_inv_by_string = { '+': op_by_string['-'], '-': op_by_string['+'], '*': op_by_string['/'], '/': op_by_string['*'] }

class Human():
  def __init__(self): self.parent = None; self.has_unknown = True
  def set_parent(self, parent_name): self.parent = parent_name
  def has_unkown(self): graph[self.parent].update_has_unkown()
  def update_relationships(self): None
  def propagate_inversive_to(self, N): return N

class Monkey():
  def __init__(self, name, n, dependencies, op):
    self.name = name
    self.dependencies = dependencies
    self.operation = op_by_string[op] if op != None else None
    self.inversive_operation = op_inv_by_string[op] if op != None else None
    self.n = n
    self.parent = None
    self.has_unknown = False

  def set_parent(self, parent_name): self.parent = parent_name
  def update_has_unkown(self):
    self.has_unknown = True
    if (self.parent): graph[self.parent].update_has_unkown()

  def calculate_value(self): self.n = self.operation(graph[self.dependencies[0]].get_value(), graph[self.dependencies[1]].get_value())

  def get_value(self):
    if self.n == None: self.calculate_value()
    return self.n

  def update_relationships(self):
    for child in self.dependencies:
      graph[child].set_parent(self.name)
      graph[child].update_relationships()
  
  def propagate_inversive_to(self, N):
    x, N2 = [self.dependencies[0], graph[self.dependencies[1]].get_value()] if (graph[self.dependencies[0]].has_unknown) else [self.dependencies[1], graph[self.dependencies[0]].get_value()]
    return graph[x].propagate_inversive_to(self.inversive_operation(N, N2))

with open(input_path) as f:
  for line in f:
    name, op = line[:-1].split(': ')
    op = op.split(' ')
    n = int(op[0]) if len(op) == 1 else None
    dependencies = [op[0], op[2]] if len(op) > 1 else []
    graph[name] = Monkey(name, n, dependencies, op[1] if len(op) > 1 else None) if (name != 'humn') else Human()

root = graph['root']
me = graph['humn']

# Updating data
root.update_relationships()
me.has_unkown()

x, N = ([root.dependencies[0], graph[root.dependencies[1]].get_value()] if (graph[root.dependencies[0]].has_unknown)
  else [root.dependencies[1], graph[root.dependencies[0]].get_value()]
)

# print('Part 1: ',root.get_value())
print('Part 2: ', graph[x].propagate_inversive_to(N))