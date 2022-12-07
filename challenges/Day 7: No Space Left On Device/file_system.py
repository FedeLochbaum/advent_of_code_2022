input_path = 'advent_of_code_2022/challenges/Day 7: No Space Left On Device/input'

class FileElement():
  def __init__(self, name, parent, size):
    self.parent = parent # To know how to get back
    self.name = name
    self.size = size

  def get_size(self): return self.size
  def is_dir(self): return False
  def print(self, tab = 0): print(' ' * tab, '- ', self.name, '( file, size=', self.size, ')')

class Dir(FileElement):
  def __init__(self, name, parent = None, size = None):
    super().__init__(name, parent, size)
    self.files = {} # To know how to acces to a file

  def elem(self, name): return self.files[name]
  def has_elem(self, name): return name in self.files
  def add_elem(self, elem): self.files[elem.name] = elem

  def print(self, tab = 0):
    print(' ' * tab, '- ', self.name, '( dir, size=', self.get_size(), ')')
    for name in self.files:
      self.files[name].print(tab + 2)

  def is_dir(self): return True

  def get_size(self):
    if (not self.size):
      self.size = sum([self.files[i].get_size() for i in self.files])
    return self.size

  def find_directories(self, f, array):
    for i in self.files:
      elem = self.files[i]
      if (f(elem)): array.append(elem); elem.find_directories(f, array)
    return array

root = Dir('/', None, None)
with open(input_path) as f:
  folder = root
  for line in f:
    splited = line[:-1].split(' ')
    command_or_size = splited[0]
    if (command_or_size == '$'): # Command
      if (splited[1] == 'cd'):
        if (splited[2] == '..'): folder = folder.parent; continue
        else:
          if (not folder.has_elem(splited[2])): folder.add_elem(Dir(splited[2], folder, None))
          folder = folder.elem(splited[2])
      continue
    
    # Listing files
    if (not folder.has_elem(splited[1])):
      elem = Dir(splited[1], folder, None) if command_or_size == 'dir' else FileElement(splited[1], folder, int(command_or_size))
      folder.add_elem(elem)
  
  for i in root.files:
    r = root.files[i].get_size()

delete_as_minimum = 30000000 - (70000000 - root.get_size())
dirs_to_delete = root.find_directories(lambda dir: dir.is_dir() and dir.get_size() >= delete_as_minimum, [])

print(min(e.get_size() for e in dirs_to_delete))