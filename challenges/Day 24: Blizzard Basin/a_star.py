from queue import PriorityQueue

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  _min = float('inf')
  visited = set()
  pqueue.put((h(initialNode), initialNode, 0)) # priority, pos, steps
  while not pqueue.empty():
    priority, node, deep = pqueue.get_nowait()
    print(' priority, node, deep: ',  priority, node, deep)
    if h(node) == 0:
      _min = min(_min, deep); continue
    for target_node in graph[(node, deep)]:
      if target_node not in visited:
        visited.add(target_node)
        pqueue.put((
          priority + h(target_node),
          target_node,
          deep + 1
        ))
  return _min